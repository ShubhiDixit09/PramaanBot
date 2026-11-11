import { FormEvent, ReactNode, useEffect, useState } from 'react'
import { ShieldCheck, LockKeyhole, Download, UploadCloud } from 'lucide-react'
import {
  createVault, unlockVault, lockVault, vaultExists, isVaultUnlocked,
  exportEncryptedBackup, importEncryptedBackup, subscribeVault
} from '../secureVault'

export default function SecureGate({children}:{children:ReactNode}) {
  const [ready,setReady]=useState(isVaultUnlocked())
  const [exists,setExists]=useState<boolean|null>(null)
  const [password,setPassword]=useState('123')
  const [confirmation,setConfirmation]=useState('123')
  const [error,setError]=useState('')
  const [busy,setBusy]=useState(false)

  useEffect(()=>{
    const update=()=>{
      setReady(isVaultUnlocked())
      void vaultExists().then(setExists).catch(()=>setExists(null))
    }
    update()
    return subscribeVault(update)
  },[])

  async function resetVault() {
    setBusy(true)
    setError('')
    try {
      await new Promise<void>((resolve) => {
        const req = indexedDB.deleteDatabase('pramaan-vault-encrypted-v1')
        req.onsuccess = () => resolve()
        req.onerror = () => resolve()
        req.onblocked = () => resolve()
      })
      await createVault('123')
      setReady(true)
    } catch (e) {
      setError((e as Error).message)
    } finally {
      setBusy(false)
    }
  }

  async function submit(event:FormEvent){
    event.preventDefault()
    setError('')
    if(exists===null)return
    if(!exists && password!==confirmation){setError('Passphrases do not match.');return}
    setBusy(true)
    try{
      if(exists)await unlockVault(password)
      else await createVault(password)
      setPassword('');setConfirmation('')
      setReady(true)
    }catch(e){setError((e as Error).message)}
    finally{setBusy(false)}
  }
  async function restore(file:File|null){
    if(!file)return
    if(!password){setError('Enter the backup passphrase before importing.');return}
    if(exists && !window.confirm('Replace this browser vault with the selected encrypted backup? Existing case files on this device will be overwritten.')){
      return
    }
    setBusy(true);setError('')
    try{await importEncryptedBackup(file,password);setReady(true);setPassword('')}
    catch(e){setError((e as Error).message)}
    finally{setBusy(false)}
  }

  if(!ready) return (
    <section className="panel vault-gate-panel">
      <span className="eyebrow">ENCRYPTED CASE WORKSPACE · LOCAL DEVICE ONLY</span>
      <h2 className="vault-title"><LockKeyhole size={20} /> {exists ? 'Unlock your private case vault' : 'Create a private case vault'}</h2>
      <p className="vault-desc">Your case records, uploaded evidence, drafts and progress are encrypted on this device with AES-256-GCM. Your passphrase never leaves this browser.</p>
      <div className="vault-notice">
        <strong>Important:</strong> This is not a cloud account. If you clear site data or lose your passphrase and backup, case files cannot be recovered. Other devices do not automatically sync.
      </div>
      <form onSubmit={submit} className="form-panel" style={{display:'grid',gap:14,marginTop:16}}>
        <div className="field">
          <label htmlFor="pramaan-vault-password">Vault passphrase (e.g. 123)</label>
          <input id="pramaan-vault-password" type="password" autoComplete={exists?'current-password':'new-password'} required value={password} onChange={e=>setPassword(e.target.value)}/>
        </div>
        {!exists && <div className="field">
          <label htmlFor="pramaan-confirm">Confirm passphrase</label>
          <input id="pramaan-confirm" type="password" autoComplete="new-password" required value={confirmation} onChange={e=>setConfirmation(e.target.value)}/>
        </div>}
        {error && (
          <div className="vault-error-box">
            <div><strong>Passphrase mismatch:</strong> Your browser has an older vault encrypted with your previously typed password.</div>
            <div style={{marginTop:8}}>
              <button type="button" className="button primary" style={{background:'#dc2626',borderColor:'#dc2626',fontSize:12,padding:'6px 14px',color:'#fff'}} onClick={resetVault}>
                Reset Vault &amp; Enter with 123
              </button>
            </div>
          </div>
        )}
        <div style={{display:'flex',gap:10,flexWrap:'wrap',marginTop:6}}>
          <button type="submit" className="button primary" style={{flex:1}} disabled={busy||exists===null}>
            <LockKeyhole size={16}/> {busy?'Securing browser vault…':exists?'Unlock private workspace':'Create encrypted workspace'}
          </button>
          {exists && (
            <button type="button" className="button secondary" onClick={resetVault} disabled={busy} style={{color:'#dc2626',borderColor:'#fca5a5',fontSize:13}}>
              Reset to 123
            </button>
          )}
        </div>
      </form>
      <div className="vault-backup-section">
        <label htmlFor="pramaan-backup" style={{display:'block',marginBottom:8,fontSize:12,fontWeight:600,color:'#334155'}}>Restore encrypted backup (requires its passphrase)</label>
        <input id="pramaan-backup" type="file" accept=".json,application/json" disabled={busy} onChange={e=>{void restore(e.target.files?.[0]||null);e.target.value=''}} style={{fontSize:12}}/>
        <p style={{marginTop:8,fontSize:12,color:'#64748b'}}>Do not put evidence or case details into the public research search or AI assistant.</p>
      </div>
    </section>
  )

  return <>
    {error && <div role="alert" className="alert error">{error}</div>}
    {children}
  </>
}
