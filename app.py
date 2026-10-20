import streamlit as st

from lazydesk.document_reader import read_document
from lazydesk.summarizer import summarize_document


st.set_page_config(
    page_title="LazyDesk AI",
    page_icon="🦥",
    layout="wide",
)

st.title("🦥 LazyDesk AI")
st.subheader("Let AI handle the reading. You focus on what matters.")

st.write(
    "Upload a document and get a concise summary, "
    "important points, deadlines, and suggested next actions."
)

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt"],
    help="Supported formats: PDF and plain-text files.",
)

if uploaded_file is not None:
    st.success(f"Ready to process: {uploaded_file.name}")

    if st.button("Summarize document", type="primary"):
        try:
            with st.spinner("Reading your document..."):
                document_text = read_document(
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                )

            with st.spinner("LazyDesk AI is preparing your summary..."):
                summary = summarize_document(document_text)

            st.markdown("## Your AI Summary")
            st.markdown(summary)

            st.download_button(
                label="Download summary",
                data=summary,
                file_name="lazydesk_summary.md",
                mime="text/markdown",
            )

        except Exception as exc:
            st.error(str(exc))

st.divider()
st.caption(
    "LazyDesk AI | Open-source AI-powered productivity project"
)