import json
import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = float(amount)
        self.category = category.strip().capitalize()
        # Αν δεν δοθεί ημερομηνία, παίρνει τη σημερινή σε μορφή ΥΥΥΥ-ΜΜ-DD
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """Μετατρέπει το αντικείμενο σε λεξικό για αποθήκευση σε JSON"""
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Διαβάζει τα έξοδα από το αρχείο JSON (File I/O)"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Μετατροπή των raw dicts ξανά σε αντικείμενα Expense
                return [Expense(item["amount"], item["category"], item["date"]) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Αν το αρχείο δεν υπάρχει ή είναι άδειο, ξεκινάμε με άδεια λίστα

    def save_expenses(self):
        """Αποθηκεύει τα έξοδα στο αρχείο JSON"""
        with open(self.filename, "w", encoding="utf-8") as f:
            # Μετατρέπουμε τα αντικείμενα σε dicts για να γραφτούν στο JSON
            json.dump([e.to_dict() for e in self.expenses], f, indent=4, ensure_ascii=False)

    def add_expense(self, amount, category):
        """Προσθήκη νέου εξόδου"""
        new_expense = Expense(amount, category)
        self.expenses.append(new_expense)
        self.save_expenses()
        print(f"Successful entry {amount}€ in category '{new_expense.category}'!")

    def show_report(self):
        """Εμφανίζει το μηνιαίο report και σύνολα ανά κατηγορία"""
        if not self.expenses:
            print("There are no documented expenses.")
            return

        print("\nMONTHLY EXPENSE REPORT")
        total = 0
        category_totals = {}

        for e in self.expenses:
            total += e.amount
            category_totals[e.category] = category_totals.get(e.category, 0) + e.amount
            print(f"[{e.date}] {e.category}: {e.amount}€")

        print(f"TOTAL EXPENSES: {total:.2f}€")
        print("\nPer Category:")
        for cat, amt in category_totals.items():
            print(f"• {cat}: {amt:.2f}€")

def export_to_csv(self, csv_filename="expenses.csv"):
        """Exports expenses to a CSV file compatible with Excel"""
        if not self.expenses:
            print("Error: No expenses found to export.")
            return
        
        try:
            with open(csv_filename, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                # Write column headers
                writer.writerow(["Date", "Category", "Amount (€)"])
                
                # Write data rows
                for e in self.expenses:
                    writer.writerow([e.date, e.category, e.amount])
                    
            print(f"Success: Report successfully exported to '{csv_filename}'.")
        except Exception as e:
            print(f"Error occurred during export: {e}")

# --- INPUT VALIDATION & CLI LOOP ---
def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Options:")
        print("1. Add expense")
        print("2. View report")
        print("3. Export to CSV (Excel)")
        print("4. Exit")
        
        choice = input("Select action (1, 2 or 3): ").strip()
        
        if choice == "1":
            # Input Validation για το ποσό
            while True:
                amount_input = input("Input expense amount: ").strip()
                try:
                    amount = float(amount_input)
                    if amount <= 0:
                        print("Expense amount must be bigger than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid amount.")

            category = input("Please state the expense category: ").strip()
            if not category:
                category = "Misc" # Default τιμή αν το αφήσει κενό
                
            tracker.add_expense(amount, category)
            
        elif choice == "2":
            tracker.show_report()
        elif choice == "3":
            tracker.export_to_csv()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()