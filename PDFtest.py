from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import date, timedelta

# Create a larger landscape-oriented PDF
pdf_file = "employee_schedule.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=(3500, 8.5 * inch))

# Create a list to store data for the table
data = [[""], ["Kajetan Mieloch"]]

# Create a list of dates from 01-01-2000 to 31-01-2000
start_date = date(2000, 1, 1)
end_date = date(2000, 1, 31)
delta = timedelta(days=1)
dates = [start_date + delta * i for i in range((end_date - start_date).days + 1)]

# Add the dates to the data list
data[0].extend([date.strftime("%d-%m-%Y") for date in dates])

# Create a table and set its style
table = Table(data, colWidths=1.5 * inch)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold', 12),  # Reduced font size
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
]))

# Create a story to hold the table and add page breaks
story = []
story.append(table)
story.append(PageBreak())

# Build the PDF document
doc.build(story)

print(f"PDF generated: {pdf_file}")
