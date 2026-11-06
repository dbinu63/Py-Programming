import json, os, re
from pathlib import Path
from datetime import datetime
from tqdm.auto import tqdm

def main(): 
    process_all_receipts(RAW_FOLDER, OUTPUT_FOLDER)

# the main func
def parse_receipt(file_path): 
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        receipt = {}

        # extract business name
        business_match = re.search(r"\n\s+(.*?)\s+\n\s+ABN", content)
        receipt["business_match"] = business_match.group(1) if business_match else None

        # extracting ABN
        abn_match = re.search(r"ABN\s+([0-9 ]+)", content)
        receipt["abn_match"] = abn_match.group(1).replace(" ", "") if abn_match else None

        # extracting date
        date_match = re.search(r"\n\s+(\d{2}/\d{2}/\d{4})\s+\n",content)
        if date_match:
            date_obj = datetime.strptime(date_match.group(1), "%d/%m/%Y")
            receipt["date"] = date_obj.strftime("%Y-%m-%d")
            receipt["month"] = date_obj.month
            receipt["year"] = date_obj.year
        else:
            receipt["date"] = None
            receipt["month"] = None
            receipt["year"] = None

        # extracting terminal
        terminal_match = re.search(r"Terminal\s+(\d+)", content)
        receipt["terminal"] = terminal_match.group(1) if terminal_match else None

        # extracting cashier
        cashier_match = re.search(r"Cashier\s+(.+)", content)
        receipt["cashier"] = cashier_match.group(1).strip() if cashier_match else None

        # extracting customer
        customer_match = re.search(r"Customer\s+(.+)", content)
        receipt["customer"] = customer_match.group(1).strip() if customer_match else None

        # extracting reference
        reference_match = re.search(r"Reference\s+([\d:]+)", content)
        receipt["reference"] = reference_match.group(1) if reference_match else None

        # extracting items
        items = []
        item_section_match = re.search(r"Cashier.*?\n(Customer.*?\n)?(.*?)\n\s*Subtotal", content, re.S) # re.DOTALL and re.S are the same (DOTALL considers everything as a single char, so newlines are abbr, re.S compresses everything into a single line. Both result in the same thing)
        if item_section_match:
            item_pattern = re.compile(r"^\s*([A-Za-z][A-Za-z\s]+?)\s+(\d+)\s+(\d+\.\d{2})\s*$", re.MULTILINE)
            for match in item_pattern.finditer(item_section_match.group(2)):
                quantity = int(match.group(2))
                unit_price = float(match.group(3))
                total = round(quantity * unit_price, 2)

                items.append({
                    "product" : match.group(1),
                    "quantity" : quantity,
                    "unit_price" : unit_price,
                    "total_price" : total
                })
        receipt["items"] = items

        # extracting subtotal
        subtotal_match = re.search(r"Subtotal\s+([\d.]+)", content)
        receipt["subtotal"] = subtotal_match.group(1) if subtotal_match else None

        # extracting GST
        gst_match = re.search(r"GST Included\s+([\d.]+)", content)
        receipt["gst"] = gst_match.group(1) if gst_match else None

        # extracting total
        total_match = re.search(r"Total\s+([\d.]+)", content)
        receipt["total"] = total_match.group(1) if total_match else None

        #extracting payment info
        payment = {}
        payment_section_match = re.search(r"Payments.*?\n(.*?)\nReference", content, re.S)
        if payment_section_match:
            payment_patern = re.compile(r"^\s*([A-Za-z][A-Za-z\s]+?)\s+(\d+\.\d{2})\s*$", re.M) # for the number val here, you can also just do [\d.]+
            for match in payment_patern.finditer(payment_section_match.group(1)):
                payment[match.group(1)] = float(match.group(2))
        receipt["payment"] = payment

    return receipt

def process_all_receipts(raw_folder, output_folder): 
    raw_path = Path(raw_folder)
    output_path = Path(output_folder)

    output_path.mkdir(parents = True, exist_ok = True)

    files = list(raw_path.glob("*.txt"))

    for file in tqdm(files, desc="Processing...", unit="file"):
        try: 
            parsed_data = parse_receipt(file)
            output_file = output_path/(file.stem + ".json")

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(parsed_data, f, indent=4)
        except Exception as e:
            print("File Processing Failed...")


if __name__ == "__main__":
    RAW_FOLDER = "../raw_receipts"
    OUTPUT_FOLDER = "../cleaned_json"
    main()