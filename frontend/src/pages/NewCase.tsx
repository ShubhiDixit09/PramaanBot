import { ArrowRight, LockKeyhole, MessageSquareText } from 'lucide-react'
import { FormEvent, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api'
import { ErrorBanner, PageHeader } from '../components'
import { localStore } from '../store'

const depositExample = {
  title: 'Landlord is refusing to return my security deposit',
  description:
    'Main Delhi mein rented flat mein rehti thi. Maine 1 July 2025 ko ₹25,000 security deposit diya tha. ' +
    'Main 30 June 2026 ko flat vacate kar chuki hoon and keys bhi landlord ko return kar di thi. ' +
    'Landlord keh rahe hain ki painting aur cleaning ke charges cut honge, but unhone koi proper bill ya written calculation share nahi ki. ' +
    'Mere repeated calls aur WhatsApp messages ke baad bhi deposit return nahi kiya gaya. ' +
    'Mere paas rent agreement, UPI payment screenshot, keys handover ke messages aur WhatsApp chats hain. ' +
    'Main jaana chahti hoon ki mujhe kya steps lene chahiye aur landlord ko bhejne ke liye ek formal notice draft chahiye.',
  jurisdiction: 'Delhi',
  language: 'Hinglish' as const,
  urgency: 'medium' as const,
}

export default function NewCase() {
  const navigate = useNavigate()
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [form, setForm] = useState({
    title: '',
    description: '',
    jurisdiction: 'Delhi',
    language: 'Hinglish' as const,
    urgency: 'medium' as const,
  })

  const submit = async (event: FormEvent) => {
    event.preventDefault()
    setBusy(true)
    setError('')
    try {
      const created = await api.createCase(form)
      localStore.setCaseId(created.id)
      localStore.clearAnalysis()
      navigate(`/workspace/${created.id}`)
    } catch (err) {
      setError((err as Error).message)
    } finally {
      setBusy(false)
    }
  }

  return (
    <>
      <PageHeader
        eyebrow="Case intake · New matter"
        title="Tell us what happened."
        description="Use your own words in English, Hindi, or Hinglish. No legal terminology required."
        action={
          <button className="button secondary" type="button" onClick={() => setForm(depositExample)} style={{fontSize:12,height:32}}>
            Load deposit dispute example
          </button>
        }
      />
      {error && <ErrorBanner message={error} />}
      <form className="form-layout" onSubmit={submit}>
        <div className="panel form-panel">
          <div className="field">
            <label htmlFor="title">Short case title</label>
            <input
              id="title"
              required
              minLength={3}
              maxLength={160}
              placeholder="e.g. Landlord refusing to return security deposit"
              value={form.title}
              onChange={(event) => setForm({ ...form, title: event.target.value })}
            />
          </div>
          <div className="field">
            <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline'}}>
              <label htmlFor="description">What happened?</label>
              <small style={{fontSize:11,color:'#64748b'}}>{form.description.length}/10,000 characters</small>
            </div>
            <textarea
              id="description"
              required
              minLength={10}
              rows={5}
              placeholder="Dates, parties involved, what you agreed on, and what outcome you are seeking…"
              value={form.description}
              onChange={(event) => setForm({ ...form, description: event.target.value })}
            />
          </div>
          <div className="field-grid">
            <div className="field">
              <label htmlFor="jurisdiction">State / jurisdiction</label>
              <select
                id="jurisdiction"
                value={form.jurisdiction}
                onChange={(event) => setForm({ ...form, jurisdiction: event.target.value })}
              >
                {['Delhi', 'Haryana', 'Uttar Pradesh', 'Rajasthan', 'Other / not sure'].map((value) => (
                  <option key={value}>{value}</option>
                ))}
              </select>
            </div>
            <div className="field">
              <label htmlFor="language">Preferred language</label>
              <select
                id="language"
                value={form.language}
                onChange={(event) =>
                  setForm({ ...form, language: event.target.value as typeof form.language })
                }
              >
                <option>Hinglish</option><option>English</option><option>Hindi</option>
              </select>
            </div>
            <div className="field">
              <label htmlFor="urgency">Urgency</label>
              <select
                id="urgency"
                value={form.urgency}
                onChange={(event) =>
                  setForm({ ...form, urgency: event.target.value as typeof form.urgency })
                }
              >
                <option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option>
              </select>
            </div>
          </div>
          <button className="button primary wide" disabled={busy} style={{marginTop:6}}>
            {busy ? 'Creating encrypted case…' : 'Create case workspace'} <ArrowRight size={16} />
          </button>
        </div>
        <aside className="form-aside">
          <div className="aside-card">
            <LockKeyhole size={18} />
            <div>
              <strong>Stored locally &amp; encrypted</strong>
              <span>{import.meta.env.PROD ? 'Your case facts are encrypted with AES-256-GCM in IndexedDB and never sent to a cloud case database.' : 'Your facts are saved directly to your local database.'}</span>
            </div>
          </div>
          <div className="aside-card">
            <MessageSquareText size={18} />
            <div>
              <strong>Everyday language works</strong>
              <span>“Landlord deposit nahi de raha” is enough. The legal engine identifies the applicable Acts and provisions automatically.</span>
            </div>
          </div>
        </aside>
      </form>
    </>
  )
}


