# Modern Sorting Application

A modern GUI application for comparing and visualizing sorting algorithms.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

## Features

- ✅ **Multiple Sorting Algorithms** - Bubble Sort, Insertion Sort, Merge Sort
- ✅ **Modern Dark Theme GUI** - Clean, professional interface
- ✅ **File Loading** - Load data from `.txt`, `.xls`, `.xlsx` files
- ✅ **Dynamic Dataset Generation** - Specify dataset size and generate random data
- ✅ **Progress Tracking** - Real-time progress bar during sorting
- ✅ **Algorithm Comparison** - Compare all algorithms on the same dataset
- ✅ **Time Complexity Display** - Shows Big O notation for each algorithm
- ✅ **Execution Statistics** - Displays sorting time and verification status
- ✅ **Sorting Verification** - Validates that the output is correctly sorted

## Requirements

- **Python 3.7 or higher**
- **Tkinter** (included with standard Python installation)
- **Optional:** `openpyxl` for `.xlsx` file support
- **Optional:** `xlrd` for `.xls` file support

## Installation

1. Clone or download this repository

2. Install optional dependencies (for Excel file support):
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install openpyxl xlrd
   ```

## How to Run

### Option 1: Direct Execution

```bash
cd "DDALab-AY225-SEBLARIO/Prelim Lab Work 2"
python sorting_app.py
```

### Option 2: From File Explorer

- Double-click on `sorting_app.py` (if Python is associated with `.py` files)

## Usage Guide

### Loading Data from File

1. Click **📂 Browse** to select a file
2. Supported formats: `.txt`, `.xls`, `.xlsx`
3. Files should contain numbers (comma, space, or newline separated)

### Generating Random Data

1. Enter the desired dataset size in the **Dataset Size** field
2. Click **🎲 Generate** to create random data
3. The data will appear in the Original Data panel

### Sorting Data

1. Select an algorithm from the **Algorithm** dropdown:
   - Bubble Sort
   - Insertion Sort
   - Merge Sort
2. Click **▶ Run** to start sorting
3. Watch the progress bar during sorting
4. Results appear with verification status

### Comparing Algorithms

1. Load or generate data
2. Click **📊 Compare All** to run all algorithms
3. View the comparison results showing:
   - Execution time for each algorithm
   - Ranking (fastest to slowest)
   - Speed comparison

## Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

## File Format Examples

**Text file (numbers.txt):**
```
64, 34, 25, 12, 22, 11, 90
```

**Or one per line:**
```
64
34
25
12
22
```

**Or space-separated:**
```
64 34 25 12 22 11 90
```

## Verification

The application automatically verifies that the sorted output is correct by checking that each element is less than or equal to the next element. The verification status is displayed:
- ✅ **Verified** - Array is correctly sorted
- ❌ **Verification Failed** - Sorting error detected

## Troubleshooting

### "Python not found"

Make sure Python is installed and added to your system PATH:
```bash
python --version
```

### Excel files not loading

Install the required dependencies:
```bash
pip install openpyxl xlrd
```

### Tkinter not available (Linux)

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

## Author

**Prelim Lab Work 2** - Data Structures and Algorithms Laboratory

---

*Made with ❤️ using Python and Tkinter*
