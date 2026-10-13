"""
Benchmarking and Experimental Performance Suite
Module: benchmark.py
Evaluates Linear Search, Iterative Binary Search, and Recursive Binary Search
across sizes: 100, 1,000, 10,000, 100,000, 500,000, 1,000,000.
Records execution time (microseconds), comparison counts, and generates plots.
"""

import sys
import os
import time
import csv
import random
import matplotlib.pyplot as plt
import numpy as np

# Increase recursion depth just in case (log2(1,000,000) is only 20, but good practice)
sys.setrecursionlimit(50000)

from student_database import generate_student_database, StudentRecord
from linear_search import linear_search
from binary_search_iterative import binary_search_iterative
from binary_search_recursive import binary_search_recursive


def measure_search(search_fn, arr, target, repeats=5):
    """
    Measures average execution time in microseconds and comparison count.
    """
    # Warmup
    search_fn(arr, target)
    
    times = []
    comps = 0
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        idx, comps = search_fn(arr, target)
        t1 = time.perf_counter_ns()
        times.append((t1 - t0) / 1000.0)  # Convert ns to microseconds (us)
        
    avg_time_us = sum(times) / len(times)
    return avg_time_us, comps


def run_all_benchmarks(sizes=None):
    if sizes is None:
        sizes = [100, 1000, 10000, 100000, 500000, 1000000]

    results = []
    print("=" * 80)
    print("STARTING DAA CO1 BENCHMARK EXPERIMENTS")
    print(f"Dataset sizes: {sizes}")
    print("=" * 80)

    rng = random.Random(42)

    for n in sizes:
        print(f"\n[+] Generating sorted student database for N = {n:,}...")
        t_gen_start = time.perf_counter()
        db = generate_student_database(n, seed=42)
        print(f"    Done in {time.perf_counter() - t_gen_start:.2f}s.")

        # Target definitions
        # 1. Best Case:
        # Linear best: first element (idx 0)
        # Binary best: middle element (idx n // 2)
        best_linear_target = db[0].reg_no
        best_binary_target = db[n // 2].reg_no

        # 2. Worst Case:
        # Absent key for all
        worst_target = "REG9999NONEXISTENT999999"

        # 3. Average Case:
        # Sample 20 random positions and average
        sample_indices = [rng.randint(0, n - 1) for _ in range(min(20, n))]
        
        # Adaptive repeats based on size
        lin_repeats = 10 if n <= 10000 else (3 if n <= 100000 else 1)
        bin_repeats = 50 if n <= 10000 else 20

        print(f"    Benchmarking N = {n:,}...")

        # --- Linear Search ---
        # Best
        lin_best_t, lin_best_c = measure_search(linear_search, db, best_linear_target, repeats=lin_repeats)
        # Worst
        lin_worst_t, lin_worst_c = measure_search(linear_search, db, worst_target, repeats=lin_repeats)
        # Average
        lin_avg_times = []
        lin_avg_comps = []
        for s_idx in sample_indices:
            t, c = measure_search(linear_search, db, db[s_idx].reg_no, repeats=lin_repeats)
            lin_avg_times.append(t)
            lin_avg_comps.append(c)
        lin_avg_t = sum(lin_avg_times) / len(lin_avg_times)
        lin_avg_c = int(sum(lin_avg_comps) / len(lin_avg_comps))

        # --- Iterative Binary Search ---
        # Best
        bit_best_t, bit_best_c = measure_search(binary_search_iterative, db, best_binary_target, repeats=bin_repeats)
        # Worst
        bit_worst_t, bit_worst_c = measure_search(binary_search_iterative, db, worst_target, repeats=bin_repeats)
        # Average
        bit_avg_times = []
        bit_avg_comps = []
        for s_idx in sample_indices:
            t, c = measure_search(binary_search_iterative, db, db[s_idx].reg_no, repeats=bin_repeats)
            bit_avg_times.append(t)
            bit_avg_comps.append(c)
        bit_avg_t = sum(bit_avg_times) / len(bit_avg_times)
        bit_avg_c = int(round(sum(bit_avg_comps) / len(bit_avg_comps)))

        # --- Recursive Binary Search ---
        # Best
        brc_best_t, brc_best_c = measure_search(binary_search_recursive, db, best_binary_target, repeats=bin_repeats)
        # Worst
        brc_worst_t, brc_worst_c = measure_search(binary_search_recursive, db, worst_target, repeats=bin_repeats)
        # Average
        brc_avg_times = []
        brc_avg_comps = []
        for s_idx in sample_indices:
            t, c = measure_search(binary_search_recursive, db, db[s_idx].reg_no, repeats=bin_repeats)
            brc_avg_times.append(t)
            brc_avg_comps.append(c)
        brc_avg_t = sum(brc_avg_times) / len(brc_avg_times)
        brc_avg_c = int(round(sum(brc_avg_comps) / len(brc_avg_comps)))

        print(f"      [Linear]    Best: {lin_best_t:7.2f} us ({lin_best_c} comps) | Avg: {lin_avg_t:9.2f} us ({lin_avg_c} comps) | Worst: {lin_worst_t:10.2f} us ({lin_worst_c} comps)")
        print(f"      [Iter Bin]  Best: {bit_best_t:7.2f} us ({bit_best_c} comps) | Avg: {bit_avg_t:9.2f} us ({bit_avg_c} comps) | Worst: {bit_worst_t:10.2f} us ({bit_worst_c} comps)")
        print(f"      [Rec  Bin]  Best: {brc_best_t:7.2f} us ({brc_best_c} comps) | Avg: {brc_avg_t:9.2f} us ({brc_avg_c} comps) | Worst: {brc_worst_t:10.2f} us ({brc_worst_c} comps)")

        results.append({
            "size": n,
            "lin_best_time_us": round(lin_best_t, 3),
            "lin_best_comps": lin_best_c,
            "lin_avg_time_us": round(lin_avg_t, 3),
            "lin_avg_comps": lin_avg_c,
            "lin_worst_time_us": round(lin_worst_t, 3),
            "lin_worst_comps": lin_worst_c,
            
            "bit_best_time_us": round(bit_best_t, 3),
            "bit_best_comps": bit_best_c,
            "bit_avg_time_us": round(bit_avg_t, 3),
            "bit_avg_comps": bit_avg_c,
            "bit_worst_time_us": round(bit_worst_t, 3),
            "bit_worst_comps": bit_worst_c,

            "brc_best_time_us": round(brc_best_t, 3),
            "brc_best_comps": brc_best_c,
            "brc_avg_time_us": round(brc_avg_t, 3),
            "brc_avg_comps": brc_avg_c,
            "brc_worst_time_us": round(brc_worst_t, 3),
            "brc_worst_comps": brc_worst_c,
        })

    return results


def save_results_to_csv(results, csv_paths):
    fieldnames = list(results[0].keys())
    for path in csv_paths:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in results:
                writer.writerow(row)
        print(f"[+] Saved CSV data to: {path}")


def plot_graphs(results, output_dirs):
    sizes = [r["size"] for r in results]
    
    # 1. Execution Time Comparison (Worst Case)
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(sizes, [r["lin_worst_time_us"] for r in results], 'ro-', label='Linear Search (Worst Case)', linewidth=2)
    plt.plot(sizes, [r["bit_worst_time_us"] for r in results], 'bs-', label='Binary Search Iterative (Worst Case)', linewidth=2)
    plt.plot(sizes, [r["brc_worst_time_us"] for r in results], 'g^--', label='Binary Search Recursive (Worst Case)', linewidth=2)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Dataset Size (N)', fontsize=12, fontweight='bold')
    plt.ylabel('Execution Time (Microseconds, log scale)', fontsize=12, fontweight='bold')
    plt.title('Execution Time vs Dataset Size (Worst Case - Log-Log Scale)', fontsize=14, fontweight='bold')
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()
    for d in output_dirs:
        os.makedirs(d, exist_ok=True)
        plt.savefig(os.path.join(d, 'execution_time_comparison.png'))
    plt.close()

    # 2. Number of Key Comparisons (Average Case & Worst Case)
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(sizes, [r["lin_worst_comps"] for r in results], 'r-o', label='Linear Search (Worst: N)', linewidth=2)
    plt.plot(sizes, [r["lin_avg_comps"] for r in results], 'm--x', label='Linear Search (Avg: N/2)', linewidth=2)
    plt.plot(sizes, [r["bit_worst_comps"] for r in results], 'b-s', label=r'Binary Search (Worst: $\lfloor \log_2 N \rfloor + 1$)', linewidth=2)
    plt.plot(sizes, [r["bit_avg_comps"] for r in results], 'c--d', label=r'Binary Search (Avg: $\approx \log_2 N - 1$)', linewidth=2)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Dataset Size (N)', fontsize=12, fontweight='bold')
    plt.ylabel('Key Comparisons Count (log scale)', fontsize=12, fontweight='bold')
    plt.title('Key Comparisons vs Dataset Size (Theoretical & Observed)', fontsize=14, fontweight='bold')
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()
    for d in output_dirs:
        plt.savefig(os.path.join(d, 'comparison_count_comparison.png'))
    plt.close()

    # 3. Iterative vs Recursive Binary Search (Average & Worst Time in Microseconds)
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(sizes, [r["bit_avg_time_us"] for r in results], 'b-s', label='Iterative Binary Search (Avg Time)', linewidth=2)
    plt.plot(sizes, [r["brc_avg_time_us"] for r in results], 'g-^', label='Recursive Binary Search (Avg Time)', linewidth=2)
    plt.plot(sizes, [r["bit_worst_time_us"] for r in results], 'b--s', label='Iterative Binary Search (Worst Time)', alpha=0.7)
    plt.plot(sizes, [r["brc_worst_time_us"] for r in results], 'g--^', label='Recursive Binary Search (Worst Time)', alpha=0.7)
    plt.xscale('log')
    plt.xlabel('Dataset Size (N)', fontsize=12, fontweight='bold')
    plt.ylabel('Execution Time (Microseconds)', fontsize=12, fontweight='bold')
    plt.title('Iterative vs Recursive Binary Search Overhead Analysis', fontsize=14, fontweight='bold')
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()
    for d in output_dirs:
        plt.savefig(os.path.join(d, 'binary_iterative_vs_recursive.png'))
    plt.close()

    # 4. Multi-Case Analysis Bar Chart for N = 100,000
    n100k = next(r for r in results if r["size"] == 100000)
    cases = ['Best Case', 'Average Case', 'Worst Case']
    lin_times = [n100k["lin_best_time_us"], n100k["lin_avg_time_us"], n100k["lin_worst_time_us"]]
    bit_times = [n100k["bit_best_time_us"], n100k["bit_avg_time_us"], n100k["bit_worst_time_us"]]
    brc_times = [n100k["brc_best_time_us"], n100k["brc_avg_time_us"], n100k["brc_worst_time_us"]]

    x = np.arange(len(cases))
    width = 0.25

    plt.figure(figsize=(10, 6), dpi=300)
    plt.bar(x - width, lin_times, width, label='Linear Search', color='#e74c3c')
    plt.bar(x, bit_times, width, label='Iterative Binary Search', color='#3498db')
    plt.bar(x + width, brc_times, width, label='Recursive Binary Search', color='#2ecc71')
    plt.yscale('log')
    plt.xlabel('Search Case Scenario', fontsize=12, fontweight='bold')
    plt.ylabel('Execution Time in Microseconds (log scale)', fontsize=12, fontweight='bold')
    plt.title('Performance Across Case Scenarios at N = 100,000 Records', fontsize=14, fontweight='bold')
    plt.xticks(x, cases, fontsize=11, fontweight='bold')
    plt.grid(True, which="both", axis="y", ls="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()
    for d in output_dirs:
        plt.savefig(os.path.join(d, 'cases_comparison_linear_vs_binary.png'))
    plt.close()

    # 5. Theoretical Curve Fitting / Ratio Verification
    plt.figure(figsize=(10, 6), dpi=300)
    lin_worst_times = [r["lin_worst_time_us"] for r in results]
    ratios_lin = [t / s for t, s in zip(lin_worst_times, sizes)]
    
    bit_worst_times = [r["bit_worst_time_us"] for r in results]
    ratios_bin = [t / np.log2(s) for t, s in zip(bit_worst_times, sizes)]

    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)
    color = 'tab:red'
    ax1.set_xlabel('Dataset Size (N)', fontsize=12, fontweight='bold')
    ax1.set_xscale('log')
    ax1.set_ylabel(r'Linear Search: $T(N) / N$ ($\mu s$ / record)', color=color, fontsize=12, fontweight='bold')
    ax1.plot(sizes, ratios_lin, 'ro-', linewidth=2, label=r'Linear Ratio: $T(N)/N$')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, which="both", ls="--", alpha=0.5)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel(r'Binary Search: $T(N) / \log_2(N)$ ($\mu s$ / step)', color=color, fontsize=12, fontweight='bold')
    ax2.plot(sizes, ratios_bin, 'bs--', linewidth=2, label=r'Binary Ratio: $T(N)/\log_2 N$')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Asymptotic Growth Rate Verification: Ratio Convergence Test', fontsize=14, fontweight='bold')
    fig.tight_layout()
    for d in output_dirs:
        plt.savefig(os.path.join(d, 'theory_vs_experiment_ratios.png'))
    plt.close()

    print("[+] All 5 performance plots successfully generated and saved.")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    task9_dir = os.path.join(base_dir, "Task_9_Experimental_Performance")
    report_graphs_dir = os.path.join(os.path.dirname(base_dir), "Report", "Tables_and_Graphs")
    
    csv_paths = [
        os.path.join(task9_dir, "benchmark_results.csv"),
        os.path.join(report_graphs_dir, "benchmark_results.csv")
    ]
    
    output_dirs = [task9_dir, report_graphs_dir]
    
    results = run_all_benchmarks()
    save_results_to_csv(results, csv_paths)
    plot_graphs(results, output_dirs)
    print("\n[SUCCESS] Experimental Benchmarking Completed Successfully!")
