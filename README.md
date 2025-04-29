# 📈 Stockbroker Trade Book CLI Application

A simple yet robust command-line tool to manage and record trades from investors. The application updates a trade book based on new incoming trade actions, maintaining persistence through CSV files.

<br /><br />

## 🚀 Features

- ✅ Interactive and batch mode
- ✅ Automatically updates existing trade volumes or creates new entries
- ✅ Validates stock codes from `stockcode.csv`
- ✅ Stores trade books in `orders.csv`
- ✅ Detailed input validation

<br /><br />

## 📂 Project Structure
stockbroker/<br />
├── orders.csv # Trade book records<br />
├── orders.txt # Sample orders records<br />
├── stockbroker.bat # Windows startup script<br />
├── stockbroker.log # (Additional) Log file<br />
├── stockbroker.py # Main application script<br />
├── stockcode.csv # List of valid stock codes<br />
└── README.md<br />

<br /><br />

# Project documentation

## ⚙️ How to Run

### 1. 🖥️ Interactive Mode

```bash
$ ./stockbroker.sh

$ buy AAPL 1000.00 100
Trade book added.

$ sell AAPL 1000.10 10
Trade book added.

buy,AAPL,1000.00,100
sell,AAPL,1000.10,10

$ exit
```

### 2. 📄 Batch Mode (File Input)
Provide a text file containing one trade per line:
buy AAPL 1000.00 100
sell AAPL 1000.10 10
buy GOOGL 1200.00 50

Then run:
```bash
$ ./stockbroker.sh orders.txt
```
<br /><br />

# Author
[Dimon Kee](https://github.com/DimonKeeYongKit)
