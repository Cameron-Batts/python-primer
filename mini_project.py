def calculate_tip(bill, percent):
    return bill * (percent / 100)

def main():
    keep_going = True

    while keep_going:
        try:
            bill = float(input("Enter your bill amount: "))
            service = input("Was the service good or bad? ").lower()

            if service == "good":
                percent = 20
            elif service == "bad":
                percent = 10
            else:
                percent = 15

            tip = calculate_tip(bill, percent)
            total = bill + tip

            print(f"Tip: ${tip:.2f}")
            print(f"Total: ${total:.2f}")

        except ValueError:
            print("That wasn't a valid number, try again.")

        again = input("Calculate another bill? (yes/no): ").lower()
        if again != "yes":
            keep_going = False

if __name__ == "__main__":
    main()