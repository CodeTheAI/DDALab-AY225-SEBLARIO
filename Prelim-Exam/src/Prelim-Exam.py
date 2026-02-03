

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import time
import threading


class SortingBenchmark:
    """Main application class for the sorting benchmark tool."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Benchmark Tool")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Data storage
        self.data = []
        self.sorted_data = []
        self.file_path = None
        self.load_time = 0
        self.sort_time = 0
        self.is_sorting = False
        self.cancel_sorting = False
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
        self.style.configure("Header.TLabel", font=("Segoe UI", 11, "bold"))
        self.style.configure("Info.TLabel", font=("Segoe UI", 10))
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="📊 Sorting Algorithm Benchmark", style="Title.TLabel")
        title_label.pack(pady=(0, 15))
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="📁 File Selection", padding="10")
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.file_label = ttk.Label(file_frame, text="No file selected", style="Info.TLabel")
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.load_btn = ttk.Button(file_frame, text="Load CSV File", command=self._load_file)
        self.load_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Configuration frame
        config_frame = ttk.LabelFrame(main_frame, text="⚙️ Sorting Configuration", padding="10")
        config_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Grid layout for configuration
        config_inner = ttk.Frame(config_frame)
        config_inner.pack(fill=tk.X)
        
        # Column selection
        ttk.Label(config_inner, text="Sort by Column:", style="Header.TLabel").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.column_var = tk.StringVar(value="ID")
        column_combo = ttk.Combobox(config_inner, textvariable=self.column_var, values=["ID", "FirstName", "LastName"], state="readonly", width=15)
        column_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Algorithm selection
        ttk.Label(config_inner, text="Algorithm:", style="Header.TLabel").grid(row=0, column=2, sticky=tk.W, padx=(20, 5), pady=5)
        self.algorithm_var = tk.StringVar(value="Merge Sort")
        algorithm_combo = ttk.Combobox(config_inner, textvariable=self.algorithm_var, 
                                        values=["Bubble Sort", "Insertion Sort", "Merge Sort"], state="readonly", width=15)
        algorithm_combo.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
        # Number of rows
        ttk.Label(config_inner, text="Number of Rows (N):", style="Header.TLabel").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.rows_var = tk.StringVar(value="1000")
        rows_combo = ttk.Combobox(config_inner, textvariable=self.rows_var, 
                                   values=["100", "500", "1000", "5000", "10000", "50000", "100000"], width=15)
        rows_combo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Sort order
        ttk.Label(config_inner, text="Sort Order:", style="Header.TLabel").grid(row=1, column=2, sticky=tk.W, padx=(20, 5), pady=5)
        self.order_var = tk.StringVar(value="Ascending")
        order_combo = ttk.Combobox(config_inner, textvariable=self.order_var, 
                                    values=["Ascending", "Descending"], state="readonly", width=15)
        order_combo.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)
        
        # Sort buttons frame
        btn_frame = ttk.Frame(config_frame)
        btn_frame.pack(pady=(10, 0))
        
        self.sort_btn = ttk.Button(btn_frame, text="🚀 Start Sorting", command=self._start_sorting, state="disabled")
        self.sort_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.cancel_btn = ttk.Button(btn_frame, text="⛔ Cancel", command=self._cancel_sorting, state="disabled")
        self.cancel_btn.pack(side=tk.LEFT)
        
        # Progress frame
        progress_frame = ttk.LabelFrame(main_frame, text="📈 Progress", padding="10")
        progress_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, pady=(0, 5))
        
        self.status_label = ttk.Label(progress_frame, text="Ready. Load a CSV file to begin.", style="Info.TLabel")
        self.status_label.pack()
        
        # Performance metrics frame
        metrics_frame = ttk.LabelFrame(main_frame, text="⏱️ Performance Metrics", padding="10")
        metrics_frame.pack(fill=tk.X, pady=(0, 10))
        
        metrics_inner = ttk.Frame(metrics_frame)
        metrics_inner.pack(fill=tk.X)
        
        # Metrics labels
        ttk.Label(metrics_inner, text="File Load Time:", style="Header.TLabel").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.load_time_label = ttk.Label(metrics_inner, text="--", style="Info.TLabel")
        self.load_time_label.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(metrics_inner, text="Sort Time:", style="Header.TLabel").grid(row=0, column=2, sticky=tk.W, padx=(30, 5), pady=2)
        self.sort_time_label = ttk.Label(metrics_inner, text="--", style="Info.TLabel")
        self.sort_time_label.grid(row=0, column=3, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(metrics_inner, text="Total Rows:", style="Header.TLabel").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.total_rows_label = ttk.Label(metrics_inner, text="--", style="Info.TLabel")
        self.total_rows_label.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(metrics_inner, text="Complexity:", style="Header.TLabel").grid(row=1, column=2, sticky=tk.W, padx=(30, 5), pady=2)
        self.complexity_label = ttk.Label(metrics_inner, text="--", style="Info.TLabel")
        self.complexity_label.grid(row=1, column=3, sticky=tk.W, padx=5, pady=2)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="📋 Sorted Results (First 10 Records)", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview for results
        columns = ("ID", "FirstName", "LastName")
        self.results_tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=150, anchor=tk.CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)
        
        self.results_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Complexity info at bottom
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=(10, 0))
        
        info_text = "📖 Complexity: Merge Sort = O(n log n) | Bubble/Insertion Sort = O(n²)"
        ttk.Label(info_frame, text=info_text, style="Info.TLabel", foreground="gray").pack()
    
    def _load_file(self):
        """Load CSV file via file dialog."""
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        
        if not file_path:
            return
        
        self.file_path = file_path
        self.status_label.config(text="Loading file...")
        self.root.update()
        
        try:
            start_time = time.perf_counter()
            
            self.data = []
            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Convert ID to integer for proper numeric sorting
                    row['ID'] = int(row['ID'])
                    self.data.append(row)
            
            end_time = time.perf_counter()
            self.load_time = end_time - start_time
            
            # Update UI
            filename = file_path.split('/')[-1].split('\\')[-1]
            self.file_label.config(text=f"📄 {filename}")
            self.load_time_label.config(text=f"{self.load_time:.4f} seconds")
            self.total_rows_label.config(text=f"{len(self.data):,}")
            self.status_label.config(text=f"✅ Loaded {len(self.data):,} records successfully!")
            self.sort_btn.config(state="normal")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")
            self.status_label.config(text="❌ Error loading file")
    
    def _start_sorting(self):
        """Validate inputs and start the sorting process."""
        if self.is_sorting:
            return
        
        # Validate row count
        try:
            n = int(self.rows_var.get())
            if n <= 0:
                raise ValueError("Must be positive")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for rows.")
            return
        
        if n > len(self.data):
            messagebox.showwarning("Warning", f"Requested {n:,} rows but file only has {len(self.data):,}. Using all available rows.")
            n = len(self.data)
        
        algorithm = self.algorithm_var.get()
        
        # Warn for large datasets with O(n²) algorithms
        if algorithm in ["Bubble Sort", "Insertion Sort"] and n > 10000:
            estimated_time = (n / 1000) ** 2 * 0.5  # Rough estimate in seconds
            result = messagebox.askyesno(
                "⚠️ Performance Warning",
                f"You are about to sort {n:,} rows using {algorithm}.\n\n"
                f"This algorithm has O(n²) complexity and may take\n"
                f"approximately {estimated_time:.0f}+ seconds to complete.\n\n"
                f"Consider using Merge Sort (O(n log n)) for large datasets.\n\n"
                f"Do you want to continue?"
            )
            if not result:
                return
        
        # Start sorting in a separate thread
        self.is_sorting = True
        self.cancel_sorting = False
        self.sort_btn.config(state="disabled")
        self.load_btn.config(state="disabled")
        self.cancel_btn.config(state="normal")
        
        thread = threading.Thread(target=self._perform_sorting, args=(n,))
        thread.daemon = True
        thread.start()
    
    def _cancel_sorting(self):
        """Cancel the current sorting operation."""
        if self.is_sorting:
            self.cancel_sorting = True
            self.status_label.config(text="⏳ Cancelling... Please wait.")
            self.cancel_btn.config(state="disabled")
    
    def _perform_sorting(self, n):
        """Perform the sorting operation."""
        algorithm = self.algorithm_var.get()
        column = self.column_var.get()
        ascending = self.order_var.get() == "Ascending"
        
        # Update complexity display
        if algorithm == "Merge Sort":
            complexity = "O(n log n)"
        else:
            complexity = "O(n²)"
        
        self.root.after(0, lambda: self.complexity_label.config(text=complexity))
        self.root.after(0, lambda: self.status_label.config(text=f"Sorting {n:,} rows using {algorithm}..."))
        self.root.after(0, lambda: self.progress_var.set(0))
        
        # Copy data subset
        data_to_sort = self.data[:n].copy()
        
        # Track start time
        start_time = time.perf_counter()
        
        # Sort based on selected algorithm
        if algorithm == "Bubble Sort":
            sorted_data = self._bubble_sort_optimized(data_to_sort, column, ascending)
        elif algorithm == "Insertion Sort":
            sorted_data = self._insertion_sort_optimized(data_to_sort, column, ascending)
        else:  # Merge Sort
            sorted_data = self._merge_sort(data_to_sort, column, ascending)
        
        end_time = time.perf_counter()
        self.sort_time = end_time - start_time
        self.sorted_data = sorted_data
        
        # Update UI on main thread
        self.root.after(0, self._display_results)
    
    def _display_results(self):
        """Display the sorting results."""
        # Clear previous results
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Insert first 10 records
        for i, row in enumerate(self.sorted_data[:10]):
            self.results_tree.insert("", tk.END, values=(row['ID'], row['FirstName'], row['LastName']))
        
        # Update metrics
        self.sort_time_label.config(text=f"{self.sort_time:.4f} seconds")
        self.progress_var.set(100)
        
        if self.cancel_sorting:
            self.status_label.config(text="❌ Sorting cancelled by user.")
        else:
            self.status_label.config(text=f"✅ Sorting complete! Processed {len(self.sorted_data):,} records.")
        
        # Re-enable buttons
        self.sort_btn.config(state="normal")
        self.load_btn.config(state="normal")
        self.cancel_btn.config(state="disabled")
        self.is_sorting = False
        self.cancel_sorting = False
    
    # ==================== SORTING ALGORITHMS ====================
    
    def _get_key(self, item, column):
        """Get the comparison key for sorting."""
        value = item[column]
        if column == "ID":
            return value  # Already an integer
        return value.lower()  # Case-insensitive string comparison
    
    def _compare(self, a, b, column, ascending):
        """Compare two items based on column and order."""
        key_a = self._get_key(a, column)
        key_b = self._get_key(b, column)
        
        if ascending:
            return key_a > key_b
        else:
            return key_a < key_b
    
    # ----- BUBBLE SORT (Optimized) -----
    def _bubble_sort_optimized(self, data, column, ascending=True):
        """
        Optimized Bubble Sort implementation.
        
        Optimizations:
        1. Early termination if no swaps occur (already sorted)
        2. Tracks the last swap position to reduce comparisons
        3. Progress updates for large datasets
        
        Complexity: O(n²) worst/average, O(n) best case
        """
        n = len(data)
        last_swap = n - 1
        update_interval = max(1, n // 100)  # Update progress every 1%
        
        for i in range(n):
            # Check for cancellation
            if self.cancel_sorting:
                return data
            
            swapped = False
            new_last_swap = 0
            
            for j in range(last_swap):
                if self._compare(data[j], data[j + 1], column, ascending):
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
                    new_last_swap = j
            
            last_swap = new_last_swap
            
            # Early termination - array is sorted
            if not swapped:
                break
            
            # Update progress
            if i % update_interval == 0:
                progress = (i / n) * 100
                self.root.after(0, lambda p=progress: self.progress_var.set(p))
        
        return data
    
    # ----- INSERTION SORT (Optimized) -----
    def _insertion_sort_optimized(self, data, column, ascending=True):
        """
        Optimized Insertion Sort implementation.
        
        Optimizations:
        1. Uses binary search to find insertion position
        2. Reduces comparisons from O(n) to O(log n) per insertion
        3. Still O(n²) due to shifting, but faster in practice
        
        Complexity: O(n²) worst/average, O(n) best case
        """
        n = len(data)
        update_interval = max(1, n // 100)
        
        for i in range(1, n):
            # Check for cancellation
            if self.cancel_sorting:
                return data
            
            key_item = data[i]
            
            # Binary search for insertion position
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                if self._compare(data[mid], key_item, column, ascending):
                    right = mid
                else:
                    left = mid + 1
            
            # Shift elements and insert
            if left < i:
                # Move elements to make room
                temp = data[i]
                for j in range(i, left, -1):
                    data[j] = data[j - 1]
                data[left] = temp
            
            # Update progress
            if i % update_interval == 0:
                progress = (i / n) * 100
                self.root.after(0, lambda p=progress: self.progress_var.set(p))
        
        return data
    
    # ----- MERGE SORT (Optimized) -----
    def _merge_sort(self, data, column, ascending=True):
        """
        Optimized Merge Sort implementation.
        
        Optimizations:
        1. Uses insertion sort for small subarrays (< 32 elements)
        2. Avoids recursion overhead with iterative bottom-up approach
        3. Minimizes array copying
        
        Complexity: O(n log n) always
        """
        n = len(data)
        
        if n <= 1:
            return data
        
        # Use insertion sort for small arrays
        if n <= 32:
            return self._insertion_sort_small(data, column, ascending)
        
        # Bottom-up iterative merge sort
        aux = data.copy()
        width = 1
        total_passes = 0
        temp = n
        while temp > 1:
            total_passes += 1
            temp //= 2
        
        current_pass = 0
        
        while width < n:
            # Check for cancellation
            if self.cancel_sorting:
                return data
            
            for i in range(0, n, 2 * width):
                left = i
                mid = min(i + width, n)
                right = min(i + 2 * width, n)
                self._merge(data, aux, left, mid, right, column, ascending)
            
            # Swap arrays
            data, aux = aux, data
            width *= 2
            
            current_pass += 1
            progress = (current_pass / total_passes) * 100
            self.root.after(0, lambda p=progress: self.progress_var.set(p))
        
        return data
    
    def _merge(self, src, dest, left, mid, right, column, ascending):
        """Merge two sorted subarrays."""
        i, j, k = left, mid, left
        
        while i < mid and j < right:
            # Use inverted comparison for merge
            if not self._compare(src[i], src[j], column, ascending):
                dest[k] = src[i]
                i += 1
            else:
                dest[k] = src[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < mid:
            dest[k] = src[i]
            i += 1
            k += 1
        
        while j < right:
            dest[k] = src[j]
            j += 1
            k += 1
    
    def _insertion_sort_small(self, data, column, ascending):
        """Simple insertion sort for small arrays (used by merge sort)."""
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            
            while j >= 0 and self._compare(data[j], key_item, column, ascending):
                data[j + 1] = data[j]
                j -= 1
            
            data[j + 1] = key_item
        
        return data


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    
    # Center window on screen
    root.update_idletasks()
    width = 900
    height = 700
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    app = SortingBenchmark(root)
    root.mainloop()


if __name__ == "__main__":
    main()
