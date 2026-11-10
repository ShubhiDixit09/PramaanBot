"""Generates high-resolution, professional Indian Government DPI UI mockup pictures."""
from __future__ import annotations

from pathlib import Path
import pymupdf

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "docs" / "frontend-proposals"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Common styling definitions for Government of India / NIC / eCourts aesthetics
HEADER_COMMON = """
  <!-- Top Sovereign Tricolor Accent -->
  <rect x="0" y="0" width="1440" height="4" fill="#FF9933"/>
  <rect x="480" y="0" width="480" height="4" fill="#FFFFFF"/>
  <rect x="960" y="0" width="480" height="4" fill="#138808"/>

  <!-- Top Civic Ribbon -->
  <rect x="0" y="4" width="1440" height="34" fill="#0b1e36"/>
  <text x="36" y="26" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#cbd5e1" font-weight="600">भारत सरकार | GOVERNMENT OF INDIA</text>
  <text x="250" y="26" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#94a3b8">विधि और न्याय मंत्रालय | MINISTRY OF LAW AND JUSTICE</text>
  <text x="1220" y="26" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#cbd5e1">Accessibility | English | हिन्दी</text>

  <!-- Masthead -->
  <rect x="0" y="38" width="1440" height="80" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <!-- Emblem placeholder circle -->
  <circle cx="68" cy="78" r="24" fill="#0b2545"/>
  <path d="M68 62 L74 72 L62 72 Z M68 76 L76 90 L60 90 Z" fill="#ffffff"/>
  <circle cx="68" cy="80" r="4" fill="#FF9933"/>
  <text x="104" y="72" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700" fill="#0b2545">PramaanPortal</text>
  <text x="260" y="72" font-family="'Segoe UI', Arial, sans-serif" font-size="16" fill="#64748b">|</text>
  <text x="274" y="72" font-family="'Segoe UI', Arial, sans-serif" font-size="20" font-weight="600" fill="#0b2545">प्रमाण पोर्टल</text>
  <text x="104" y="92" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">National Citizen Legal Intelligence & Evidence Action System</text>

  <!-- Masthead status badge -->
  <rect x="1170" y="62" width="234" height="32" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <circle cx="1186" cy="78" r="4" fill="#16a34a"/>
  <text x="1198" y="82" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#334155">Official Public Digital Infrastructure</text>

  <!-- Primary Navigation Bar (Navy Blue) -->
  <rect x="0" y="118" width="1440" height="48" fill="#0b2545"/>
"""

# Screen 1: Executive Dashboard & Citizen Matter Register
SCREEN_1 = f"""<svg width="1440" height="900" viewBox="0 0 1440 900" xmlns="http://www.w3.org/2000/svg">
  <rect width="1440" height="900" fill="#f8fafc"/>
  {HEADER_COMMON}
  <!-- Nav items -->
  <rect x="36" y="118" width="140" height="48" fill="#134074"/>
  <text x="56" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">Matters Overview</text>
  <text x="216" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">File New Matter</text>
  <text x="360" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Active Dossiers</text>
  <text x="496" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Statutory Research</text>
  <text x="656" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Action Checklists</text>
  <text x="806" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Notice Builder</text>
  <text x="946" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Verification Audit</text>

  <!-- Breadcrumb bar -->
  <rect x="0" y="166" width="1440" height="38" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="36" y="190" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">Portal Home  /  Citizen Workspace  /  Matter Register</text>

  <!-- Page Header Banner -->
  <rect x="36" y="222" width="1368" height="96" rx="6" fill="#0b2545"/>
  <text x="68" y="260" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700" fill="#ffffff">Citizen Legal Matter Register</text>
  <text x="68" y="284" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Evidence-grounded statutory analysis, document verification, and formal notice drafting under Indian law.</text>
  <!-- CTA Button inside banner -->
  <rect x="1200" y="248" width="176" height="42" rx="4" fill="#FF9933"/>
  <text x="1232" y="274" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b1e36">+ New Legal Matter</text>

  <!-- Quick Metric Cards -->
  <rect x="36" y="336" width="324" height="88" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="56" y="366" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">ACTIVE GRIEVANCES</text>
  <text x="56" y="402" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="700" fill="#0b2545">03</text>
  <text x="100" y="400" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#16a34a">In progress</text>

  <rect x="384" y="336" width="324" height="88" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="404" y="366" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">INDEXED EVIDENCE FILES</text>
  <text x="404" y="402" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="700" fill="#0b2545">08</text>
  <text x="450" y="400" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0284c7">Parsed agreements & receipts</text>

  <rect x="732" y="336" width="324" height="88" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="752" y="366" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">DRAFTED STATUTORY NOTICES</text>
  <text x="752" y="402" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="700" fill="#0b2545">02</text>
  <text x="798" y="400" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">Ready for review</text>

  <rect x="1080" y="336" width="324" height="88" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="1100" y="366" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">STATUTORY ACCURACY</text>
  <text x="1100" y="402" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="700" fill="#15803d">94%</text>
  <text x="1164" y="400" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">Citation verified</text>

  <!-- Table Container -->
  <rect x="36" y="444" width="1368" height="390" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="60" y="480" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Your Registered Matters</text>

  <!-- Table Header -->
  <rect x="36" y="500" width="1368" height="40" fill="#f1f5f9"/>
  <text x="60" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">CASE ID</text>
  <text x="180" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">SUBJECT & SUMMARY</text>
  <text x="560" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">JURISDICTION</text>
  <text x="720" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">PRIMARY STATUTE</text>
  <text x="960" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">EVIDENCE</text>
  <text x="1100" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">STATUS</text>
  <text x="1260" y="525" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#475569">ACTION</text>

  <!-- Row 1 -->
  <line x1="36" y1="588" x2="1404" y2="588" stroke="#e2e8f0"/>
  <text x="60" y="562" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">PRM-2026-081</text>
  <text x="180" y="556" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0f172a">Unlawful deduction of ₹25,000 security deposit</text>
  <text x="180" y="574" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Tenant vacated premise; landlord withheld deposit without breakdown</text>
  <text x="560" y="562" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#334155">NCT of Delhi</text>
  <text x="720" y="562" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0369a1">Transfer of Property Act, S. 108(m)</text>
  <rect x="960" y="546" width="100" height="24" rx="12" fill="#e0f2fe"/>
  <text x="974" y="562" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">3 Files Parsed</text>
  <rect x="1100" y="546" width="90" height="24" rx="12" fill="#dcfce7"/>
  <text x="1120" y="562" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#15803d">Active</text>
  <rect x="1250" y="546" width="110" height="26" rx="4" fill="#0b2545"/>
  <text x="1268" y="563" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#ffffff">Open Dossier</text>

  <!-- Row 2 -->
  <line x1="36" y1="652" x2="1404" y2="652" stroke="#e2e8f0"/>
  <text x="60" y="626" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">PRM-2026-074</text>
  <text x="180" y="620" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0f172a">E-commerce defective laptop refund refusal</text>
  <text x="180" y="638" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Seller rejected return window despite DOA certificate within 48h</text>
  <text x="560" y="626" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#334155">Uttar Pradesh</text>
  <text x="720" y="626" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0369a1">Consumer Protection Act, S. 35</text>
  <rect x="960" y="610" width="100" height="24" rx="12" fill="#e0f2fe"/>
  <text x="974" y="626" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">2 Files Parsed</text>
  <rect x="1100" y="610" width="90" height="24" rx="12" fill="#fef3c7"/>
  <text x="1114" y="626" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#92400e">Reviewing</text>
  <rect x="1250" y="610" width="110" height="26" rx="4" fill="#0b2545"/>
  <text x="1268" y="627" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#ffffff">Open Dossier</text>

  <!-- Row 3 -->
  <line x1="36" y1="716" x2="1404" y2="716" stroke="#e2e8f0"/>
  <text x="60" y="690" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">PRM-2026-069</text>
  <text x="180" y="684" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0f172a">Cyber financial fraud - unauthorized UPI debit</text>
  <text x="180" y="702" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">₹42,000 deducted through phishing apk; bank dispute pending</text>
  <text x="560" y="690" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#334155">Karnataka</text>
  <text x="720" y="690" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0369a1">IT Act, S. 66D / BNS S. 318(4)</text>
  <rect x="960" y="674" width="100" height="24" rx="12" fill="#e0f2fe"/>
  <text x="974" y="690" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">4 Files Parsed</text>
  <rect x="1100" y="674" width="90" height="24" rx="12" fill="#dcfce7"/>
  <text x="1120" y="690" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#15803d">Active</text>
  <rect x="1250" y="674" width="110" height="26" rx="4" fill="#0b2545"/>
  <text x="1268" y="691" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#ffffff">Open Dossier</text>
</svg>"""

# Screen 2: Intake & Evidence Ingestion Stepper
SCREEN_2 = f"""<svg width="1440" height="900" viewBox="0 0 1440 900" xmlns="http://www.w3.org/2000/svg">
  <rect width="1440" height="900" fill="#f8fafc"/>
  {HEADER_COMMON}
  <!-- Nav items -->
  <text x="56" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Matters Overview</text>
  <rect x="196" y="118" width="140" height="48" fill="#134074"/>
  <text x="216" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">File New Matter</text>
  <text x="360" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Active Dossiers</text>
  <text x="496" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Statutory Research</text>
  <text x="656" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Action Checklists</text>
  <text x="806" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Notice Builder</text>

  <!-- Stepper Bar -->
  <rect x="0" y="166" width="1440" height="64" fill="#ffffff" stroke="#e2e8f0"/>
  <circle cx="200" cy="198" r="14" fill="#0b2545"/>
  <text x="196" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#ffffff" font-weight="700">1</text>
  <text x="224" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b2545">Complainant & Matter</text>

  <line x1="380" y1="198" x2="480" y2="198" stroke="#0b2545" stroke-width="2"/>
  <circle cx="510" cy="198" r="14" fill="#0b2545"/>
  <text x="506" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#ffffff" font-weight="700">2</text>
  <text x="534" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b2545">Evidence Ingestion</text>

  <line x1="680" y1="198" x2="780" y2="198" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="810" cy="198" r="14" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="806" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b" font-weight="700">3</text>
  <text x="834" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#64748b">Statutory Matching</text>

  <line x1="970" y1="198" x2="1070" y2="198" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="1100" cy="198" r="14" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="1096" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b" font-weight="700">4</text>
  <text x="1124" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#64748b">Review & Action Plan</text>

  <!-- Intake Layout -->
  <rect x="36" y="254" width="760" height="580" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="64" y="290" font-family="'Segoe UI', Arial, sans-serif" font-size="18" font-weight="700" fill="#0b2545">Record Your Grievance</text>
  <text x="64" y="312" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">Explain what happened in plain English, Hindi, or Hinglish. Statutory references will be identified automatically.</text>

  <!-- Form Fields -->
  <text x="64" y="356" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#334155">MATTER TITLE *</text>
  <rect x="64" y="366" width="704" height="42" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="80" y="392" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#0f172a">Landlord refusing to refund ₹25,000 security deposit after flat handover</text>

  <text x="64" y="436" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#334155">JURISDICTION / STATE *</text>
  <rect x="64" y="446" width="340" height="42" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="80" y="472" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#0f172a">NCT of Delhi</text>

  <text x="428" y="436" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#334155">ESTIMATED DISPUTED SUM (INR)</text>
  <rect x="428" y="446" width="340" height="42" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="444" y="472" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#0f172a">₹ 25,000</text>

  <text x="64" y="516" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#334155">DETAILED CHRONOLOGICAL STATEMENT *</text>
  <rect x="64" y="526" width="704" height="220" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="80" y="556" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b" width="670">I resided at Flat 402, Rohini Sector 15 under a 11-month lease from 1 July 2025.</text>
  <text x="80" y="580" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b">A security deposit of ₹25,000 was paid via UPI on 01/07/2025.</text>
  <text x="80" y="604" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b">I vacated the premises on 30 June 2026 after handing over the physical keys.</text>
  <text x="80" y="628" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b">The landlord refuses to return the deposit citing arbitrary painting and deep cleaning,</text>
  <text x="80" y="652" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b">without providing any contractor bills, invoices, or photographic proof of damages.</text>

  <rect x="64" y="770" width="160" height="42" rx="4" fill="#0b2545"/>
  <text x="96" y="796" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">Save & Proceed  →</text>

  <!-- Evidence Side Ingestion Panel -->
  <rect x="824" y="254" width="580" height="580" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="852" y="290" font-family="'Segoe UI', Arial, sans-serif" font-size="18" font-weight="700" fill="#0b2545">Evidentiary Document Ingestion</text>
  <text x="852" y="312" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#64748b">Upload rental agreements, payment receipts, bank logs, notices or FIR copies.</text>

  <!-- Upload Dropzone -->
  <rect x="852" y="336" width="524" height="120" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="4 4"/>
  <text x="1010" y="390" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="600" fill="#0b2545">Upload Supporting Evidence</text>
  <text x="960" y="412" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Drag and drop PDF, PNG, JPG files (Max 10MB per file)</text>

  <!-- Parsed Files List -->
  <text x="852" y="486" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#334155">INDEXED EVIDENCE (2 FILES)</text>

  <!-- File 1 Card -->
  <rect x="852" y="504" width="524" height="96" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="872" y="530" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b2545">Rental_Agreement_Signed.pdf</text>
  <rect x="1220" y="516" width="136" height="20" rx="10" fill="#dcfce7"/>
  <text x="1232" y="530" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="600" fill="#15803d">PDF Text Extracted</text>
  <text x="872" y="552" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#334155">Doc Type: Rent Agreement / Lease Deed</text>
  <text x="872" y="572" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Key Facts: ₹25,000 security deposit clause 4; normal wear & tear excluded under clause 8.</text>

  <!-- File 2 Card -->
  <rect x="852" y="616" width="524" height="96" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="872" y="642" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b2545">UPI_Payment_Proof_HDFC.png</text>
  <rect x="1220" y="628" width="136" height="20" rx="10" fill="#e0f2fe"/>
  <text x="1242" y="642" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="600" fill="#0369a1">Receipt Indexed</text>
  <text x="872" y="664" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#334155">Doc Type: Payment Receipt / Transaction Proof</text>
  <text x="872" y="684" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Key Facts: Amount ₹25,000 paid to Landlord account; UTR Ref: 518293019283 on 01/07/2025.</text>
</svg>"""

# Screen 3: Case Dossier & Statutory Analysis Workspace
SCREEN_3 = f"""<svg width="1440" height="900" viewBox="0 0 1440 900" xmlns="http://www.w3.org/2000/svg">
  <rect width="1440" height="900" fill="#f8fafc"/>
  {HEADER_COMMON}
  <!-- Nav items -->
  <text x="56" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Matters Overview</text>
  <text x="216" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">File New Matter</text>
  <rect x="340" y="118" width="140" height="48" fill="#134074"/>
  <text x="360" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">Active Dossiers</text>
  <text x="496" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Statutory Research</text>
  <text x="656" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Action Checklists</text>
  <text x="806" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Notice Builder</text>

  <!-- Dossier Meta Bar -->
  <rect x="0" y="166" width="1440" height="54" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="36" y="198" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Dossier #PRM-2026-081: Tenancy Security Deposit Dispute</text>
  <rect x="520" y="182" width="100" height="22" rx="4" fill="#e2e8f0"/>
  <text x="532" y="197" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#334155">NCT OF DELHI</text>
  <rect x="630" y="182" width="100" height="22" rx="4" fill="#dcfce7"/>
  <text x="644" y="197" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#15803d">EVIDENCE INDEXED</text>

  <rect x="1230" y="176" width="174" height="34" rx="4" fill="#0b2545"/>
  <text x="1250" y="198" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#ffffff">Draft Formal Notice  →</text>

  <!-- Left Column: Case Facts & Evidence Dossier -->
  <rect x="36" y="240" width="670" height="630" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="36" y="240" width="670" height="42" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="56" y="266" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="700" fill="#0b2545">Verified Statement of Facts</text>

  <!-- Fact Summary Cards -->
  <rect x="56" y="300" width="630" height="76" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="76" y="324" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="700" fill="#64748b">COMPLAINANT CLAIM</text>
  <text x="76" y="344" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b">Full refund of ₹25,000 security deposit following completion of 11-month lease tenure.</text>
  <text x="76" y="362" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#64748b">Keys handed over on 30 June 2026; no itemized deduction bill or receipts tendered by landlord.</text>

  <!-- Key Evidence Table -->
  <text x="56" y="410" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b2545">Documentary Evidence on Record</text>

  <rect x="56" y="424" width="630" height="68" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="76" y="448" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">1. Registered Lease Deed (11-Month Residential)</text>
  <text x="76" y="468" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#334155">Clause 4: ₹25,000 deposit refundable within 7 days of handover. Clause 8: Tenant not liable for normal wear &amp; tear.</text>

  <rect x="56" y="502" width="630" height="68" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="76" y="526" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">2. HDFC Bank UPI Debit Receipt</text>
  <text x="76" y="546" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#334155">UTR 518293019283 confirms ₹25,000 transferred to Landlord Bank account on 01/07/2025.</text>

  <rect x="56" y="580" width="630" height="68" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="76" y="604" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">3. WhatsApp Chat &amp; Handover Photographic Record</text>
  <text x="76" y="624" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#334155">Landlord acknowledged key receipt on 30/06/2026. Electronic record authenticated under Section 63 BSA.</text>

  <!-- Right Column: Statutory Grounding & Legal Assessment -->
  <rect x="734" y="240" width="670" height="630" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="734" y="240" width="670" height="42" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="754" y="266" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="700" fill="#0b2545">Statutory Intelligence &amp; Legal Grounds</text>

  <!-- Legal Provisions Cited -->
  <rect x="754" y="300" width="630" height="88" rx="4" fill="#f0f9ff" stroke="#bae6fd"/>
  <text x="774" y="324" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0369a1">Transfer of Property Act, 1882 — Section 108(m)</text>
  <text x="774" y="346" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0c4a6e">Lessee is bound to restore property in as good condition as received, subject to reasonable wear and tear.</text>
  <text x="774" y="366" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0284c7">Ground: Arbitrary deductions for repainting without structural damage violate Section 108(m).</text>

  <rect x="754" y="400" width="630" height="88" rx="4" fill="#f0fdf4" stroke="#bbf7d0"/>
  <text x="774" y="424" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#15803d">Indian Contract Act, 1872 — Section 73 &amp; 74</text>
  <text x="774" y="446" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#14532d">Party suffering breach is entitled to compensation for direct loss; penalty deductions without proof are invalid.</text>
  <text x="774" y="466" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#16a34a">Ground: Withholding of complete ₹25,000 without actual contractor bills constitutes contractual breach.</text>

  <!-- Procedural Action Steps -->
  <text x="754" y="520" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b2545">Recommended Procedural Action Steps</text>
  <rect x="754" y="536" width="630" height="150" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>

  <text x="774" y="564" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#1e293b">1. Issue a formal 15-day Demand Legal Notice citing Lease Clause 4 &amp; 8 and Section 108(m) TPA.</text>
  <text x="774" y="596" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#1e293b">2. Dispatch via Registered Post AD and Speed Post; preserve postal tracking as proof of service.</text>
  <text x="774" y="628" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#1e293b">3. Demand contractor bills and photographic proof for any deduction within 7 business days.</text>
  <text x="774" y="660" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#1e293b">4. Upon non-compliance, initiate summary recovery proceedings before the competent civil jurisdiction.</text>
</svg>"""

# Screen 4: Formal Statutory Notice Builder (A4 Letterhead)
SCREEN_4 = f"""<svg width="1440" height="900" viewBox="0 0 1440 900" xmlns="http://www.w3.org/2000/svg">
  <rect width="1440" height="900" fill="#f8fafc"/>
  {HEADER_COMMON}
  <!-- Nav items -->
  <text x="56" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Matters Overview</text>
  <text x="216" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">File New Matter</text>
  <text x="360" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Active Dossiers</text>
  <text x="496" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Statutory Research</text>
  <text x="656" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Action Checklists</text>
  <rect x="786" y="118" width="140" height="48" fill="#134074"/>
  <text x="806" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">Notice Builder</text>

  <!-- Left Configuration Panel -->
  <rect x="36" y="186" width="400" height="680" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="60" y="222" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Document Drafting Parameters</text>

  <text x="60" y="260" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="700" fill="#64748b">STATUTORY DRAFT TYPE</text>
  <rect x="60" y="270" width="352" height="38" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="294" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0f172a">Legal Notice for Security Deposit Refund</text>

  <text x="60" y="330" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="700" fill="#64748b">ADDRESSED TO (RECIPIENT)</text>
  <rect x="60" y="340" width="352" height="38" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="364" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0f172a">Landlord: Sh. Ramesh Kumar, Rohini, Delhi</text>

  <text x="60" y="400" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="700" fill="#64748b">STATUTORY TIMELINE DEMANDED</text>
  <rect x="60" y="410" width="352" height="38" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="434" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0f172a">15 Days from Receipt of this Notice</text>

  <text x="60" y="470" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="700" fill="#64748b">PRIMARY CLAIMED SUM</text>
  <rect x="60" y="480" width="352" height="38" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="74" y="504" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#0f172a">₹ 25,000 + 18% p.a. statutory interest</text>

  <!-- Download & Action Buttons -->
  <rect x="60" y="550" width="352" height="42" rx="4" fill="#0b2545"/>
  <text x="144" y="576" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">Download A4 PDF Notice</text>

  <rect x="60" y="604" width="352" height="42" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="156" y="630" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#0b2545">Print Official Draft</text>

  <!-- Right Simulated A4 Sheet -->
  <rect x="460" y="186" width="944" height="680" rx="4" fill="#ffffff" stroke="#cbd5e1" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.05))"/>

  <text x="520" y="230" font-family="'Times New Roman', serif" font-size="11" font-weight="700" fill="#000000">BY REGISTERED POST WITH ACKNOWLEDGEMENT DUE / SPEED POST</text>
  <text x="520" y="248" font-family="'Times New Roman', serif" font-size="11" fill="#64748b">Ref: PRM/DL/2026/NOT-081</text>
  <text x="1240" y="248" font-family="'Times New Roman', serif" font-size="11" fill="#000000">Date: 10/11/2026</text>

  <text x="520" y="280" font-family="'Times New Roman', serif" font-size="13" font-weight="700" fill="#000000">FORMAL STATUTORY LEGAL NOTICE UNDER SECTION 106 &amp; 108 OF TRANSFER OF PROPERTY ACT, 1882</text>
  <line x1="520" y1="286" x2="1350" y2="286" stroke="#000000" stroke-width="1"/>

  <text x="520" y="316" font-family="'Times New Roman', serif" font-size="12" font-weight="700" fill="#000000">TO,</text>
  <text x="520" y="334" font-family="'Times New Roman', serif" font-size="12" fill="#000000">Sh. Ramesh Kumar (Landlord),</text>
  <text x="520" y="352" font-family="'Times New Roman', serif" font-size="12" fill="#000000">House No. 124, Pocket B-4, Sector 15, Rohini, New Delhi - 110085.</text>

  <text x="520" y="388" font-family="'Times New Roman', serif" font-size="12" font-weight="700" fill="#000000">SUBJECT: DEMAND FOR IMMEDIATE REFUND OF SECURITY DEPOSIT OF RS. 25,000/- WITH INTEREST</text>

  <text x="520" y="420" font-family="'Times New Roman', serif" font-size="12" fill="#000000">Sir,</text>
  <text x="520" y="444" font-family="'Times New Roman', serif" font-size="12" fill="#1e293b">Under instructions and on behalf of my client, who was your lawful tenant at Flat 402, Rohini, I serve this Notice:</text>
  <text x="520" y="472" font-family="'Times New Roman', serif" font-size="12" fill="#1e293b">1. That my client entered into a registered 11-month lease on 01/07/2025 and deposited a sum of Rs. 25,000/-.</text>
  <text x="520" y="500" font-family="'Times New Roman', serif" font-size="12" fill="#1e293b">2. That on 30/06/2026, my client peacefully vacated the demised premises and returned physical keys.</text>
  <text x="520" y="528" font-family="'Times New Roman', serif" font-size="12" fill="#1e293b">3. That under Section 108(m) of the Transfer of Property Act, 1882, the tenant is exempt from normal wear and tear.</text>
  <text x="520" y="556" font-family="'Times New Roman', serif" font-size="12" fill="#1e293b">4. That your withholding of the entire deposit without contractor receipts constitutes actionable contractual breach.</text>
  <text x="520" y="584" font-family="'Times New Roman', serif" font-size="12" fill="#1e293b">5. That you are hereby called upon to pay the principal sum of Rs. 25,000/- within FIFTEEN (15) DAYS of this notice.</text>

  <text x="520" y="640" font-family="'Times New Roman', serif" font-size="12" font-weight="700" fill="#000000">VERIFIED AND ISSUED BY:</text>
  <text x="520" y="660" font-family="'Times New Roman', serif" font-size="12" fill="#000000">Complainant / Authorized Signatory</text>
  <text x="520" y="678" font-family="'Times New Roman', serif" font-size="11" fill="#64748b">Copy retained for record &amp; court filing</text>
</svg>"""

# Screen 5: Central Statutory Research & Legal Knowledge Base
SCREEN_5 = f"""<svg width="1440" height="900" viewBox="0 0 1440 900" xmlns="http://www.w3.org/2000/svg">
  <rect width="1440" height="900" fill="#f8fafc"/>
  {HEADER_COMMON}
  <!-- Nav items -->
  <text x="56" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Matters Overview</text>
  <text x="216" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">File New Matter</text>
  <text x="360" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Active Dossiers</text>
  <rect x="476" y="118" width="160" height="48" fill="#134074"/>
  <text x="496" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#ffffff">Statutory Research</text>
  <text x="656" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Action Checklists</text>
  <text x="806" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Notice Builder</text>

  <!-- Big Search Header -->
  <rect x="36" y="186" width="1368" height="150" rx="6" fill="#0b2545"/>
  <text x="68" y="226" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700" fill="#ffffff">Indian Central Statutory Archive &amp; Case Matcher</text>
  <text x="68" y="250" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#cbd5e1">Search authenticated provisions across BNS, BNSS, Consumer Protection Act, Transfer of Property Act &amp; Motor Vehicles Act.</text>

  <!-- Search Input Bar -->
  <rect x="68" y="272" width="1120" height="46" rx="4" fill="#ffffff"/>
  <text x="88" y="300" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1e293b">landlord deducted security deposit painting wear and tear</text>
  <rect x="1200" y="272" width="176" height="46" rx="4" fill="#FF9933"/>
  <text x="1246" y="300" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="700" fill="#0b1e36">Search Corpus</text>

  <!-- Filter Category Chips -->
  <rect x="36" y="356" width="110" height="32" rx="16" fill="#0b2545"/>
  <text x="56" y="376" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="#ffffff">All Provisions</text>

  <rect x="156" y="356" width="160" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="176" y="376" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#334155">Consumer Protection</text>

  <rect x="326" y="356" width="160" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="346" y="376" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#334155">Tenancy &amp; Rent Law</text>

  <rect x="496" y="356" width="160" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="516" y="376" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#334155">Criminal (BNS / BNSS)</text>

  <rect x="666" y="356" width="160" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="686" y="376" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#334155">Cyber &amp; Financial Fraud</text>

  <rect x="836" y="356" width="160" height="32" rx="16" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="856" y="376" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#334155">Motor Vehicles / Traffic</text>

  <!-- Cards Grid -->
  <!-- Card 1 -->
  <rect x="36" y="410" width="670" height="210" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="56" y="430" width="110" height="22" rx="4" fill="#e0f2fe"/>
  <text x="68" y="445" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="700" fill="#0369a1">TENANCY LAW</text>
  <rect x="580" y="430" width="106" height="22" rx="4" fill="#dcfce7"/>
  <text x="592" y="445" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="700" fill="#15803d">98% Match Rank</text>
  <text x="56" y="474" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Transfer of Property Act, 1882 — Section 108(m)</text>
  <text x="56" y="496" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">Maintenance of property and reasonable wear and tear</text>
  <text x="56" y="524" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#475569">The lessee is bound to keep and restore the property in as good condition as it was when possessed, subject to reasonable wear and tear or irresistible force. Landlord cannot make arbitrary repainting deductions.</text>
  <line x1="56" y1="564" x2="686" y2="564" stroke="#f1f5f9"/>
  <text x="56" y="590" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">Official Gazette: indiacode.nic.in/bitstream/123456789/2338/1/A1882-04.pdf</text>

  <!-- Card 2 -->
  <rect x="734" y="410" width="670" height="210" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="754" y="430" width="110" height="22" rx="4" fill="#fef3c7"/>
  <text x="766" y="445" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="700" fill="#92400e">CONTRACT LAW</text>
  <rect x="1278" y="430" width="106" height="22" rx="4" fill="#dcfce7"/>
  <text x="1290" y="445" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="700" fill="#15803d">92% Match Rank</text>
  <text x="754" y="474" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Indian Contract Act, 1872 — Section 73</text>
  <text x="754" y="496" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">Compensation for loss or damage caused by contractual breach</text>
  <text x="754" y="524" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#475569">When a contract is broken, the party suffering breach is entitled to compensation for any direct loss or damage naturally arising in the usual course of things. Unilateral deposit forfeiture is actionable.</text>
  <line x1="754" y1="564" x2="1384" y2="564" stroke="#f1f5f9"/>
  <text x="754" y="590" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">Official Gazette: indiacode.nic.in/bitstream/123456789/2187/1/A1872-09.pdf</text>

  <!-- Card 3 -->
  <rect x="36" y="640" width="670" height="210" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="56" y="660" width="110" height="22" rx="4" fill="#dcfce7"/>
  <text x="68" y="675" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="700" fill="#15803d">CONSUMER LAW</text>
  <text x="56" y="704" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Consumer Protection Act, 2019 — Section 35</text>
  <text x="56" y="726" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">Manner in which consumer complaint shall be filed</text>
  <text x="56" y="754" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#475569">A consumer complaint may be filed with the District Commission by an individual, registered association, or groups of consumers. Jurisdiction applies where complainant resides or where opposite party works.</text>
  <line x1="56" y1="794" x2="686" y2="794" stroke="#f1f5f9"/>
  <text x="56" y="820" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">Official Gazette: indiacode.nic.in/bitstream/123456789/15256/5/A2019-35.pdf</text>

  <!-- Card 4 -->
  <rect x="734" y="640" width="670" height="210" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="754" y="660" width="110" height="22" rx="4" fill="#ede9fe"/>
  <text x="766" y="675" font-family="'Segoe UI', Arial, sans-serif" font-size="10" font-weight="700" fill="#6d28d9">CRIMINAL LAW</text>
  <text x="754" y="704" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="#0b2545">Bharatiya Nagarik Suraksha Sanhita, 2023 — Section 173</text>
  <text x="754" y="726" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#334155">Registration of First Information Report (Zero FIR / e-FIR)</text>
  <text x="754" y="754" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#475569">Information relating to cognizable offences may be reported orally or electronically (e-FIR). Mandatory registration of Zero FIR irrespective of police station territorial jurisdiction.</text>
  <line x1="754" y1="794" x2="1384" y2="794" stroke="#f1f5f9"/>
  <text x="754" y="820" font-family="'Segoe UI', Arial, sans-serif" font-size="11" font-weight="600" fill="#0369a1">Official Gazette: indiacode.nic.in/bitstream/123456789/20099/1/eng.pdf</text>
</svg>"""

PROPOSALS = [
    ("01_citizen_portal_overview", SCREEN_1),
    ("02_grievance_intake_and_evidence", SCREEN_2),
    ("03_case_dossier_and_analysis", SCREEN_3),
    ("04_statutory_notice_builder", SCREEN_4),
    ("05_statutory_knowledge_base", SCREEN_5),
]

for name, svg_data in PROPOSALS:
    svg_path = OUTPUT_DIR / f"{name}.svg"
    png_path = OUTPUT_DIR / f"{name}.png"
    svg_path.write_text(svg_data, encoding="utf-8")
    doc = pymupdf.open(stream=svg_data.encode("utf-8"), filetype="svg")
    pix = doc[0].get_pixmap(dpi=150)
    pix.save(str(png_path))
    print(f"Generated: {png_path} ({pix.width}x{pix.height})")

print("All mockups generated successfully in:", OUTPUT_DIR)
