"""
computeSales.py

Computes the total cost of all sales based on a price catalogue.
"""

import json
import sys
import time
import os


def load_json_file(file_path):
    """Loads a JSON file and returns its content."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error reading {file_path}: {error}")
        return None


def compute_total_sales(price_catalogue, sales_records):
    """Computes total sales amount."""
    total = 0.0

    for sale in sales_records:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_catalogue:
            print(f"Product not found in catalogue: {product}")
            continue

        if not isinstance(quantity, int) or quantity < 0:
            print(f"Invalid quantity for product {product}: {quantity}")
            continue

        total += price_catalogue[product] * quantity

    return total


def main():
    """Main entry point of the program."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print(
              "Usage: python computeSales.py priceCatalogue.json "
              "salesRecord.json"
             )
        sys.exit(1)

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_file)
    sales_records = load_json_file(sales_record_file)

    if price_catalogue is None or sales_records is None:
        sys.exit(1)

    total_sales = compute_total_sales(price_catalogue, sales_records)

    elapsed_time = time.time() - start_time

    print("\nSales Results")
    print("-------------")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Execution Time: {elapsed_time:.6f} seconds")

    os.makedirs("results", exist_ok=True)
    result_path = os.path.join("results", "SalesResults.txt")
    with open(result_path, "w", encoding="utf-8") as result_file:
        result_file.write("Sales Results\n")
        result_file.write("-------------\n")
        result_file.write(f"Total Sales: ${total_sales:.2f}\n")
        result_file.write(f"Execution Time: {elapsed_time:.6f} seconds\n")


if __name__ == "__main__":
    main()
