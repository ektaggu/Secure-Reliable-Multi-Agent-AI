
from pathlib import Path
import logging
import time

from ai_summarizer import summarize_document


# Configure audit logging
logging.basicConfig(
    filename="document_summary_agent/agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class DocumentSummaryAgent:

    def run(self, file_path):
        start_time = time.time()

        logging.info("Agent execution started")
        logging.info("Input document: %s", file_path)

        path = Path(file_path)

        if not path.exists():
            logging.error("Document not found: %s", file_path)
            print("Document not found!")
            return

        try:
            document = path.read_text(encoding="utf-8")
            logging.info("Document successfully loaded")

            print("\nAgent is reading the document...")

            summary = summarize_document(document)

            logging.info("Document summary generated successfully")

            execution_time = time.time() - start_time

            logging.info(
                "Execution time: %.2f seconds",
                execution_time
            )

            print("\nAgent's Document Summary:\n")
            print(summary)

            logging.info("Summary output: %s", summary)
            logging.info("Agent execution completed successfully")

        except Exception:
            logging.exception("Agent execution failed")
            print("An error occurred. Check agent.log")


if __name__ == "__main__":
    agent = DocumentSummaryAgent()

    document_path = input("Enter document path: ")

    agent.run(document_path)
