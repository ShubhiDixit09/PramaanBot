"""Document Intelligence & Entity Extraction service for PramaanBot backend."""
from __future__ import annotations

import re
from typing import Any


def extract_text_from_pdf(content: bytes) -> str:
    """Extract text chunks from PDF streams using standard PDF operators."""
    try:
        binary = content.decode("latin1", errors="ignore")
    except Exception:
        return ""

    chunks: list[str] = []
    # Match standard Tj operators
    tj_pattern = re.compile(r"\(([^)]+)\)\s*Tj", re.IGNORECASE)
    for match in tj_pattern.finditer(binary):
        raw = match.group(1).replace(r"\(", "(").replace(r"\)", ")").replace(r"\\", "\\").strip()
        if raw:
            chunks.append(raw)

    # Match array TJ operators
    array_tj_pattern = re.compile(r"\[([^\]]+)\]\s*TJ", re.IGNORECASE)
    for match in array_tj_pattern.finditer(binary):
        inner = match.group(1)
        sub_strings = re.findall(r"\(([^)]+)\)", inner)
        combined = "".join(sub_strings).replace(r"\(", "(").replace(r"\)", ")").replace(r"\\", "\\").strip()
        if combined:
            chunks.append(combined)

    if len(" ".join(chunks)) < 40:
        words = re.findall(r"[A-Za-z0-9₹.,/-]{3,}", binary)
        legal_keywords = {"agreement", "tenant", "landlord", "rent", "deposit", "police", "fir", "notice", "consumer", "invoice", "receipt", "rs", "section"}
        if any(w.lower() in legal_keywords for w in words):
            chunks.extend(w for w in words[:250] if not re.match(r"^(obj|endobj|stream|endstream|xref|trailer|catalog|pages)$", w, re.I))

    return " ".join(chunks)[:25000].strip()


def analyze_document_content(filename: str, text: str, media_type: str) -> dict[str, Any]:
    """Classify document and extract legal entities (dates, parties, amounts, key findings)."""
    combined = f"{filename} {text}".lower()

    doc_type = "General Evidence"
    if re.search(r"rent.*agreement|lease|tenan|landlord|flat|premises|deposit", combined):
        doc_type = "Rent Agreement / Lease Deed"
    elif re.search(r"fir|first information|police|station|ps|cognizable|bns|bnss", combined):
        doc_type = "Police Complaint / FIR"
    elif re.search(r"legal.*notice|demand.*notice|advocate|counsel", combined):
        doc_type = "Legal Notice / Demand Notice"
    elif re.search(r"upi|transaction|receipt|payment.*proof|transfer|utr", combined):
        doc_type = "Payment Receipt / Transaction Proof"
    elif re.search(r"invoice|bill|tax.*invoice|order.*id|delivery|warranty", combined):
        doc_type = "Consumer Invoice / Bill"
    elif re.search(r"challan|traffic|e-challan|speed|signal|vehicle", combined):
        doc_type = "Traffic Challan"
    elif re.search(r"rti|public information|pio|appellate", combined):
        doc_type = "RTI Application / Order"

    # Extract dates
    dates = list(set(re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)))[:5]

    # Extract amounts (₹ or Rs.)
    amounts = list(set(f"₹{m}" for m in re.findall(r"(?:₹|rs\.?|inr)\s*([\d,]+(?:\.\d{2})?)", text, re.I) if len(m) >= 2))[:5]

    # Extract parties
    parties = []
    if re.search(r"landlord|lessor", combined):
        parties.append("Landlord / Lessor")
    if re.search(r"tenant|lessee", combined):
        parties.append("Tenant / Lessee")
    if re.search(r"complainant", combined):
        parties.append("Complainant")
    if re.search(r"respondent|accused|opposite party", combined):
        parties.append("Opposite Party")
    if re.search(r"buyer|consumer", combined):
        parties.append("Consumer / Buyer")
    if re.search(r"seller|merchant|dealer", combined):
        parties.append("Seller / Merchant")

    findings = []
    if amounts:
        findings.append(f"Identified amounts: {', '.join(amounts)}")
    if dates:
        findings.append(f"Extracted dates: {', '.join(dates)}")
    if re.search(r"wear.*tear", text, re.I):
        findings.append("Contains normal wear & tear exception clause")
    if re.search(r"deposit|security", text, re.I):
        findings.append("References security deposit return obligations")

    summary = f"Identified as {doc_type}."
    if amounts:
        summary += f" Reflects monetary value of {amounts[0]}."
    if parties:
        summary += f" Involves: {', '.join(parties)}."

    return {
        "parser": "pdf-stream-extractor" if "pdf" in media_type else ("plain-text" if "text" in media_type else "image-analyzer"),
        "vision_status": "Document text extracted and entities indexed",
        "doc_type": doc_type,
        "extracted_text": text[:15000],
        "dates": dates,
        "amounts": amounts,
        "parties": parties,
        "key_findings": findings,
        "summary": summary,
        "stored_locally": True,
    }
