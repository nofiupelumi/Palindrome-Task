# Product data
products = [
    {"name": "Tea", "price": 2200, "stock": 5},
    {"name": "Milk", "price": 1800, "stock": 8},
    {"name": "Sugar", "price": 550, "stock": 5},
    {"name": "Bread", "price": 750, "stock": 8},
    {"name": "Detergent", "price": 850, "stock": 5},
    {"name": "Bathing Soap", "price": 750, "stock": 8},
    {"name": "Coca Cola", "price": 250, "stock": 5},
    {"name": "Body Spray", "price": 2250, "stock": 8},
    {"name": "Tooth Brush", "price": 250, "stock": 5},
    {"name": "Tooth Paste", "price": 750, "stock": 8},
]

# Default account balance (using a dictionary to store individual balances)
account_balances = {"default_user": 100}

# Main loop
while True:
    # Display available tasks
    print("\nAvailable Tasks:")
    print("1. See Available Products")
    print("2. Buy Products")
    print("3. Remove Items from Cart")
    print("4. Sort Products")
    print("5. Review Purchased Products")
    print("6. View All Available Products")
    print("7. Quit")

    # User input to choose a task
    chosen_task = input("Enter the number of the task you want to perform: ")

    # Task 1: See Available Products
    if chosen_task == "1":
        print("\nAvailable Products:")
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product['name']} - ${product['price']} (Stock: {product['stock']})")

    # Task 2: Buy Products
    elif chosen_task == "2":
        username = input("Enter your name as a password to log in: ")
        if username not in account_balances:
            account_balances[username] = account_balances.get("default_user", 100)

        shopping_cart = []
        total_cost = 0

        while True:
            num_products = int(input("How many products do you want to buy? "))
            for _ in range(num_products):
                choice = int(input("Enter the product number: "))
                if 1 <= choice <= len(products):
                    product = products[choice - 1]
                    if product["stock"] > 0:
                        if username == "default_user" and shopping_cart == []:
                            product["price"] *= 0.9
                        shopping_cart.append(product)
                        total_cost += product["price"]
                        product["stock"] -= 1
                    else:
                        print("Sorry, this product is out of stock.")
                else:
                    print("Invalid product number.")

            print("Your Shopping Cart:")
            for item in shopping_cart:
                print(f"{item['name']} - ${item['price']}")
            print(f"Total Cost: ${total_cost}")

            if total_cost > account_balances[username]:
                print("Insufficient account balance.")
                break
            else:
                account_balances[username] -= total_cost
                print(f"Remaining Account Balance for {username}: ${account_balances[username]}")
                break

    # Task 3: Remove Items from Cart
    elif chosen_task == "3":
        remove_option = input("Do you want to remove items from your cart? (yes/no): ").lower()
        if remove_option == "yes":
            product_name_to_remove = input("Enter the name of the product to remove: ")
            for item in shopping_cart:
                if item["name"].lower() == product_name_to_remove.lower():
                    total_cost -= item["price"]
                    item["stock"] += 1
                    shopping_cart.remove(item)
                    print(f"{product_name_to_remove} removed from your cart.")
                    break
            else:
                print(f"{product_name_to_remove} not found in your cart.")

    # Task 5: Review Purchased Products
    elif chosen_task == "5":
        print("\nReview Purchased Products:")
        for item in shopping_cart:
            review = input(f"Enter a review for {item['name']}: ")
            item["review"] = review
            print(f"Review for {item['name']} added.")
        print("Reviews added.")

    # Task 6: View All Available Products
    elif chosen_task == "6":
        print("\nAll Available Products:")
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product['name']} - ${product['price']} (Stock: {product['stock']})")

    # Task 7: Quit
    elif chosen_task == "7":
        print("Exiting the program. Thank you!")
        break

    # Invalid task
    else:
        print("Invalid task number. Please choose a valid task.")
