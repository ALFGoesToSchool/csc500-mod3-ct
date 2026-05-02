# CSC500 Module 3 Critical Thinking Assignment - Part 1
# Author: Andrew Friedrich
# Description: Calculate the total amount of a restaurant meal,
#              including an 18% tip and 7% sales tax.

def main():
    # Prompt the user for the charge for the food
    food_charge = float(input("Enter the charge for the food: $"))

    # Calculate tip (18%) and tax (7%) based on the food charge
    tip = food_charge * 0.18
    tax = food_charge * 0.07

    # Calculate the total price
    total = food_charge + tip + tax

    # Display each amount and the total
    print("\n----- Meal Total -----")
    print(f"Food charge: ${food_charge:.2f}")
    print(f"Tip (18%):   ${tip:.2f}")
    print(f"Tax (7%):    ${tax:.2f}")
    print(f"Total:       ${total:.2f}")


if __name__ == "__main__":
    main()
