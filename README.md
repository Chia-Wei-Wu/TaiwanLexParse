# Taiwan Lex Parsing

This project is focused on converting Taiwanese legal PDF documents into structured JSON format, which can be used for various NLP applications, including **Retrieval-Augmented Generation (RAG)** and as **training data for Large Language Models (LLMs)**. By extracting key legal information, such as law names, revision dates, chapters, articles, and content, this tool facilitates the processing of legal documents for downstream tasks like legal research, automated question-answering systems, and more.

## Key Features
- **PDF Text Extraction**: Extract raw text from legal PDF documents.
- **Structured Legal Data**: Convert raw legal text into structured JSON format, including law names, revision dates, chapters, article numbers, and content.
- **Ready for RAG & LLM Training**: The structured JSON data is designed to be used for Retrieval-Augmented Generation (RAG) or as training data for fine-tuning Large Language Models (LLMs) on legal domains.

## Installation

1. **Python 3.x**: Ensure you have Python 3.x installed on your system.
2. **Dependencies**: Install the required dependencies using `pip`:

```bash
pip install PyPDF2

