"""
Unit Test Suite for Search Algorithms
Module: test_suite.py
Tests Linear Search, Iterative Binary Search, and Recursive Binary Search
across normal and edge cases to ensure 100% correctness and parity.
"""

import unittest
from student_database import generate_student_database, StudentRecord
from linear_search import linear_search
from binary_search_iterative import binary_search_iterative
from binary_search_recursive import binary_search_recursive


class TestSearchAlgorithms(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create small, medium, and large sorted datasets
        cls.db_small = generate_student_database(15, seed=101)
        cls.db_large = generate_student_database(1000, seed=202)

    def test_first_element_search(self):
        """Test finding the first element (Best case for Linear Search)."""
        target = self.db_small[0].reg_no
        
        idx_lin, c_lin = linear_search(self.db_small, target)
        idx_bit, c_bit = binary_search_iterative(self.db_small, target)
        idx_brc, c_brc = binary_search_recursive(self.db_small, target)
        
        self.assertEqual(idx_lin, 0)
        self.assertEqual(idx_bit, 0)
        self.assertEqual(idx_brc, 0)
        self.assertEqual(c_lin, 1)  # Linear search checks exactly 1 element

    def test_last_element_search(self):
        """Test finding the last element (Worst case for Linear Search)."""
        n = len(self.db_small)
        target = self.db_small[n - 1].reg_no
        
        idx_lin, c_lin = linear_search(self.db_small, target)
        idx_bit, c_bit = binary_search_iterative(self.db_small, target)
        idx_brc, c_brc = binary_search_recursive(self.db_small, target)
        
        self.assertEqual(idx_lin, n - 1)
        self.assertEqual(idx_bit, n - 1)
        self.assertEqual(idx_brc, n - 1)
        self.assertEqual(c_lin, n)  # Linear search checks all n elements

    def test_middle_element_search(self):
        """Test finding the middle element (Best case for Binary Search)."""
        mid_idx = len(self.db_small) // 2
        target = self.db_small[mid_idx].reg_no
        
        idx_lin, c_lin = linear_search(self.db_small, target)
        idx_bit, c_bit = binary_search_iterative(self.db_small, target)
        idx_brc, c_brc = binary_search_recursive(self.db_small, target)
        
        self.assertEqual(idx_lin, mid_idx)
        self.assertEqual(idx_bit, mid_idx)
        self.assertEqual(idx_brc, mid_idx)
        self.assertEqual(c_bit, 1)  # Binary search checks exactly 1 element at mid
        self.assertEqual(c_brc, 1)

    def test_non_existent_element(self):
        """Test searching for an element not present in the database."""
        absent_target = "REG9999NONEXISTENT"
        n = len(self.db_small)
        
        idx_lin, c_lin = linear_search(self.db_small, absent_target)
        idx_bit, c_bit = binary_search_iterative(self.db_small, absent_target)
        idx_brc, c_brc = binary_search_recursive(self.db_small, absent_target)
        
        self.assertEqual(idx_lin, -1)
        self.assertEqual(idx_bit, -1)
        self.assertEqual(idx_brc, -1)
        self.assertEqual(c_lin, n)

    def test_single_element_list(self):
        """Edge case: Single-element list."""
        single_db = generate_student_database(1, seed=42)
        target = single_db[0].reg_no
        
        idx_lin, _ = linear_search(single_db, target)
        idx_bit, _ = binary_search_iterative(single_db, target)
        idx_brc, _ = binary_search_recursive(single_db, target)
        
        self.assertEqual(idx_lin, 0)
        self.assertEqual(idx_bit, 0)
        self.assertEqual(idx_brc, 0)
        
        # Absent in single element
        idx_lin, _ = linear_search(single_db, "REG0000")
        idx_bit, _ = binary_search_iterative(single_db, "REG0000")
        idx_brc, _ = binary_search_recursive(single_db, "REG0000")
        self.assertEqual(idx_lin, -1)
        self.assertEqual(idx_bit, -1)
        self.assertEqual(idx_brc, -1)

    def test_empty_list(self):
        """Edge case: Empty list."""
        empty_db = []
        idx_lin, c_lin = linear_search(empty_db, "REG2024")
        idx_bit, c_bit = binary_search_iterative(empty_db, "REG2024")
        idx_brc, c_brc = binary_search_recursive(empty_db, "REG2024")
        
        self.assertEqual(idx_lin, -1)
        self.assertEqual(idx_bit, -1)
        self.assertEqual(idx_brc, -1)
        self.assertEqual(c_lin, 0)
        self.assertEqual(c_bit, 0)
        self.assertEqual(c_brc, 0)

    def test_parity_across_random_queries(self):
        """Verify that all three algorithms return identical indices across 50 random queries."""
        import random
        rng = random.Random(42)
        indices = [rng.randint(0, len(self.db_large) - 1) for _ in range(50)]
        
        for idx in indices:
            target = self.db_large[idx].reg_no
            idx_lin, _ = linear_search(self.db_large, target)
            idx_bit, _ = binary_search_iterative(self.db_large, target)
            idx_brc, _ = binary_search_recursive(self.db_large, target)
            self.assertEqual(idx, idx_lin)
            self.assertEqual(idx, idx_bit)
            self.assertEqual(idx, idx_brc)


if __name__ == "__main__":
    unittest.main()
