"""
Author  : Dimon Kee Yong Kit
Date    : April 29, 2025
Purpose : Take-Home Assessment for Senior Back-end Software Engineer Position
"""

import sys
import os
import csv
import logging
from typing import List, Set, Tuple

Trade = Tuple[str, str, float, int]
Orders = List[Trade]

# Configure logging
logging.basicConfig(
    filename='stockbroker.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

STOCK_FILE = "stockcode.csv"
ORDER_FILE = "orders.csv"

def load_valid_stocks() -> Set[str]:
    if not os.path.exists(STOCK_FILE):
        return set()
    with open(STOCK_FILE, "r") as f:
        return set(line.strip().upper() for line in f if line.strip())

def load_orders() -> Orders:
    orders = []
    if os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, "r") as f:
            for line in csv.reader(f):
                if len(line) == 4:
                    action, stock, price, volume = line
                    orders.append([action, stock, float(price), int(volume)])
    return orders

def save_orders(orders: Orders) -> None:
    with open(ORDER_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for order in orders:
            writer.writerow([order[0], order[1], f"{order[2]:.2f}", order[3]])

def is_valid_trade(
    action: str,
    stock: str,
    price: float,
    volume: int,
    valid_stocks: Set[str]
) -> bool:
    if action not in ["buy", "sell"]:
        print("Invalid trade action.")
        logging.warning(f"Rejected trade due to invalid action: {action}")
        return False
    if stock not in valid_stocks:
        print("Invalid stock code.")
        logging.warning(f"Rejected trade due to invalid stock code: {stock}")
        return False
    if len(stock) != 4 or not stock.isupper():
        print("Stock code must be 4 uppercase letters.")
        logging.warning(f"Rejected trade due to invalid stock code format: {stock}")
        return False
    if not (price >= 0.50 and round(price, 2) == price):
        print("Invalid trade price.")
        logging.warning(f"Rejected trade due to invalid price: {price}")
        return False
    if not (1 <= volume <= 1_000_000):
        print("Invalid trade volume.")
        logging.warning(f"Rejected trade due to invalid volume: {volume}")
        return False
    return True

def process_trade(
    trade: Trade,
    orders: Orders
) -> None:
    action, stock, price, volume = trade
    for order in orders:
        if order[0] == action and order[1] == stock and order[2] == price:
            order[3] += volume
            print("Trade volume adjusted.")
            logging.info(f"Updated {action.upper()} trade: {stock} at {price:.2f} for {volume}")
            return
    orders.append([action, stock, price, volume])
    print("Trade book added.")
    logging.info(f"Added new {action.upper()} trade: {stock} at {price:.2f} for {volume}")

def handle_input_line(
    line: str,
    valid_stocks: Set[str],
    orders: Orders
) -> None:
    try:
        parts = line.strip().split()
        if len(parts) != 4:
            print("Invalid command format.")
            return
        action, stock, price_str, volume_str = parts
        price = float(price_str)
        volume = int(volume_str)

        if is_valid_trade(action, stock, price, volume, valid_stocks):
            process_trade([action, stock, price, volume], orders)
    except Exception as e:
        print(f"Error processing trade: {e}")

def interactive_mode(
    valid_stocks: Set[str],
    orders: Orders
) -> None:
    while True:
        line = input("$ ").strip()
        if line.lower() == "exit":
            break
        handle_input_line(line, valid_stocks, orders)
    save_orders(orders)

def file_mode(
    file_path: str,
    valid_stocks: Set[str],
    orders: Orders
) -> None:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    with open(file_path, "r") as f:
        for line in f:
            handle_input_line(line, valid_stocks, orders)
    save_orders(orders)

def main():
    valid_stocks = load_valid_stocks()
    orders = load_orders()
    if len(sys.argv) == 1:
        interactive_mode(valid_stocks, orders)
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1], valid_stocks, orders)
    else:
        print("Usage: ./stockbroker.sh [orders.txt]")

if __name__ == "__main__":
    main()
