import os
import json

from utils.export_pdf import create_pdf
from utils.export_ppt import create_ppt

class FormattingAgent:

    def run(self):

        with open("data/cleaned/clean_data.json") as f:
            data = json.load(f)

        print("\nFormatting data...")

        print("Current Working Directory:", os.getcwd())
        print("Output Folder Exists:", os.path.exists("output"))

        pdf_path = create_pdf(data, "output/research_report.pdf")
        ppt_path = create_ppt(data, "output/research_report.pptx")

        print("\nFiles generated:")
        print("PDF:", pdf_path)
        print("PPT:", ppt_path)

        return {
            "pdf": pdf_path,
            "ppt": ppt_path
        }