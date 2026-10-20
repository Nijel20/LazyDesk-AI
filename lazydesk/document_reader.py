from io import BytesIO
from pypdf import PdfReader


def read_document(filename: str, file_bytes: bytes) -> str:
    """Extract text from a PDF or plain-text document."""

    if not file_bytes:
        raise ValueError("The uploaded file is empty.")

    if filename.lower().endswith(".pdf"):
        reader = PdfReader(BytesIO(file_bytes))

        if reader.is_encrypted:
            raise ValueError(
                "Password-protected PDFs are not supported yet."
            )

        pages = []

        for page in reader.pages:
            pages.append(page.extract_text() or "")

        text = "\n\n".join(pages)

    elif filename.lower().endswith(".txt"):
        text = file_bytes.decode("utf-8-sig")

    else:
        raise ValueError(
            "Unsupported file type. Upload a PDF or TXT file."
        )

    if not text.strip():
        raise ValueError(
            "No readable text was found in this document."
        )

    return text