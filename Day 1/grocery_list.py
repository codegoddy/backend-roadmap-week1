print("Welcome to the Grocery List Manager 🛒")

grocery_list = []

while True:
    print("\nWhat would you like to do?")
    print("[1] Add Item")
    print("[2] View List")
    print("[3] Remove Item")
    print("[4] Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item_name = input("Item name: ")

        try:
            quantity = int(input("Quantity: "))
            price = float(input("price per unit: "))
        except ValueError:
            print("Please enter valid numbers for quantity and price")
            continue
        total_price = quantity * price
        grocery_list.append({
            "name": item_name,
            "quantity": quantity,
            "price": price,
            "total": total_price
        })
        print(f"{item_name} added to your list")

    elif choice == "2":
        if not grocery_list:
            print("Your grocery list is empty")
            continue
        print("\n Grocery List:")
        grand_total = 0

        for item in grocery_list:
            name = item["name"]
            qty = item["quantity"]
            price = item["price"]
            total = item["total"]

            print(f"- {name} - {qty} @ {price} - Ksh.{total}")
            grand_total += total

            print(f'\n Total cost: Ksh.{grand_total}')
    elif choice == "3":
        item_to_remove = input("Enter the name of the Item to remove: ")

        found = False
        for item in grocery_list:
            if item["name"].lower() == item_to_remove.lower():
                grocery_list.remove(item)
                print(f"Removed {item_to_remove} from your list.")
                found =True
                break
        if not found:
            print(f"Could not find '{item_to_remove}' in your list")

    elif choice == "4":
        print("Goodbye, and happy shopping!")
        break
    else:
        print("invalid option. Try again.")