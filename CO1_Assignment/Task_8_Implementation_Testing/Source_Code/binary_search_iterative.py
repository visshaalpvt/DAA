"""
Binary Search (Iterative) Implementation
Module: binary_search_iterative.py
Course: DAA - Course Outcome 1 (CO1)
"""

from typing import List, Tuple
from student_database import StudentRecord


def binary_search_iterative(arr: List[StudentRecord], target_reg_no: str) -> Tuple[int, int]:
    """
    Performs Iterative Binary Search on a sorted list of StudentRecord objects.
    
    Parameters:
        arr (List[StudentRecord]): Sorted collection of student records.
        target_reg_no (str): The target registration number to search for.
        
    Returns:
        Tuple[int, int]: (index of target if found, else -1, number of key comparisons made)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        # Avoid integer overflow (though Python handles arbitrarily large ints)
        mid = low + (high - low) // 2
        comparisons += 1
        
        mid_val = arr[mid].reg_no
        
        # 3-way decision comparison
        if mid_val == target_reg_no:
            return mid, comparisons
        elif mid_val < target_reg_no:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons


if __name__ == "__main__":
    from student_database import generate_student_database
    
    db = generate_student_database(15)
    query = db[7].reg_no
    idx, comps = binary_search_iterative(db, query)
    print(f"Iterative Binary Search for '{query}': Index={idx}, Comparisons={comps}")
    
    absent = "REG9999XXXX000"
    idx, comps = binary_search_iterative(db, absent)
    print(f"Iterative Binary Search for absent key '{absent}': Index={idx}, Comparisons={comps}")
