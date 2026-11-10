import SecureGate from './components/SecureGate'
import {
  Accessibility,
  CircleGauge,
  Home,
  Landmark,
  Languages,
  Scale,
  ShieldCheck,
} from 'lucide-react'
import { useEffect, useState } from 'react'
import { Link, NavLink, Navigate, Route, Routes, useLocation } from 'react-router-dom'
import { api } from './api'
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

function PublicLanding() {
  return (
    <section className="dashboard-hero" aria-labelledby="public-title">
      <div className="dashboard-hero-copy">
        <div className="dashboard-hero-topline"><span>PRAMAANBOT / PUBLIC RESEARCH</span><span>READ · VERIFY · LEARN</span></div>
        <h1 id="public-title">Explore Indian law<br /><em>with sources.</em></h1>
        <p>Search the project's small curated set of legal provisions and review public action guides. This preview uses real source ranking, not a generative AI model or an authenticated case-management backend.</p>
        <div className="dashboard-hero-actions">
          <Link className="hero-start" to="/research">Search legal sources</Link>
          <Link className="hero-research" to="/procedures">View action guides</Link>
        </div>
        <p>Informational prototype only. Do not enter names, case details, identity numbers, or other confidential information. The public site does not store private case files.</p>
      </div>
    </section>
  )
}

export default function App() {
  const [health, setHealth] = useState<'checking' | 'online' | 'offline'>('checking')
  const [ollama, setOllama] = useState(false)
  const [aiReady, setAiReady] = useState(false)
  const location = useLocation()
  const isPublicDemo = import.meta.env.PROD
  const currentPage = navigation.find((item) => item.to !== '/' && location.pathname.startsWith(item.to))?.label || (location.pathname.startsWith('/workspace') ? 'Case workspace' : 'Overview')

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
            <span className="civic-label"><Landmark size={14} /> <span lang="hi">डिजिटल विधिक सेवा</span><i /> Digital Legal Services</span>
            <span className="prototype-mark">Public-service prototype</span>
            <span className="civic-tools"><Languages size={14} /> English&nbsp;&nbsp;|&nbsp;&nbsp;<span lang="hi">हिन्दी</span> <Accessibility size={14} /> Accessibility</span>
          </div>
        </div>
        <div className="masthead-brand-bar">
          <div className="site-container masthead-brand-inner">
            <Link className="header-brand" to="/" aria-label="PramaanBot (प्रमाणबॉट) dashboard">
              <span className="header-brand-mark"><Scale size={24} strokeWidth={1.5} /></span>
              <span className="header-brand-copy">
                <span className="brand-name-row">
                  <strong>PramaanBot</strong>
                  <span className="brand-name-divider" aria-hidden="true">|</span>
                  <strong className="brand-name-hindi" lang="hi">प्रमाणबॉट</strong>
                </span>
                <small>Citizen Legal Assistance Platform</small>
              </span>
            </Link>
            <div className="header-actions">
              <span className="header-privacy" title={import.meta.env.DEV ? "Case data remains on your local backend" : "Public demonstration — configure a secure backend before handling case data"}>
                <ShieldCheck size={16} />
                {import.meta.env.DEV ? 'Local & secure' : 'Encrypted on this device'}
              </span>
            </div>
          </div>
        </div>
        <div className="primary-nav-bar">
          <div className="site-container primary-nav-inner">
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
          </div>
        </div>
        <div className="context-strip">
          <div className="site-container context-strip-inner">
            <div className="breadcrumb">
              <Link to="/"><Home size={15} /> <span>{isPublicDemo ? "Public research" : "My cases"}</span></Link>
              <span className="breadcrumb-slash">/</span>
              <strong>{currentPage}</strong>
            </div>
            <div className="status-cluster">
              <span className={`status-dot ${health}`} />
              <span>{health === 'online' ? (isPublicDemo ? 'Public legal research online' : 'API connected') : health === 'offline' ? 'Research API offline' : 'Checking API'}</span>
              <span className="divider" />
              <CircleGauge size={15} />
              <span>{ollama ? 'Gemma connected' : isPublicDemo ? (aiReady ? 'Optional Gemini assistant' : 'Offline source analysis') : 'Safe fallback mode'}</span>
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
              <div><strong>PramaanBot</strong><span>Digital public legal services prototype</span></div>
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
