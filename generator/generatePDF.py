import os

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from datetime import timedelta
from datetime import date as dt


import datetime


def all_days_between(start_date: datetime.date, end_date: datetime.date):
    delta = end_date - start_date
    days = []
    for i in range(delta.days + 1):
        days.append(start_date + datetime.timedelta(days=i))
    return days


def generatePDF(employees: [object], startDate: datetime.date, endDate: datetime.date):
    
    #Handle employees data
    print(employees)
        
  

    #Handle saving and displaying    
    
    # Create a BytesIO object to hold the PDF data in memory
    pdf_data = BytesIO()

    # Create the PDF object and generate the PDF content
    p = canvas.Canvas(pdf_data, pagesize=landscape((3500, 612)))

    # Draw things on the PDF. Customize this part according to your needs.
    # Example: add your table, text, and other content here.

    # Your code for date generation and adding dates to the data list here...
    data = [[""], ["Kajetan Mieloch"]]
    dates = all_days_between(startDate, endDate)

    # Example: Add the dates to the data list
    for date in dates:
        
        data[0].append(date.strftime("%d-%m-%Y"))

    # Create a table and set its style
    table = Table(data, colWidths=1.5)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold', 12),  # Reduced font size
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    # Your existing code for building the PDF...
    # (i.e., from p.showPage() to p.save())

    # Instead of saving the PDF to a file, show the page and save it to the BytesIO object
    table.wrapOn(p, 0, 0)
    table.drawOn(p, 0, 0)
    p.showPage()
    p.save()

    # Move the BytesIO object's position to the beginning before reading
    pdf_data.seek(0)

    # You can now return the PDF data for rendering or further processing
    return pdf_data.read()