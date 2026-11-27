
from pathlib import Path


def read_document(file_path):
    """Read a text document."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def summarize_document(text):
    """Create a basic summary from document text."""
    sentences = text.replace("\n", " ").split(".")
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if not sentences:
        return "Document is empty."

    return ". ".join(sentences[:3]) + "."


if __name__ == "__main__":
    document_path = input("Enter document path: ")

    try:
        document_text = read_document(document_path)
        summary = summarize_document(document_text)

        print("\nDocument Summary:")
        print(summary)

    except Exception as error:
        print("Error:", error)
