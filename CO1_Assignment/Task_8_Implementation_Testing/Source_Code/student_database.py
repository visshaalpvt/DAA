"""
Student Database Module
Defines the StudentRecord schema and utilities to generate synthetic datasets
of student registration numbers and associated academic records.
"""

import random
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class StudentRecord:
    reg_no: str
    name: str
    department: str
    cgpa: float
    year_of_study: int

    def __lt__(self, other: 'StudentRecord') -> bool:
        return self.reg_no < other.reg_no

    def __eq__(self, other: object) -> bool:
        if isinstance(other, StudentRecord):
            return self.reg_no == other.reg_no
        if isinstance(other, str):
            return self.reg_no == other
        return False


DEPARTMENTS = [
    "Computer Science and Engineering",
    "Information Technology",
    "Artificial Intelligence and Data Science",
    "Electronics and Communication Engineering",
    "Electrical and Electronics Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Biomedical Engineering"
]

FIRST_NAMES = [
    "Aarav", "Aditi", "Akash", "Ananya", "Bhuvan", "Deepak", "Divya", "Ganesh",
    "Hari", "Ishaan", "Kavya", "Keerthi", "Manoj", "Meera", "Naveen", "Nisha",
    "Pradeep", "Priya", "Rahul", "Rithika", "Rohit", "Sai", "Sanjay", "Sneha",
    "Suresh", "Swetha", "Varun", "Vignesh", "Vikram", "Visshaal"
]

LAST_NAMES = [
    "Balaji", "Chandran", "Iyer", "Kumar", "Murugan", "Natarajan", "Pillai",
    "Rajan", "Rao", "Reddy", "Sankaran", "Sharma", "Subramanian", "Sundaram", "Varma"
]


def format_reg_no(index: int, total_digits: int = 7, year: int = 2024, dept_code: str = "BCSE") -> str:
    """
    Generates a standardized student registration number.
    Format: REG<YEAR><DEPT><SEQ_NUMBER_PADDED>
    Example: REG2024BCSE000042
    """
    return f"REG{year}{dept_code}{index:0{total_digits}d}"


def generate_student_database(size: int, seed: int = 42) -> List[StudentRecord]:
    """
    Generates a deterministic synthetic student database of given size.
    The records are sorted by registration number.
    """
    rng = random.Random(seed)
    records: List[StudentRecord] = []
    
    dept_codes = ["BCSE", "BIT", "BAIDS", "BECE", "BEEE", "BMECH"]
    total_digits = max(6, len(str(size)) + 1)
    
    for i in range(1, size + 1):
        reg = format_reg_no(i, total_digits=total_digits)
        first_name = rng.choice(FIRST_NAMES)
        last_name = rng.choice(LAST_NAMES)
        name = f"{first_name} {last_name}"
        dept = rng.choice(DEPARTMENTS)
        cgpa = round(rng.uniform(6.5, 9.9), 2)
        year_of_study = rng.randint(1, 4)
        
        records.append(StudentRecord(
            reg_no=reg,
            name=name,
            department=dept,
            cgpa=cgpa,
            year_of_study=year_of_study
        ))
        
    return records


def get_test_targets(records: List[StudentRecord], size: int) -> Tuple[str, str, str]:
    """
    Returns targets for:
    1. Best Case: Target at beginning (index 0) or middle
    2. Average Case: Target at random existing position
    3. Worst Case: Non-existent registration number
    """
    best_target = records[0].reg_no
    mid_target = records[len(records) // 2].reg_no
    worst_target = "REG9999NONEXIST999999"
    return best_target, mid_target, worst_target
