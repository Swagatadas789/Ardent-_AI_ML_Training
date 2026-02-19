import statistics

def get_number(prompt):
    """Safely get a number from user input with type casting."""
    while True:
        try:
            value = input(prompt).strip()
            # Try int first, then float
            try:
                return int(value)
            except ValueError:
                return float(value)
        except ValueError:
            print("  ❌ Invalid input. Please enter a valid number.")

def get_numbers_list():
    """Get a list of numbers from the user."""
    while True:
        try:
            raw = input("Enter numbers separated by spaces: ").strip()
            nums = [float(x) if '.' in x else int(x) for x in raw.split()]
            if not nums:
                print("  ❌ Please enter at least one number.")
                continue
            return nums
        except ValueError:
            print("  ❌ Invalid input. Please enter valid numbers separated by spaces.")

def basic_calculator():
    """Perform basic arithmetic: +, -, *, /."""
    print("\n--- Basic Calculator ---")
    a = get_number("Enter first number : ")
    print("Operations: + | - | * | /")
    op = input("Enter operator     : ").strip()
    b = get_number("Enter second number: ")

    if op == '+':
        result = a + b
        symbol = '+'
    elif op == '-':
        result = a - b
        symbol = '-'
    elif op == '*':
        result = a * b
        symbol = '×'
    elif op == '/':
        if b == 0:
            print("  ❌ Error: Division by zero is not allowed.")
            return
        result = a / b
        symbol = '÷'
    else:
        print("  ❌ Unknown operator. Use +, -, *, /")
        return

    print(f"\n  ✅ {a} {symbol} {b} = {result}")

def stats_calculator():
    """Calculate mean, median, and mode for a list of numbers."""
    print("\n--- Statistics Calculator ---")
    nums = get_numbers_list()

    mean   = statistics.mean(nums)
    median = statistics.median(nums)

    try:
        mode = statistics.mode(nums)
        mode_str = str(mode)
    except statistics.StatisticsError:
        # Multiple modes exist — show all
        mode_list = statistics.multimode(nums)
        mode_str = f"{mode_list} (multiple modes)"

    print(f"\n  Numbers : {nums}")
    print(f"  Mean    : {mean}")
    print(f"  Median  : {median}")
    print(f"  Mode    : {mode_str}")

def main():
    print("=" * 40)
    print("        Python Calculator")
    print("=" * 40)

    menu = {
        '1': ('Basic Arithmetic (+, -, *, /)', basic_calculator),
        '2': ('Statistics (Mean, Median, Mode)', stats_calculator),
        '3': ('Exit', None),
    }

    while True:
        print("\nMenu:")
        for key, (label, _) in menu.items():
            print(f"  [{key}] {label}")

        choice = input("\nYour choice: ").strip()

        if choice == '3':
            print("\nGoodbye! 👋")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("  ❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
