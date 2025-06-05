"""
Test cases for the sequence generator program.
This file tests all the functions to make sure they work correctly.
"""

# Import all the functions from our main program
from sequence_generator import (
    generate_arithmetic_sequence, arithmetic_sum,
    generate_geometric_sequence, geometric_sum, geometric_product
)

def test_arithmetic_normal_cases():
    """Test normal cases for arithmetic sequences."""
    print("Testing Arithmetic Sequences - Normal Cases:")
    
    # Test Case 1: Basic positive sequence
    result = generate_arithmetic_sequence(2, 3, 5)
    expected = [2, 5, 8, 11, 14]
    print(f"Test 1 - Basic sequence: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Test Case 2: Negative difference
    result = generate_arithmetic_sequence(10, -2, 4)
    expected = [10, 8, 6, 4]
    print(f"Test 2 - Negative diff: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Test Case 3: Starting with negative number
    result = generate_arithmetic_sequence(-5, 4, 3)
    expected = [-5, -1, 3]
    print(f"Test 3 - Negative start: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Test sum calculations
    sum_result = arithmetic_sum(2, 3, 5)
    expected_sum = 40  # 2 + 5 + 8 + 11 + 14 = 40
    print(f"Test 4 - Sum calculation: {sum_result} == {expected_sum} -> {'PASS' if sum_result == expected_sum else 'FAIL'}")

def test_arithmetic_edge_cases():
    """Test edge cases for arithmetic sequences."""
    print("\nTesting Arithmetic Sequences - Edge Cases:")
    
    # Edge Case 1: Zero terms
    result = generate_arithmetic_sequence(5, 2, 0)
    expected = []
    print(f"Test 1 - Zero terms: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Edge Case 2: Single term
    result = generate_arithmetic_sequence(7, 2, 1)
    expected = [7]
    print(f"Test 2 - Single term: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Edge Case 3: Zero difference
    result = generate_arithmetic_sequence(5, 0, 4)
    expected = [5, 5, 5, 5]
    print(f"Test 3 - Zero difference: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")

def test_geometric_normal_cases():
    """Test normal cases for geometric sequences."""
    print("\nTesting Geometric Sequences - Normal Cases:")
    
    # Test Case 1: Basic positive sequence
    result = generate_geometric_sequence(2, 3, 4)
    expected = [2, 6, 18, 54]
    print(f"Test 1 - Basic sequence: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Test Case 2: Fractional ratio
    result = generate_geometric_sequence(8, 0.5, 3)
    expected = [8, 4.0, 2.0]
    print(f"Test 2 - Fractional ratio: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Test Case 3: Negative ratio
    result = generate_geometric_sequence(3, -2, 4)
    expected = [3, -6, 12, -24]
    print(f"Test 3 - Negative ratio: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Test sum calculations
    sum_result = geometric_sum(2, 3, 4)
    expected_sum = 80  # 2 + 6 + 18 + 54 = 80
    print(f"Test 4 - Sum calculation: {sum_result} == {expected_sum} -> {'PASS' if sum_result == expected_sum else 'FAIL'}")
    
    # Test product calculation
    product_result = geometric_product(2, 2, 3)
    expected_product = 64  # 2 * 4 * 8 = 64
    print(f"Test 5 - Product calculation: {product_result} == {expected_product} -> {'PASS' if product_result == expected_product else 'FAIL'}")

def test_geometric_edge_cases():
    """Test edge cases for geometric sequences."""
    print("\nTesting Geometric Sequences - Edge Cases:")
    
    # Edge Case 1: Zero terms
    result = generate_geometric_sequence(5, 2, 0)
    expected = []
    print(f"Test 1 - Zero terms: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    
    # Edge Case 2: Ratio of 1
    result = generate_geometric_sequence(7, 1, 3)
    expected = [7, 7, 7]
    sum_result = geometric_sum(7, 1, 3)
    expected_sum = 21
    print(f"Test 2 - Ratio of 1: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")
    print(f"Test 2b - Sum with ratio 1: {sum_result} == {expected_sum} -> {'PASS' if sum_result == expected_sum else 'FAIL'}")
    
    # Edge Case 3: Zero first term
    result = generate_geometric_sequence(0, 5, 3)
    expected = [0, 0, 0]
    print(f"Test 3 - Zero first term: {result} == {expected} -> {'PASS' if result == expected else 'FAIL'}")

def run_manual_tests():
    """Run some manual demonstration tests."""
    print("\n" + "="*60)
    print("MANUAL DEMONSTRATION TESTS")
    print("="*60)
    
    print("\nExample 1: Arithmetic Sequence (3, 4, 5 terms)")
    seq = generate_arithmetic_sequence(3, 4, 5)
    sum_val = arithmetic_sum(3, 4, 5)
    print(f"Sequence: {seq}")
    print(f"Sum: {sum_val}")
    
    print("\nExample 2: Geometric Sequence (2, 2, 4 terms)")
    seq = generate_geometric_sequence(2, 2, 4)
    sum_val = geometric_sum(2, 2, 4)
    product_val = geometric_product(2, 2, 4)
    print(f"Sequence: {seq}")
    print(f"Sum: {sum_val}")
    print(f"Product: {product_val}")
    
    print("\nExample 3: Edge case - Single term arithmetic")
    seq = generate_arithmetic_sequence(10, 5, 1)
    sum_val = arithmetic_sum(10, 5, 1)
    print(f"Sequence: {seq}")
    print(f"Sum: {sum_val}")

def main():
    """Run all tests."""
    print("="*60)
    print("SEQUENCE GENERATOR TEST SUITE")
    print("="*60)
    
    # Run all test categories
    test_arithmetic_normal_cases()
    test_arithmetic_edge_cases()
    test_geometric_normal_cases()
    test_geometric_edge_cases()
    
    # Run manual demonstrations
    run_manual_tests()
    
    print("\n" + "="*60)
    print("TESTING COMPLETE!")
    print("Check the results above - all tests should show 'PASS'")
    print("If any show 'FAIL', there might be an issue with the code.")
    print("="*60)

if __name__ == "__main__":
    main()