# Prelim Exam - Sorting Algorithm Benchmark Tool

A comprehensive console-based benchmarking tool that compares the performance of different sorting algorithms (Bubble Sort, Insertion Sort, and Merge Sort) on CSV data.

## 📁 Project Structure

```
Prelim Exam/
├── README.md           # This file
├── Prelim-Exam.py      # Main entry point (launcher)
├── data/
│   └── generated_data.csv  # Dataset (100,000 rows)
└── src/
    ├── generate_data.py      # CSV data generator
    ├── sorting_algorithms.py # Sorting algorithm implementations
    └── benchmark_app.py      # Main benchmark application
```

## 🚀 Getting Started

### 1. Generate the Dataset

First, generate the CSV data file:

```bash
cd src
python generate_data.py
```

This creates `data/generated_data.csv` with 100,000 rows containing:
- **ID**: Random integers (1-100,000)
- **FirstName**: Random first names
- **LastName**: Random last names

### 2. Run the Benchmark Tool

You can run the benchmark tool in two ways:

**Interactive Mode (Recommended):**
```bash
python Prelim-Exam.py
# or
cd src
python benchmark_app.py
```

**Full Benchmark Suite:**
```bash
cd src
python benchmark_app.py --full
```

## 📊 Features

### Sorting Algorithms (Implemented from Scratch)
- **Bubble Sort** - O(n²) time complexity
- **Insertion Sort** - O(n²) time complexity  
- **Merge Sort** - O(n log n) time complexity

### Capabilities
- ✅ Load and parse CSV data
- ✅ Sort by any column: ID (Integer), FirstName (String), LastName (String)
- ✅ Specify number of rows to sort (N = 1,000 / 10,000 / 100,000)
- ✅ Track file loading time vs. sorting time separately
- ✅ Progress bar for long-running operations
- ✅ Warning messages for O(n²) algorithms on large datasets
- ✅ Display first 10 sorted records for verification
- ✅ Formatted benchmark results table

## 📈 Benchmark Results Table

| Algorithm       | N = 1,000    | N = 10,000   | N = 100,000      |
|-----------------|--------------|--------------|------------------|
| Bubble Sort     | *TBD*        | *TBD*        | *Skipped (slow)* |
| Insertion Sort  | *TBD*        | *TBD*        | *Skipped (slow)* |
| Merge Sort      | *TBD*        | *TBD*        | *TBD*            |

> **Note:** Run the benchmark on your machine and fill in the actual times.
> O(n²) algorithms are skipped for N=100,000 as they would take 10+ minutes.

### Expected Performance Comparison

Based on algorithm complexity:

| N (rows)  | Bubble/Insertion O(n²) | Merge Sort O(n log n) |
|-----------|------------------------|----------------------|
| 1,000     | ~100ms                 | ~1ms                 |
| 10,000    | ~10 seconds            | ~10ms                |
| 100,000   | ~15-30 minutes         | ~100ms               |

## 🎓 Theoretical Context

This benchmark demonstrates the practical difference between algorithm complexities:

- **O(n²)** (Bubble Sort, Insertion Sort): Time grows quadratically
  - 10x more data = 100x more time
  - Suitable for small datasets only

- **O(n log n)** (Merge Sort): Time grows nearly linearly
  - 10x more data ≈ 13x more time
  - Standard for modern computing

## 🛠️ Usage Examples

### Interactive Mode Options

1. **Number of Rows**: Enter 1000, 10000, or 100000
2. **Column Selection**:
   - `1` - Sort by ID (Integer comparison)
   - `2` - Sort by FirstName (String comparison)
   - `3` - Sort by LastName (String comparison)
3. **Algorithm Selection**:
   - `1` - Bubble Sort only
   - `2` - Insertion Sort only
   - `3` - Merge Sort only
   - `4` - All algorithms

### Sample Output

```
============================================================
               BENCHMARK RESULTS
============================================================
  Dataset Size: 10,000 rows
  Sort Column:  ID

  Algorithm            |            Time | Status
  --------------------+-----------------+------------
  Bubble Sort          |         12.34 s | ✓ Complete
  Insertion Sort       |          8.92 s | ✓ Complete
  Merge Sort           |         15.6 ms | ✓ Complete
```

## ⚠️ Important Notes

1. **Large Dataset Warning**: Sorting 100,000 rows with O(n²) algorithms will take a very long time (potentially 15-30+ minutes).

2. **Progress Tracking**: The tool shows progress bars during sorting operations.

3. **Cancellation**: Press `Ctrl+C` to cancel a long-running sort operation.

4. **No Built-in Functions**: All sorting algorithms are implemented from scratch without using Python's built-in `sort()` or `sorted()` functions.

## 📝 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)
