from pathlib import Path
from ai_summarizer import summarize_document


class DocumentSummaryAgent:

    def run(self, file_path):
        path = Path(file_path)

        if not path.exists():
            print("Document not found!")
            return

        document = path.read_text(encoding="utf-8")

        print("\nAgent is reading the document...")

        summary = summarize_document(document)

        print("\nAgent's Document Summary:\n")
        print(summary)


if __name__ == "__main__":
    agent = DocumentSummaryAgent()

    document_path = input("Enter document path: ")

    agent.run(document_path)