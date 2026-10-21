"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    return credit_cost * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Total cost for one year: "))
    credits = int(input("Credits this semester: "))
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.

    while True:
        print("\nCost of College Menu")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class")
        print("Q. Quit")
        # Show your menu here.

        choice = input("Choose an option: ").upper()

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):,.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):,.2f}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(annual_cost):,.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):,.2f}")
        elif choice == "5":
            print(f"Cost per CS 1430 class: ${cost_per_class(annual_cost, credits):,.2f}")
        else:
            print("Invalid choice. Please choose 1-5 or Q.")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
