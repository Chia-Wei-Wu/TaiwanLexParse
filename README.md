# Taiwan Lex Parsing

This project is focused on converting Taiwanese legal PDF documents into structured format, which can be used for various NLP applications, including **Retrieval-Augmented Generation** and as **training data for Large Language Models**. By extracting key legal information, such as law names, revision dates, chapters, articles, and content, this tool facilitates the processing of legal documents for downstream tasks like legal research, automated question-answering systems, and more.

## Key Features
- **PDF Text Extraction**: Extract raw text from legal PDF documents.
- **Structured Legal Data**: Convert raw legal text into structured format, including law names, revision dates, chapters, article numbers, and content.
- **Ready for RAG & LLM Training**: The structured data is designed to be used for Retrieval-Augmented Generation or as training data for fine-tuning Large Language Models on legal domains.

## Installation

1. **Python 3.x**: Ensure you have Python 3.x installed on your system.
2. **Dependencies**: Install the required dependencies using `pip`:

```bash
pip install PyPDF2

## Run Script
```bash
python TaiwanLexParse.py doc/passage --input_folder --output_folder




