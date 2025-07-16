from datetime import datetime

class Invoice:
    def __init__(self, name, service, amount, is_done=False):
        self.name = name
        self.service = service
        self.amount = amount
        self.is_done = is_done

    def mark_done(self):
        self.is_done = True

    def display(self):
        checkbox = "✓" if self.is_done else "✗"
        print(f"{checkbox} {self.name} - {self.service} - KSH.{self.amount}")

    def get_line(self):
        checkbox = "✓" if self.is_done else "✗"
        return f"{checkbox},{self.name},{self.service},{self.amount}"


class InvoiceManager:
    def __init__(self):
        self.invoices = []

    def add_invoice(self):
        name = input("Client Name: ")
        service = input("Type of Service: ")
        try:
            amount = float(input("Amount (KSH): "))
        except ValueError:
            print("⚠️ Please enter a valid amount.")
            return

        invoice = Invoice(name, service, amount)
        self.invoices.append(invoice)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("invoice.txt", "a") as file:
            file.write(f"[{timestamp}] {invoice.get_line()}\n")

        print(f"✅ Invoice for {name} added successfully!")

    def view_invoice(self):
        print("\n📄 Your Invoices:\n------------------")
        try:
            with open("invoice.txt", "r") as file:
                invoices = file.readlines()
                if not invoices:
                    print("No invoices yet.")
                    return
                for i, line in enumerate(invoices, 1):
                    print(f"{i}. {line.strip()}")
        except FileNotFoundError:
            print("⚠️ No invoice file found yet.")


# CLI loop
invoices = InvoiceManager()

while True:
    print("\n📋 Welcome to your Invoice Manager App")
    print("[1] Add Invoice")
    print("[2] View Invoices")
    print("[3] Mark Invoice as Paid (coming soon)")
    print("[4] Summary (coming soon)")
    print("[5] Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        invoices.add_invoice()
    elif choice == "2":
        invoices.view_invoice()
    elif choice == "3":
        print("🚧 Marking invoices is under construction.")
    elif choice == "4":
        print("📊 Summary is under construction.")
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option. Please try again.")
