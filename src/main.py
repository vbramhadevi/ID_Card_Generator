import csv
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image

ID_WIDTH = 3.375 * inch
ID_HEIGHT = 2.125 * inch
PHOTO_SIZE = (300, 300)  # 1 inch x 1 inch at 300 DPI


def read_employee_data(csv_path):
    try:
        with open(csv_path, newline='') as file:
            reader = csv.DictReader(file)
            print("CSV Headers:", reader.fieldnames)
            return list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


def resize_photo(photo_path, temp_name):
    try:
        img = Image.open(photo_path)
        img = img.resize(PHOTO_SIZE, Image.LANCZOS)
        img.save(temp_name)
        return temp_name
    except Exception as e:
        print(f"Error processing photo {photo_path}: {e}")
        return None


def draw_id_card(c, template_path, employee, photo_path, index):
    name = employee['name'].strip()
    title = employee.get('title', '').strip()  # Use empty string if title is missing

    # Draw background/template
    c.drawImage(template_path, 0, 0, width=ID_WIDTH, height=ID_HEIGHT)

    # Draw photo if it exists
    if os.path.exists(photo_path):
        temp_photo = f"temp_photo_{index}_{name.replace(' ', '_')}.png"
        resized_photo = resize_photo(photo_path, temp_photo)
        if resized_photo:
            c.drawImage(resized_photo, 1.95 * inch, 0.8 * inch,
                        width=1 * inch, height=1 * inch)
            os.remove(temp_photo)
    else:
        print(f"Photo not found: {photo_path}")

    # Draw text
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.3 * inch, 0.28 * inch, name)
    c.setFont("Helvetica", 8)
    c.drawString(0.3 * inch, 0.7 * inch, title)

    c.showPage()


def create_id_pdf(template_path, csv_path, photo_dir, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=(ID_WIDTH, ID_HEIGHT))
    employees = read_employee_data(csv_path)

    for index, row in enumerate(employees):
        if not all(k in row and row[k].strip() for k in ['name', 'photo_path']):
            print(f"Skipping row due to missing data: {row}")
            continue

        photo_path = os.path.join(photo_dir, row['photo_path'].strip())
        print(f"Processing ID for {row['name']} with photo {photo_path}")
        draw_id_card(c, template_path, row, photo_path, index)

    c.save()
    print(f"PDF successfully generated: {output_pdf}")


if __name__ == "__main__":
    create_id_pdf(
        template_path="ute_id_template.png",
        csv_path="employeesData.csv",
        photo_dir="images",
        output_pdf="employee_cards.pdf"
    )