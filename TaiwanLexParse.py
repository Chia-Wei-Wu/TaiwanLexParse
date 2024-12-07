#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, re, json, sys
from PyPDF2 import PdfReader

def parse_doc(pdf_path, output_path):
    try:
        reader = PdfReader(pdf_path)
        all_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                all_text += text.strip() + "\n"
        if not all_text:
            print(f"No text extracted from {pdf_path}")
            return
        file_name = os.path.splitext(os.path.basename(pdf_path))[0]
        data = {
            "law": file_name,
            "content": all_text.strip(),
            "type": "doc"
        }
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump([data], file, ensure_ascii=False, indent=4)
        print(f"Successfully processed doc: {pdf_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")


def parse_passage(pdf_path, output_path):
    try:
        reader = PdfReader(pdf_path)
        all_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                all_text += text.strip() + "\n"
        if not all_text:
            print(f"No text extracted from {pdf_path}")
            return

        parsed_data = parse_content(all_text)
        
        if not parsed_data:
            print(f"No parsed data from {pdf_path}")
            return

        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(parsed_data, file, ensure_ascii=False, indent=4)

        print(f"Successfully processed passage: {pdf_path} -> {output_path}")
    except Exception as e:
        print(f"Error: {e}")


def parse_content(content):
    data = []
    law_name = ""
    revision_date = ""
    chapter = ""
    lines = content.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        match_law_name = re.match(r"法規名稱：(.+)", line)
        if match_law_name:
            law_name = match_law_name.group(1)
            continue
        match_revision_date = re.match(r"修正日期：(.+)", line)
        if match_revision_date:
            revision_date = match_revision_date.group(1)
            continue
        match_chapter = re.match(r"第\s*(\S+)\s*章\s*(.+)", line)
        if match_chapter:
            chapter = match_chapter.group(2)
            continue
        match_article = re.match(r"第\s*(\S+)\s*條", line)
        if match_article:
            current_article_number = match_article.group(1)
            article_content = re.sub(r"^條", "", line.split(f"條", 1)[-1]).strip()
            data.append({
                "law": law_name,
                "date": revision_date,
                "章": chapter,
                "條": f"第{current_article_number}條",
                "content": article_content,
                "type": "passage"
            })
            continue
        if data:
            data[-1]["content"] += f" {line}"

    return data


def process_files(input_path, output_folder, mode):
    if not os.path.exists(input_path):
        print(f"Error: Input path does not exist: {input_path}")
        return
    os.makedirs(output_folder, exist_ok=True)
    if os.path.isfile(input_path) and input_path.endswith(".pdf"):
        pdf_files = [input_path]
    elif os.path.isdir(input_path):
        pdf_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(".pdf")]
        if not pdf_files:
            print(f"No PDF files found in the directory: {input_path}")
            return
    else:
        print(f"Invalid input path. It should be a PDF file or a directory: {input_path}")
        return
    for pdf_file in pdf_files:
        file_name = os.path.splitext(os.path.basename(pdf_file))[0]
        output_path = os.path.join(output_folder, f"{file_name}.json")
        try:
            if mode == "doc":
                parse_doc(pdf_file, output_path)
            elif mode == "passage":
                parse_passage(pdf_file, output_path)
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python TaiwanLexParse.py <mode: doc|passage> <input_path> <output_folder>")
    else:
        mode = sys.argv[1]
        input_path = sys.argv[2]
        output_folder = sys.argv[3]

        process_files(input_path, output_folder, mode)

