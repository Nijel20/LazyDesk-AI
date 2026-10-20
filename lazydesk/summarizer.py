from lazydesk.ai_client import generate_response


def summarize_document(document_text: str) -> str:
    """Generate a concise, structured document summary."""

    prompt = f"""
Summarize the document below for someone who wants to save time.

Use these headings:
1. Overview
2. Key Points
3. Important Dates or Deadlines
4. Recommended Next Actions

Only include information supported by the document.
If a section has no relevant information, say so.
Do not invent dates, names, or commitments.

DOCUMENT:
{document_text[:25000]}
"""

    return generate_response(prompt)