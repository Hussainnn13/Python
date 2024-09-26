def vendingshop():
    stock = {"lays": 5, "redbull": 3, "shawarma": 2}
    history = {"lays": 0, "redull": 0, "shawarma": 0}

    while True:
        print("\nItems available: ", stock)
        choice = input("Enter the item you want (lays,redbull,shawarma) or 'exit' to stop: ").lower()

        if choice == 'exit':
            popular_item = max(history, key=history.get)
            print(f"Thank you for using the vending shop! The item mostly bought is: {popular_item}")
            break
        elif choice in stock and stock[choice] > 0:
            stock[choice] -= 1
            history[choice] += 1
            print(f"Dispensing {choice}. Stock left: {stock[choice]}")
        else:
            print("Sorry, that item is not available at the moment.")

vendingshop()
