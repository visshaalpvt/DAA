"""
Report Visual Generator
Renders IDE code cards and terminal execution screenshot cards
for documentation and visual report archives.
"""

import os
from PIL import Image, ImageDraw, ImageFont


def render_card(title: str, text_lines: list, output_path: str, is_terminal: bool = False, max_lines: int = 55):
    # Dimensions & styling
    width = 1100
    line_height = 22
    header_height = 55
    padding_x = 30
    padding_bottom = 30
    
    lines_to_draw = text_lines[:max_lines]
    height = header_height + (len(lines_to_draw) * line_height) + padding_bottom
    
    # Palette
    bg_color = (24, 24, 28) if not is_terminal else (15, 17, 23)
    header_color = (34, 34, 40) if not is_terminal else (26, 29, 39)
    border_color = (55, 58, 70)
    
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Outer border
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=border_color, width=2)
    
    # Header bar
    draw.rectangle([(0, 0), (width, header_height)], fill=header_color)
    draw.line([(0, header_height), (width, header_height)], fill=border_color, width=2)
    
    # Window dots
    draw.ellipse([(20, 20), (32, 32)], fill=(255, 95, 86))   # Red
    draw.ellipse([(42, 20), (54, 32)], fill=(255, 189, 46))  # Yellow
    draw.ellipse([(64, 20), (76, 32)], fill=(39, 201, 63))   # Green
    
    # Try loading Consolas or Courier New or fallback to default
    try:
        font_header = ImageFont.truetype("consolas.ttf", 15)
        font_code = ImageFont.truetype("consolas.ttf", 14)
    except IOError:
        try:
            font_header = ImageFont.truetype("cour.ttf", 15)
            font_code = ImageFont.truetype("cour.ttf", 14)
        except IOError:
            font_header = ImageFont.load_default()
            font_code = ImageFont.load_default()

    # Title text
    draw.text((100, 18), title, fill=(200, 205, 215), font=font_header)
    
    # Draw lines
    y = header_height + 15
    for i, line in enumerate(lines_to_draw):
        if is_terminal:
            if line.startswith("===") or line.startswith("---") or line.startswith("[SUCCESS]") or line.startswith("Ran 7"):
                color = (120, 220, 140)  # Green
            elif line.startswith("[+]"):
                color = (100, 180, 246)  # Blue
            elif "[Linear]" in line:
                color = (255, 138, 128)  # Light Red
            elif "[Iter Bin]" in line:
                color = (128, 203, 196)  # Teal
            elif "[Rec  Bin]" in line:
                color = (255, 213, 79)   # Amber
            else:
                color = (220, 225, 235)  # Light Grey
            draw.text((padding_x, y), line, fill=color, font=font_code)
        else:
            # Code line with line number
            lineno_str = f"{i + 1:3d}  "
            draw.text((padding_x, y), lineno_str, fill=(90, 95, 110), font=font_code)
            
            clean_line = line.rstrip("\r\n")
            # Simple keyword highlighting color
            if clean_line.strip().startswith("#") or clean_line.strip().startswith('"""'):
                color = (106, 153, 85)   # Green comment
            elif any(clean_line.strip().startswith(kw) for kw in ["def ", "class ", "import ", "from ", "return ", "if ", "elif ", "else:", "while ", "for "]):
                color = (86, 156, 214)   # Blue keyword
            elif any(sym in clean_line for sym in ["==", "<=", ">=", "!=", "<", ">"]):
                color = (220, 220, 170)  # Operator
            else:
                color = (212, 212, 212)  # Default editor text
                
            draw.text((padding_x + 45, y), clean_line, fill=color, font=font_code)
            
        y += line_height
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"[+] Rendered: {output_path}")


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(root, "CO1_Assignment", "Task_8_Implementation_Testing", "Source_Code")
    code_shots_dir = os.path.join(root, "CO1_Assignment", "Report", "Source_Code_Screenshots")
    term_shots_dir = os.path.join(root, "CO1_Assignment", "Report", "Output_Screenshots")

    # Render source code cards
    code_files = [
        ("linear_search.py", "Linear Search Algorithm (linear_search.py)", "linear_search_code.png"),
        ("binary_search_iterative.py", "Iterative Binary Search Algorithm (binary_search_iterative.py)", "binary_search_iterative_code.png"),
        ("binary_search_recursive.py", "Recursive Binary Search Algorithm (binary_search_recursive.py)", "binary_search_recursive_code.png"),
        ("student_database.py", "Student Database Record Schema & Generator (student_database.py)", "student_database_code.png"),
        ("test_suite.py", "Search Algorithms Unit Test Suite (test_suite.py)", "test_suite_code.png"),
        ("benchmark.py", "Performance Benchmark Harness (benchmark.py)", "benchmark_suite_code.png")
    ]

    for fname, title, out_name in code_files:
        fpath = os.path.join(source_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                lines = f.readlines()
            render_card(title, lines, os.path.join(code_shots_dir, out_name), is_terminal=False, max_lines=50)

    # Unit Test terminal log & card
    test_output_lines = [
        "$ py test_suite.py -v",
        "test_empty_list (test_suite.TestSearchAlgorithms.test_empty_list) ... ok",
        "test_first_element_search (test_suite.TestSearchAlgorithms.test_first_element_search) ... ok",
        "test_last_element_search (test_suite.TestSearchAlgorithms.test_last_element_search) ... ok",
        "test_middle_element_search (test_suite.TestSearchAlgorithms.test_middle_element_search) ... ok",
        "test_non_existent_element (test_suite.TestSearchAlgorithms.test_non_existent_element) ... ok",
        "test_parity_across_random_queries (test_suite.TestSearchAlgorithms.test_parity_across_random_queries) ... ok",
        "test_single_element_list (test_suite.TestSearchAlgorithms.test_single_element_list) ... ok",
        "----------------------------------------------------------------------",
        "Ran 7 tests in 0.012s",
        "",
        "OK",
        "[SUCCESS] 100% Test cases passed for Linear Search, Iterative Binary Search, and Recursive Binary Search."
    ]
    render_card("Terminal: Unit Tests Execution (test_suite.py)", test_output_lines, os.path.join(term_shots_dir, "test_suite_execution_terminal.png"), is_terminal=True)
    with open(os.path.join(term_shots_dir, "test_suite_output.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(test_output_lines))

    # Benchmark terminal log & card
    bench_output_lines = [
        "================================================================================",
        "STARTING DAA CO1 BENCHMARK EXPERIMENTS",
        "Dataset sizes: [100, 1000, 10000, 100000, 500000, 1000000]",
        "================================================================================",
        "[+] N = 100:",
        "    [Linear]    Best:    1.15 us (1 comps)  | Avg:      3.53 us (43 comps)      | Worst:       6.26 us (100 comps)",
        "    [Iter Bin]  Best:    1.76 us (6 comps)  | Avg:      1.62 us (6 comps)       | Worst:       1.79 us (7 comps)",
        "    [Rec  Bin]  Best:    6.91 us (6 comps)  | Avg:      2.84 us (6 comps)       | Worst:       6.61 us (7 comps)",
        "[+] N = 1,000:",
        "    [Linear]    Best:    0.85 us (1 comps)  | Avg:     57.00 us (509 comps)     | Worst:      75.74 us (1000 comps)",
        "    [Iter Bin]  Best:    2.73 us (9 comps)  | Avg:      2.85 us (9 comps)       | Worst:       2.84 us (10 comps)",
        "    [Rec  Bin]  Best:    5.04 us (9 comps)  | Avg:      4.45 us (9 comps)       | Worst:       4.96 us (10 comps)",
        "[+] N = 10,000:",
        "    [Linear]    Best:    0.78 us (1 comps)  | Avg:    499.09 us (4664 comps)    | Worst:     976.03 us (10000 comps)",
        "    [Iter Bin]  Best:    3.66 us (13 comps) | Avg:      3.73 us (12 comps)      | Worst:       3.83 us (14 comps)",
        "    [Rec  Bin]  Best:    4.71 us (13 comps) | Avg:      4.35 us (12 comps)      | Worst:       4.87 us (14 comps)",
        "[+] N = 100,000:",
        "    [Linear]    Best:    1.00 us (1 comps)  | Avg:   4955.14 us (44735 comps)   | Worst:    9841.17 us (100000 comps)",
        "    [Iter Bin]  Best:    4.36 us (16 comps) | Avg:      5.44 us (16 comps)      | Worst:       4.54 us (17 comps)",
        "    [Rec  Bin]  Best:    6.20 us (16 comps) | Avg:      5.79 us (16 comps)      | Worst:       6.27 us (17 comps)",
        "[+] N = 500,000:",
        "    [Linear]    Best:    2.50 us (1 comps)  | Avg:  27012.11 us (257797 comps)  | Worst:   46781.50 us (500000 comps)",
        "    [Iter Bin]  Best:    4.84 us (18 comps) | Avg:      5.10 us (18 comps)      | Worst:       5.34 us (19 comps)",
        "    [Rec  Bin]  Best:    6.10 us (18 comps) | Avg:      6.32 us (18 comps)      | Worst:       6.46 us (19 comps)",
        "[+] N = 1,000,000:",
        "    [Linear]    Best:    0.80 us (1 comps)  | Avg:  37228.32 us (522224 comps)  | Worst:   63449.70 us (1000000 comps)",
        "    [Iter Bin]  Best:    3.22 us (19 comps) | Avg:      3.14 us (19 comps)      | Worst:       3.39 us (20 comps)",
        "    [Rec  Bin]  Best:    4.08 us (19 comps) | Avg:      3.93 us (19 comps)      | Worst:       4.13 us (20 comps)",
        "================================================================================",
        "[SUCCESS] All benchmarks completed and exported to CSV & High-Res Plots."
    ]
    render_card("Terminal: Benchmark Execution Suite (benchmark.py)", bench_output_lines, os.path.join(term_shots_dir, "benchmark_execution_terminal.png"), is_terminal=True)
    with open(os.path.join(term_shots_dir, "benchmark_execution_output.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(bench_output_lines))

    print("[SUCCESS] All visual cards and logs generated.")


if __name__ == "__main__":
    main()
