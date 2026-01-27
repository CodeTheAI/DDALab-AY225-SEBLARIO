# Bubble Sort Application

A modern GUI application implementing the classic **Bubble Sort** algorithm with optimization for early termination when no swaps occur.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

## Features

- ✅ **Classic Bubble Sort** - Exchange sort algorithm implementation
- ✅ **Optimized Flag** - Early break when no swaps occur (array already sorted)
- ✅ **Modern Dark Theme GUI** - Clean, professional interface
- ✅ **File Loading** - Load numbers from `.txt` or `.csv` files
- ✅ **Execution Statistics** - Displays execution time, comparisons, and swaps
- ✅ **Flexible Input** - Accepts comma, space, or newline separated numbers

## Requirements

- **Python 3.7 or higher**
- **Tkinter** (included with standard Python installation)

## How to Run

### Option 1: Direct Execution

1. Open a terminal/command prompt
2. Navigate to the project directory:
   ```bash
   cd "DDALab-AY225-SEBLARIO/Prelim Lab Work 1"
   ```
3. Run the application:
   ```bash
   python Bubblesort.py
   ```

### Option 2: From File Explorer

- Double-click on `Bubblesort.py` (if Python is associated with `.py` files)

## Usage Guide

### Manual Input

1. Enter numbers in the input field, separated by:
   - Commas: `64, 34, 25, 12, 22`
   - Spaces: `64 34 25 12 22`
   - Newlines (one number per line)
   
2. Click **▶ Sort Array** to sort

### Loading from File

1. Click **📂 Load from File**
2. Select a `.txt` or `.csv` file containing numbers
3. Click **▶ Sort Array** to sort

### Sample Data

- Click **📊 Load Sample** to load demonstration data

## File Format for Loading

The application accepts files with numbers in various formats:

**Example `numbers.txt`:**
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

## Algorithm Details

### Bubble Sort with Optimization

```python
def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Optimization flag
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Exchange elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Early break if no swaps occurred
        if not swapped:
            break
```

### Time Complexity

| Case | Complexity |
|------|------------|
| Best Case (already sorted) | O(n) |
| Average Case | O(n²) |
| Worst Case (reverse sorted) | O(n²) |

### Space Complexity

- **O(1)** - In-place sorting algorithm

## Statistics Displayed

- **⏱️ Execution Time** - Time taken to sort (in milliseconds)
- **🔍 Comparisons** - Number of element comparisons made
- **🔄 Swaps** - Number of element exchanges performed

## Screenshots

The application features a modern dark theme with:
- Clean input/output sections
- Real-time statistics
- File loading capability
- Sample data for quick testing

## Troubleshooting

### "Python not found"

Make sure Python is installed and added to your system PATH:
```bash
python --version
```

### Tkinter not available

On some Linux systems, you may need to install Tkinter:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

## Author

**Prelim Lab Work 1** - Data Structures and Algorithms Laboratory

---

*Made with ❤️ using Python and Tkinter*
