from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(data, output_path="output/report.pdf"):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph(f"<b>{data.get('topic', '')}</b>", styles["Title"]))
    content.append(Spacer(1, 12))

    # Executive Summary
    if data.get("executive_summary"):
        content.append(Paragraph("<b>Executive Summary</b>", styles["Heading2"]))
        content.append(Paragraph(data["executive_summary"], styles["BodyText"]))
        content.append(Spacer(1, 12))

    # Overview
    content.append(Paragraph("<b>Overview</b>", styles["Heading2"]))
    for item in data.get("overview", []):
        content.append(Paragraph("• " + item, styles["BodyText"]))

    content.append(Spacer(1, 12))

    # Key Concepts
    content.append(Paragraph("<b>Key Concepts</b>", styles["Heading2"]))
    for item in data.get("key_concepts", []):
        if isinstance(item, dict):
            text = f"{item['term']}: {item['description']}"
        else:
            text = item
        content.append(Paragraph("• " + text, styles["BodyText"]))

    content.append(Spacer(1, 12))

    # Facts
    content.append(Paragraph("<b>Important Facts</b>", styles["Heading2"]))
    for item in data.get("important_facts", []):
        content.append(Paragraph("• " + item, styles["BodyText"]))

    doc.build(content)

    return output_path