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
    
    pdf_data = BytesIO()

    # Create the PDF object and generate the PDF content
    p = canvas.Canvas(pdf_data, pagesize=landscape((3500, 612)))

    # Your code for date generation and adding dates to the data list here...
    data = [[""]]
    dates = all_days_between(startDate, endDate)
    # Example: Add the dates to the data list
    for date in dates:
        data[0].append(date.strftime("%d-%m-%Y"))

    # Your code for adding employee data to the data list here...
    for employee in employees:
        data.append([employee.getNames()])
        for date in dates:
            match_found = False  # Initialize a flag to track if a match is found
            for availability in employee.getAvailability():
                if availability['day'] == date:
                    if availability['availability'] == 'available_in_hours':
                        availability_list = employee.getAvailabilityHours()
                        date_to_find = availability['day']

                        for availability in availability_list:
                            if availability['day'] == date_to_find:
                                start_time = availability['start']
                                end_time = availability['end']
                                data[-1].append(str(start_time) + " - " + str(end_time))
                    else:
                        data[-1].append(availability['availability'])
                    match_found = True  # Set the flag to True when a match is found
                    break  # Exit the availability loop since we found a match
            if not match_found:
                data[-1].append('')


















    # Create a table and set its style
    table = Table(data, colWidths=1.5 * 100)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold', 12),  # Reduced font size
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    # Calculate the width and height of the table
    table_width, table_height = table.wrapOn(p, 0, 0)

    # Position the table at the bottom left corner of the page
    x = 0
    y = 512

    # Draw the table on the PDF
    table.drawOn(p, x, y)

    # Instead of saving the PDF to a file, show the page and save it to the BytesIO object
    p.showPage()
    p.save()

    # Move the BytesIO object's position to the beginning before reading
    pdf_data.seek(0)

    # You can now return the PDF data for rendering or further processing
    return pdf_data.read()