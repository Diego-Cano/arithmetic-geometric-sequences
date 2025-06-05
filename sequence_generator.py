"""
Arithmetic and Geometric Sequence Generator
A simple program to generate sequences and calculate their properties.
"""

def generate_arithmetic_sequence(first_term, common_diff, num_terms):
    """
    Generate an arithmetic sequence.
    In an arithmetic sequence, we add the same number each time.
    Example: 2, 5, 8, 11, 14 (adding 3 each time)
    """
    if num_terms <= 0:
        return []
    
    sequence = []
    current_term = first_term
    
    for i in range(num_terms):
        sequence.append(current_term)
        current_term += common_diff
    
    return sequence

def arithmetic_sum(first_term, common_diff, num_terms):
    """
    Calculate the sum of an arithmetic sequence.
    Formula: Sum = n/2 * (2a + (n-1)d)
    where n = number of terms, a = first term, d = common difference
    """
    if num_terms <= 0:
        return 0
    
    return (num_terms / 2) * (2 * first_term + (num_terms - 1) * common_diff)

def generate_geometric_sequence(first_term, common_ratio, num_terms):
    """
    Generate a geometric sequence.
    In a geometric sequence, we multiply by the same number each time.
    Example: 2, 6, 18, 54 (multiplying by 3 each time)
    """
    if num_terms <= 0:
        return []
    
    sequence = []
    current_term = first_term
    
    for i in range(num_terms):
        sequence.append(current_term)
        current_term *= common_ratio
    
    return sequence

def geometric_sum(first_term, common_ratio, num_terms):
    """
    Calculate the sum of a geometric sequence.
    Formula: Sum = a * (1 - r^n) / (1 - r) if r ≠ 1
             Sum = n * a if r = 1
    """
    if num_terms <= 0:
        return 0
    
    if common_ratio == 1:
        return num_terms * first_term
    else:
        return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)

def geometric_product(first_term, common_ratio, num_terms):
    """
    Calculate the product of a geometric sequence.
    This can get very large, so I limit it to small sequences.
    """
    if num_terms <= 0:
        return 1
    
    product = 1
    current_term = first_term
    
    for i in range(num_terms):
        product *= current_term
        current_term *= common_ratio
    
    return product

def get_user_input(prompt, input_type="float"):
    """Get and validate user input."""
    while True:
        try:
            user_input = input(prompt)
            if input_type == "int":
                value = int(user_input)
                if value <= 0:
                    print("Please enter a positive number.")
                    continue
                return value
            else:  # float
                return float(user_input)
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("    SEQUENCE GENERATOR")
    print("="*50)
    print("1. Generate Arithmetic Sequence")
    print("2. Generate Geometric Sequence")
    print("3. Exit")
    print("="*50)

def handle_arithmetic():
    """Handle arithmetic sequence generation."""
    print("\n--- ARITHMETIC SEQUENCE ---")
    print("An arithmetic sequence adds the same value each time.")
    print("Example: 2, 5, 8, 11, 14 (adding 3 each time)\n")
    
    first_term = get_user_input("Enter the first term: ")
    common_diff = get_user_input("Enter the common difference: ")
    num_terms = get_user_input("Enter number of terms: ", "int")
    
    # Generate sequence and calculate sum
    sequence = generate_arithmetic_sequence(first_term, common_diff, num_terms)
    total_sum = arithmetic_sum(first_term, common_diff, num_terms)
    
    # Display results
    print(f"\nResults:")
    print(f"First term: {first_term}")
    print(f"Common difference: {common_diff}")
    print(f"Number of terms: {num_terms}")
    print(f"Sequence: {sequence}")
    print(f"Sum: {total_sum}")

def handle_geometric():
    """Handle geometric sequence generation."""
    print("\n--- GEOMETRIC SEQUENCE ---")
    print("A geometric sequence multiplies by the same value each time.")
    print("Example: 2, 6, 18, 54 (multiplying by 3 each time)\n")
    
    first_term = get_user_input("Enter the first term: ")
    common_ratio = get_user_input("Enter the common ratio: ")
    num_terms = get_user_input("Enter number of terms: ", "int")
    
    # Generate sequence and calculate sum/product
    sequence = generate_geometric_sequence(first_term, common_ratio, num_terms)
    total_sum = geometric_sum(first_term, common_ratio, num_terms)
    
    # Only show product for reasonable-sized sequences
    show_product = num_terms <= 8 and all(abs(x) < 100 for x in sequence)
    if show_product:
        product = geometric_product(first_term, common_ratio, num_terms)
    
    # Display results
    print(f"\nResults:")
    print(f"First term: {first_term}")
    print(f"Common ratio: {common_ratio}")
    print(f"Number of terms: {num_terms}")
    print(f"Sequence: {sequence}")
    print(f"Sum: {total_sum}")
    
    if show_product:
        print(f"Product: {product}")
    else:
        print("Product: (too large to display)")

def main():
    """Main program loop."""
    print("Welcome to the Sequence Generator!")
    print("This program creates arithmetic and geometric sequences.")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            handle_arithmetic()
        elif choice == '2':
            handle_geometric()
        elif choice == '3':
            print("\nThanks for using the Sequence Generator!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()