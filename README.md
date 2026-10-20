# 🦥 LazyDesk AI

### Let AI handle the reading. You focus on what matters.

LazyDesk AI is an AI-powered productivity assistant that helps users understand documents faster by generating concise summaries, identifying key points, highlighting important dates and deadlines, and recommending next actions.

Built with Python and Streamlit, LazyDesk AI integrates with Ollama Cloud to provide AI-powered document analysis through a simple, user-friendly interface.

## ✨ Features

- **Document Upload:** Upload PDF and plain-text (TXT) documents.
- **AI-Powered Summarization:** Turn lengthy documents into concise, structured summaries.
- **Key Point Extraction:** Identify the most important information in a document.
- **Deadline Identification:** Highlight important dates and deadlines mentioned in the source document.
- **Recommended Next Actions:** Generate suggested follow-up actions based on document content.
- **Downloadable Summaries:** Download generated summaries in Markdown format.
- **Simple Interface:** Use the application through a browser without needing to interact with the command line during normal operation.

## 🎯 The Problem

Reading and reviewing lengthy documents can consume valuable time, especially for students, professionals, and people managing multiple responsibilities. Important deadlines, action items, and decisions can be overlooked when information is buried in large amounts of text.

LazyDesk AI aims to reduce this burden by helping users identify essential information and understand what they may need to do next.

## 💡 The Solution

LazyDesk AI combines document text extraction with a hosted AI model to transform supported documents into structured summaries. Users upload a document, request a summary, review the results, and download them for future reference.

The application is designed to support productivity, not replace careful reading or professional judgement. Users should verify important dates, commitments, and decisions against the original document.

## 🛠️ Technology Stack

- **Python** — application logic
- **Streamlit** — interactive web interface
- **Ollama Cloud API** — hosted AI inference
- **Requests** — HTTP communication with the AI service
- **pypdf** — PDF text extraction
- **python-dotenv** — environment variable configuration
- **pytest** — testing framework

## 📁 Project Structure

```text
LazyDeskAI/
├── app.py
├── lazydesk/
│   ├── __init__.py
│   ├── ai_client.py
│   ├── document_reader.py
│   ├── summarizer.py
│   ├── task_extractor.py
│   ├── organizer.py
│   └── config.py
├── tests/
│   └── test_utils.py
├── sample_documents/
│   └── .gitkeep
├── outputs/
│   └── .gitkeep
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Before installing LazyDesk AI, ensure you have:

- Python 3.10 or a compatible newer version
- Git, if cloning the repository
- An internet connection
- An Ollama account and a valid API key with access to a supported model

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/LazyDesk-AI.git
cd LazyDesk-AI
```

Replace `YOUR-USERNAME` with the GitHub username that owns the repository.

Alternatively, download the repository as a ZIP file and extract it.

### 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configure Ollama Cloud

Create a `.env` file in the project's root directory, alongside `app.py`.

Add your own API key and a model identifier supported by your Ollama account:

```dotenv
OLLAMA_API_KEY=your_actual_api_key
OLLAMA_MODEL=your_supported_model
OLLAMA_BASE_URL=https://ollama.com/api
```

Replace the placeholder values with your actual configuration. The model name must match a model available to your account through the API.

**Security warning:** Never commit your `.env` file or expose your API key in source code, screenshots, logs, or public posts. The `.gitignore` file should exclude `.env`. Only commit `.env.example` with placeholder values.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal, usually:

```text
http://localhost:8501
```

Open that address in your browser to use LazyDesk AI.

## 📖 How to Use LazyDesk AI

1. Start the application using the command above.
2. Open the local application URL in your browser.
3. Upload a PDF or TXT document.
4. Select **Summarize document**.
5. Wait for the AI to analyse the extracted text.
6. Review the overview, key points, important dates or deadlines, and recommended next actions.
7. Select **Download summary** to save the result as a Markdown file.

## 🔐 Privacy and Security

LazyDesk AI uses Ollama Cloud for AI inference. Document text included in an AI request is transmitted to the hosted service for processing; therefore, this version is **not an entirely offline application**.

- Do not upload confidential or sensitive documents unless you are authorised to share them with the service.
- Keep API credentials in environment variables rather than hardcoding them.
- Avoid committing private documents or generated files containing sensitive information.
- Review the applicable service terms and privacy policy before processing sensitive material.

## 🧪 Testing

The project includes a `tests/` directory for automated tests.

Run the available tests with:

```bash
python -m pytest
```

Additional tests can be added for document extraction, error handling, AI response processing, and summary generation.

## 🗺️ Future Improvements

Planned areas for development include:

- Automated task and deadline extraction into structured lists
- Task prioritisation and completion tracking
- Document categorisation and organisation
- A dashboard for previously processed documents and extracted tasks
- Support for additional document formats
- Improved test coverage and validation
- More robust handling of large documents and API failures

These are potential improvements and should not be considered implemented until they are available in the application.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them.
4. Commit your changes with a descriptive message.
5. Open a pull request describing the improvement.

Please avoid submitting API keys, private documents, or other sensitive information.

## 📄 License

No license has been selected yet. A license should be added before describing the project as open source or granting others explicit reuse rights. Choose a license appropriate for your goals and include its corresponding `LICENSE` file in the repository.

## 👨‍💻 Author

**Project:** LazyDesk AI

**Challenge:** Hacktoberfest 2026 — DEV Challenge Week 3, “Slow and Steady”

**Repository:** Add the public GitHub repository URL after publishing.

---

*LazyDesk AI — Spend less time reading. Spend more time doing.*