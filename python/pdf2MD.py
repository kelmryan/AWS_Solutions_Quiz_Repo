import PyPDF2 as p2
import sys
import re
import correction
from PIL import Image

def extract_relevant_info(rawInfo):
    start_index = None
    end_index = None
    relevant_info = []
    correct_answer = None
    correct_answer_info = []
    for i, line in enumerate(rawInfo):
        if line.startswith("Topic 1 Question"):
            start_index = i
            rawInfo[i + 1] = "### "  + rawInfo[i + 1] # Add '###' before "Topic 1 Question"
            ) 
        if line.startswith("Correct Answer:") and start_index is not None:
            end_index = i + 1
            correct_answer_info = rawInfo[end_index:end_index]
            correct_answer = line.split("Correct Answer:")[1].strip()
            relevant_info.append("**Correct Answer: **" + correct_answer)
            relevant_info.extend(correct_answer_info)
            relevant_info.extend(rawInfo[start_index:end_index])
            relevant_info.append("")
            start_index = None  # Reset start_index to look for the next "Topic 1 Question"    
    return relevant_info

def pdf_to_md(pdfFileName):
    with open(pdfFileName, 'rb') as pdfFile:
        pdfread = p2.PdfFileReader(pdfFile)
        number_of_pages = pdfread.getNumPages()

        with open('results.md', 'w', encoding='utf-8') as md_file:
            for page_number in range(number_of_pages):
                pageinfo = pdfread.getPage(page_number)
                rawText = pageinfo.extractText()
                #remove null
                rawText = re.sub(r'\x00', 'fi', rawText)  # Replace \x00 with fi
                rawInfo = rawText.split('\n')
                relevant_info = extract_relevant_info(rawInfo)

                for line in relevant_info:
                    md_file.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf2md.py <pdf_file>")
    else:
        pdfFileName = sys.argv[1]
        pdf_to_md(pdfFileName)
        correction.correct_answer_parser('results.md')
