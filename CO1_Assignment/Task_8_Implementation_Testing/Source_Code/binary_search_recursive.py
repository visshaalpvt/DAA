"""
Binary Search (Recursive) Implementation
Module: binary_search_recursive.py
Course: DAA - Course Outcome 1 (CO1)
"""

from typing import List, Tuple
from student_database import StudentRecord


def _binary_search_recursive_helper(
    arr: List[StudentRecord], 
    target_reg_no: str, 
    low: int, 
    high: int, 
    comparisons: int
) -> Tuple[int, int]:
    """
    Internal recursive helper for Binary Search.
    
    Recurrence Relation:
        T(n) = T(n/2) + c   for n > 1
        T(0) = c_0, T(1) = c_1
    """
    # Base Case: Empty search interval
    if low > high:
        return -1, comparisons

    mid = low + (high - low) // 2
    comparisons += 1
    mid_val = arr[mid].reg_no

    if mid_val == target_reg_no:
        return mid, comparisons
    elif mid_val < target_reg_no:
        # Search in the right sub-array: T(n/2)
        return _binary_search_recursive_helper(arr, target_reg_no, mid + 1, high, comparisons)
    else:
        # Search in the left sub-array: T(n/2)
        return _binary_search_recursive_helper(arr, target_reg_no, low, mid - 1, comparisons)


def binary_search_recursive(arr: List[StudentRecord], target_reg_no: str) -> Tuple[int, int]:
    """
    Wrapper function for Recursive Binary Search.
    
    Parameters:
        arr (List[StudentRecord]): Sorted collection of student records.
        target_reg_no (str): The target registration number to search for.
        
    Returns:
        Tuple[int, int]: (index of target if found, else -1, number of key comparisons made)
    """
    return _binary_search_recursive_helper(arr, target_reg_no, 0, len(arr) - 1, 0)


if __name__ == "__main__":
    from student_database import generate_student_database
    
    db = generate_student_database(15)
    query = db[7].reg_no
    idx, comps = binary_search_recursive(db, query)
    print(f"Recursive Binary Search for '{query}': Index={idx}, Comparisons={comps}")
    
    absent = "REG9999XXXX000"
    idx, comps = binary_search_recursive(db, absent)
    print(f"Recursive Binary Search for absent key '{absent}': Index={idx}, Comparisons={comps}")
