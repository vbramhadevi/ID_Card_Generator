# ID_Card_Generator

The given project creates a single PDF document with employee ID cards (one employee per page) based on a pre-set ID template image, CSV file with employee information and a folder of employee photos. The ID cards will be of standard size (3.375 x 2.125 inches) with the name of the employee at the bottom-left and a photograph at the top-left.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Features
- Creation of a PDF that contains each employee ID on a separate page.
- Templates ID design (`ute_id_template.png`).
- Reads employee data (name, photo path) in CSV file.
- Adds employee photos and text (name) to every ID.
- Name is placed at bottom-left and the font size is 10 points.
- Title: The title is placed at (1.7 inches x, 0.6 inches up) and has the font size 8.
- Photo will be placed at (0.37 inches x, 0.33 inches of the top) and the dimensions will be 1x1 inch.

## Requirements
- **Python**: Version 3.8 or higher
- **Libraries**:
  - `reportlab`: For PDF generation
  - `pillow`: For image processing
- **Input Files**:
  - `ute_id_template.png`: ID template image (1013x638 pixels for 3.375x2.125 inches at 300 DPI)
  - `employeesData.csv`: CSV file with columns `name`, `photo_path`
  - Employee photos in `src/images/` (e.g., `emp1.jpg`, `emp2.jpg`, `emp3.jpg`, `emp4.jpg`)

Install dependencies via:
```bash
pip install -r requirements.txt
```

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/employee_id_generator.git
   cd employee_id_generator
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Input Files**
   - Place `ute_id_template.png` in `src/`.
   - Place employee photos (e.g., `emp1.jpg`, `emp2.jpg`) in `src/images/`.
   - Create or update `src/employeesData.csv` with the following format:
   ```csv
    name,photo_path
    Pavani,emp1.jpg
    Hrithik,emp2.jpg
    Diya,emp3.jpg
    Brian,emp4.jpg
   ```

## Usage
1. **Navigate to the `src/` directory:**
    ```bash
    cd src
    ```

2. **Run the script:**
    ```bash
    python main.py
    ```

3. **Check the output:**
    - A file named `employee_cards.pdf` will be generated in `src/`.
    - There is one ID card with the template, employee photo and name per page.


