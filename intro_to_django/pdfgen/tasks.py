import os
from celery import shared_task
from django.conf import settings
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from .models import Report
from reportlab.lib import colors

os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

@shared_task
def generate_pdf_report(report_id):
    report = Report.objects.get(id=report_id)
    report.status = "processing"
    report.save()
    file_path = os.path.join(
        settings.MEDIA_ROOT,
        f"report_{report_id}.pdf"
    )

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    data = [
        ["Name", "Age", "City"],
        ["John", "20", "London"],
        ["David", "15", "Kyiv"],
        ["Vasya", "30", "Lviv"]
    ]

    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.green),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 2, colors.yellow),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgreen)
    ]))
    content = [
        Paragraph(f"Report: {report.title}", styles["Title"]),
        Paragraph(f"Report ID: {report.id}", styles["Normal"]),
        Paragraph(f"Created at: {report.created_at}", styles["BodyText"]),
        table
    ]

    doc.build(content)
    report.file.name = f"report_{report_id}.pdf"
    report.status = "done"
    report.save()

    return "done"