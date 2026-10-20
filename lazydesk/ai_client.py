import requests

from lazydesk.config import (
    OLLAMA_API_KEY,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)


def generate_response(prompt: str) -> str:
    """Send a prompt to Ollama Cloud and return its response."""

    if not OLLAMA_API_KEY:
        raise RuntimeError(
            "Ollama API key is missing. Add it to your .env file."
        )

    if not prompt.strip():
        raise ValueError("The prompt cannot be empty.")

    url = f"{OLLAMA_BASE_URL.rstrip('/')}/chat"

    headers = {
        "Authorization": f"Bearer {OLLAMA_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are LazyDesk AI, a helpful assistant that "
                    "summarizes documents clearly and accurately. "
                    "Do not invent facts absent from the document."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "stream": False,
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=180,
        )
        response.raise_for_status()
        data = response.json()

        return data["message"]["content"]

    except requests.Timeout as exc:
        raise RuntimeError(
            "The AI request timed out. Please try again."
        ) from exc

    except requests.RequestException as exc:
        raise RuntimeError(
            "Could not connect to Ollama Cloud. Check your "
            "internet connection, API key, and model availability."
        ) from exc

    except (KeyError, TypeError, ValueError) as exc:
        raise RuntimeError(
            "Ollama returned an unexpected response."
        ) from exc