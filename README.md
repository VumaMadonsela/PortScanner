# Python Port Scanner

A simple Python-based port scanner that allows users to scan a specific IP address and port range to identify open TCP ports. This project is ideal for beginners who want to learn the basics of socket programming and network security.
TO install and use just download the files and Run on Visual Studio, be sure that you have all The Python Files installed onto your Development environment.
---

## Features

- Scan any IPv4 address for open ports
- Customizable port range (e.g., 20–80, 1–65535)
- Fast response with socket timeouts
- Input validation and error handling
- Clean and user-friendly command-line interface

---

##  Tools & Technologies Used

- **Python 3**
- **Visual Studio** (with Python Development Workload)
- **Socket Module** – for network connections
- **sys Module** – for exiting the program safely
- **try/except Blocks** – for error and exception handling

---

##  How It Works

1. The user inputs:
   - An IP address to scan
   - A start and end port range

2. The script:
   - Loops through each port in the range
   - Uses `socket.connect_ex()` to check if the port is open
   - Displays open ports at the end

3. Handles:
   - Invalid IP addresses
   - Port range errors
   - Keyboard interrupts (Ctrl + C)

---

##  How to Run the Project

### Requirements:
- Python 3.x installed
- Visual Studio with Python support (or any Python IDE)

### Steps:
1. Clone or download the project
2. Open the `.py` file in Visual Studio
3. Run the script
4. Follow on-screen prompts to scan an IP

---

##  Example Output

