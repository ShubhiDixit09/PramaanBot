import SecureGate from './components/SecureGate'
import {
  Accessibility,
  CircleGauge,
  Download,
  Landmark,
  Languages,
  LockKeyhole,
  Scale,
  ShieldCheck,
} from 'lucide-react'
import { useEffect, useState } from 'react'
import { Link, NavLink, Navigate, Route, Routes, useLocation } from 'react-router-dom'
import { api } from './api'
import {
  exportEncryptedBackup,
  isVaultUnlocked,
  lockVault,
  subscribeVault,
} from './secureVault'
import Dashboard from './pages/Dashboard'
import Drafts from './pages/Drafts'
import NewCase from './pages/NewCase'
import Procedures from './pages/Procedures'
import Research from './pages/Research'
import Trust from './pages/Trust'
import Workspace from './pages/Workspace'

const navigation = [
  { to: '/', label: 'Overview' },
  { to: '/cases/new', label: 'New case' },
  { to: '/workspace', label: 'Case workspace' },
  { to: '/research', label: 'Legal research' },
  { to: '/procedures', label: 'Action guides' },
  { to: '/drafts', label: 'Documents' },
  { to: '/trust', label: 'Verification' },
]

export default function App() {
  const [health, setHealth] = useState<'checking' | 'online' | 'offline'>('checking')
  const [ollama, setOllama] = useState(false)
  const [aiReady, setAiReady] = useState(false)
  const [vaultUnlocked, setVaultUnlocked] = useState(isVaultUnlocked())
  const location = useLocation()
  const isPublicDemo = import.meta.env.PROD

  useEffect(() => {
    const updateVault = () => setVaultUnlocked(isVaultUnlocked())
    updateVault()
    return subscribeVault(updateVault)
  }, [])

  useEffect(() => {
    api
      .health()
      .then((result) => {
        setHealth('online')
        setOllama(result.ollama.available)
        setAiReady(Boolean(result.ai_assist_configured))
      })
      .catch(() => setHealth('offline'))
  }, [])

  return (
    <div className="app-shell">
      <a className="skip-link" href="#main-content">Skip to main content</a>
      <header className="site-header">
        <div className="civic-ribbon">
          <div className="site-container civic-ribbon-inner">
            <span className="civic-label">
              <Landmark size={13} />
              <span lang="hi">डिजिटल विधिक सेवा</span>
              <i>|</i>
              <span>Digital Legal Services</span>
            </span>
            <span className="civic-tools">
              <Languages size={13} /> English&nbsp;|&nbsp;<span lang="hi">हिन्दी</span>
              <Accessibility size={13} /> Accessibility
            </span>
          </div>
        </div>
        <div className="main-navbar">
          <div className="site-container navbar-inner">
            <Link className="header-brand" to="/" aria-label="PramaanBot dashboard">
              <span className="header-brand-mark"><Scale size={18} strokeWidth={1.75} /></span>
              <div className="header-brand-copy">
                <span className="brand-name-row">
                  <strong>PramaanBot</strong>
                  <span className="brand-name-divider" aria-hidden="true">|</span>
                  <span className="brand-name-hindi" lang="hi">प्रमाणबॉट</span>
                </span>
                <small>Citizen Legal Assistance Platform</small>
              </div>
            </Link>
            <nav className="primary-nav" aria-label="Primary navigation">
              {navigation.map(({ to, label }) => (
                <NavLink
                  key={to}
                  to={to}
                  end={to === '/'}
                  className={({ isActive }) => (isActive ? 'active' : '')}
                >
                  <span>{label}</span>
                </NavLink>
              ))}
            </nav>
            <div className="header-actions">
              <span className={`api-status-pill ${health}`} title={health === 'online' ? 'Public legal research API connected' : 'API offline'}>
                <span className={`status-dot ${health}`} />
                <span>{health === 'online' ? 'Online' : 'Offline'}</span>
              </span>
              {vaultUnlocked ? (
                <div className="header-vault-group">
                  <span className="header-vault-status active" title="Browser vault encrypted with AES-256-GCM">
                    <ShieldCheck size={13} /> Vault Active
                  </span>
                  <button
                    type="button"
                    className="header-mini-btn"
                    onClick={() => void exportEncryptedBackup()}
                    title="Download encrypted backup"
                  >
                    <Download size={12} /> Backup
                  </button>
                  <button
                    type="button"
                    className="header-mini-btn danger"
                    onClick={lockVault}
                    title="Lock vault"
                  >
                    <LockKeyhole size={12} /> Lock
                  </button>
                </div>
              ) : (
                <span className="header-vault-status locked" title="Encrypted on this device">
                  <LockKeyhole size={12} /> Vault Locked
                </span>
              )}
            </div>
          </div>
        </div>
      </header>
      <div className="main-column">
        <main id="main-content" className="site-container">
          {isPublicDemo && location.pathname === '/research' && (
            <div className="civic-notice-banner" role="status">
              <strong>Public source search:</strong> Results come from a small curated corpus. Case files, evidence and drafts use a separate password-encrypted browser vault.
              Google Gemini is called only after a specific consent action with a generic question. Never enter private case details into public search.
              {health === 'offline' ? ' The research API is currently unavailable.' : ''}
            </div>
          )}
          {isPublicDemo ? (
            <Routes>
              <Route path="/" element={<SecureGate><Dashboard /></SecureGate>} />
              <Route path="/cases/new" element={<SecureGate><NewCase /></SecureGate>} />
              <Route path="/workspace" element={<SecureGate><Workspace /></SecureGate>} />
              <Route path="/workspace/:caseId" element={<SecureGate><Workspace /></SecureGate>} />
              <Route path="/research" element={<Research />} />
              <Route path="/procedures" element={<SecureGate><Procedures /></SecureGate>} />
              <Route path="/drafts" element={<SecureGate><Drafts /></SecureGate>} />
              <Route path="/trust" element={<SecureGate><Trust /></SecureGate>} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          ) : (
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/cases/new" element={<NewCase />} />
            <Route path="/workspace" element={<Workspace />} />
            <Route path="/workspace/:caseId" element={<Workspace />} />
            <Route path="/research" element={<Research />} />
            <Route path="/procedures" element={<Procedures />} />
            <Route path="/drafts" element={<Drafts />} />
            <Route path="/trust" element={<Trust />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
          )}
        </main>
        <footer className="site-footer">
          <div className="site-container site-footer-inner">
            <div className="footer-identity">
              <Scale size={24} />
              <div><strong>PramaanBot</strong><span>Citizen Legal Assistance Platform</span></div>
            </div>
            <div className="footer-links">
              <Link to={isPublicDemo ? "/research" : "/trust"}>{isPublicDemo ? "Legal sources" : "Trust & verification"}</Link>
              <Link to="/research">Legal sources</Link>
              <span>Legal information, not legal advice</span>
            </div>
            <div className="footer-status"><ShieldCheck size={15} /> {import.meta.env.DEV ? "Local data stays on your computer" : "Case files and evidence remain encrypted in this browser"}</div>
          </div>
        </footer>
      </div>
    </div>
  )
}
