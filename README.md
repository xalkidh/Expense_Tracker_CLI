# CLI Expense Tracker

A lightweight, Object-Oriented Command-Line Interface (CLI) application built with Python to help users log, track, and manage their daily expenses. Data is persistently stored in JSON format, and reports can be exported directly to CSV for Excel integration.

## Features

* Persistent Storage: Expenses are saved in a structured JSON file, ensuring data survives application restarts.
* Robust Input Validation: Prevents crashes from invalid price inputs such as text instead of numbers or negative values.
* Automated Categorization: Dynamically groups costs and formats text fields for clean report generation.
* Data Export: Generate a Microsoft Excel compatible CSV report with proper encoding for special characters.

## Tech Stack and Concepts

* Language: Python 3
* Object-Oriented Programming: Utilizes structured Expense and ExpenseTracker classes to ensure code maintainability.
* File I/O: Handles raw data read and write streams using Python's built-in json and csv modules.
* Error Handling: Implements try-except blocks to smoothly catch file corruption and invalid user input.

## Installation and Setup

### Prerequisites

Make sure you have Python 3 installed on your machine.

### Instructions

1. Clone the repository:
   ```bash
   git clone [https://github.com/xalkidh/Expense_Tracker_CLI.git](https://github.com/xalkidh/Expense_Tracker_CLI.git)

2. Navigate to the project directory:
cd Expense_Tracker_CLI

3. Run the application:
python tracker.py

Note: On macOS or Linux systems, use python3 tracker.py instead.

### Usage
When you run the application, an interactive menu will guide you through the available options:
Expense Tracker Options:
1. Add expense
2. View report
3. Export to CSV (Excel)
4. Exit

Selecting 1 prompts for an amount and a category.
Selecting 2 displays a formatted summary breakdown per category.
Selecting 3 creates an expenses.csv file in the project directory.
Selecting 4 safely closes the program.

### License
This project is open-source and available under the MIT License.