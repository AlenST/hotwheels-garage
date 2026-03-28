import json
import openpyxl
import os

EXCEL_FILE = 'List.xlsx'
OUTPUT_JS = 'cars_data.js'

def excel_to_json():
    wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
    sheet = wb.active
    headers = [cell.value for cell in sheet[1]]
    cars = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if all(cell is None or cell == '' for cell in row):
            continue
        car = {}
        for idx, header in enumerate(headers):
            if header:
                car[header] = row[idx] if row[idx] is not None else ''
        cars.append(car)
    return cars

def write_js_file(cars):
    js_content = f"// Auto-generated from {EXCEL_FILE}\nconst carData = {json.dumps(cars, ensure_ascii=False, indent=2)};\n"
    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"✅ Generated {OUTPUT_JS} with {len(cars)} cars.")

if __name__ == '__main__':
    if not os.path.exists(EXCEL_FILE):
        print(f"❌ {EXCEL_FILE} not found! Please place your Excel file in this folder.")
        exit(1)
    cars = excel_to_json()
    write_js_file(cars)