"""
Linear Search (Sequential Search) Implementation
Module: linear_search.py
Course: DAA - Course Outcome 1 (CO1)
"""

from typing import List, Tuple, Optional
from student_database import StudentRecord


def linear_search(arr: List[StudentRecord], target_reg_no: str) -> Tuple[int, int]:
    """
    Performs Linear Search on a list of StudentRecord objects.
    
    Parameters:
        arr (List[StudentRecord]): Collection of student records.
        target_reg_no (str): The target registration number to search for.
        
    Returns:
        Tuple[int, int]: (index of target if found, else -1, number of key comparisons made)
    """
    comparisons = 0
    n = len(arr)
    
    for i in range(n):
        comparisons += 1
        # Basic Operation: Key comparison between query and record registration number
        if arr[i].reg_no == target_reg_no:
            return i, comparisons
            
    return -1, comparisons


if __name__ == "__main__":
    from student_database import generate_student_database
    
    db = generate_student_database(10)
    print("Database sample (first 3):")
    for r in db[:3]:
        print(f"  {r.reg_no} | {r.name} | {r.department}")
        
    query = db[2].reg_no
    idx, comps = linear_search(db, query)
    print(f"\nSearching for existing key '{query}': Index={idx}, Comparisons={comps}")
    
    absent = "REG9999XXXX000"
    idx, comps = linear_search(db, absent)
    print(f"Searching for absent key '{absent}': Index={idx}, Comparisons={comps}")
