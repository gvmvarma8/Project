import csv
import os
from datetime import datetime

PURCHASE_FILE = "purchases.csv"
SALES_FILE = "sales.csv"

# Ensure files exist with headers
def init_files():
    if not os.path.exists(PURCHASE_FILE):
        with open(PURCHASE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Bags", "PricePerBag"])
    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Bags", "PricePerBag"])


def get_current_stock():
    total_purchased = 0
    total_sold = 0

    with open(PURCHASE_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_purchased += int(row["Bags"])

    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_sold += int(row["Bags"])

    return total_purchased - total_sold


def add_purchase():
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    bags = int(input("Enter number of bags purchased: "))
    price = float(input("Enter purchase price per bag: "))
    with open(PURCHASE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, bags, price])
    print("✅ Purchase entry added.")


def add_sale():
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    bags = int(input("Enter number of bags sold: "))

    current_stock = get_current_stock()
    if bags > current_stock:
        print(f"❌ Not enough stock! You only have {current_stock} bags left.")
        return

    price = float(input("Enter selling price per bag: "))
    with open(SALES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, bags, price])
    print("✅ Sale entry added.")


def view_current_stock():
    total_purchased = 0
    total_sold = 0
    purchase_value = 0

    with open(PURCHASE_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_purchased += int(row["Bags"])
            purchase_value += int(row["Bags"]) * float(row["PricePerBag"])

    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_sold += int(row["Bags"])

    current_stock = total_purchased - total_sold
    avg_cost = (purchase_value / total_purchased) if total_purchased else 0
    stock_value = current_stock * avg_cost

    print(f"\n Current Stock: {current_stock} bags")
    print(f" Stock Value: ₹{stock_value:.2f}\n")


def view_profit_summary():
    total_cost = 0
    total_revenue = 0

    with open(PURCHASE_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_cost += int(row["Bags"]) * float(row["PricePerBag"])

    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_revenue += int(row["Bags"]) * float(row["PricePerBag"])

    profit = total_revenue - total_cost

    print("\n   Profit Summary:")
    print(f"   Total Revenue: ₹{total_revenue:.2f}")
    print(f"   Total Cost: ₹{total_cost:.2f}")
    print(f"   Profit: ₹{profit:.2f}\n")


def main():
    init_files()
    while True:
        print("\n Rice Shop CLI Tracker")
        print("1. Add Purchase Entry")
        print("2. Add Sale Entry")
        print("3. View Current Stock")
        print("4. View Profit Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_purchase()
        elif choice == "2":
            add_sale()
        elif choice == "3":
            view_current_stock()
        elif choice == "4":
            view_profit_summary()
        elif choice == "5":
            print(" Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    main()
