"""
Bubble Sort Application with Modern GUI
Features:
- Classic bubble sort with optimization (early break if no swaps)
- File loading capability
- Displays sorted array and execution time
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import re
import threading


class BubbleSortApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bubble Sort Visualizer")
        self.root.geometry("700x600")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(True, True)
        
        # Configure styles
        self.setup_styles()
        
        # Create main container
        self.main_frame = ttk.Frame(root, style="Main.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Build UI components
        self.create_header()
        self.create_input_section()
        self.create_output_section()
        self.create_stats_section()
        self.create_buttons()
        
    def setup_styles(self):
        """Configure modern dark theme styles"""
        style = ttk.Style()
        style.theme_use("clam")
        
        # Main frame
        style.configure("Main.TFrame", background="#1e1e2e")
        
        # Labels
        style.configure("Header.TLabel",
                       background="#1e1e2e",
                       foreground="#cdd6f4",
                       font=("Segoe UI", 24, "bold"))
        
        style.configure("SubHeader.TLabel",
                       background="#1e1e2e",
                       foreground="#a6adc8",
                       font=("Segoe UI", 10))
        
        style.configure("Section.TLabel",
                       background="#1e1e2e",
                       foreground="#89b4fa",
                       font=("Segoe UI", 12, "bold"))
        
        style.configure("Stats.TLabel",
                       background="#313244",
                       foreground="#cdd6f4",
                       font=("Segoe UI", 11),
                       padding=(10, 5))
        
        # Buttons
        style.configure("Primary.TButton",
                       background="#89b4fa",
                       foreground="#1e1e2e",
                       font=("Segoe UI", 11, "bold"),
                       padding=(20, 10))
        style.map("Primary.TButton",
                 background=[("active", "#b4befe")])
        
        style.configure("Secondary.TButton",
                       background="#45475a",
                       foreground="#cdd6f4",
                       font=("Segoe UI", 10),
                       padding=(15, 8))
        style.map("Secondary.TButton",
                 background=[("active", "#585b70")])
        
        # Entry
        style.configure("Custom.TEntry",
                       fieldbackground="#313244",
                       foreground="#cdd6f4",
                       insertcolor="#cdd6f4")
        
        # LabelFrame
        style.configure("Card.TLabelframe",
                       background="#1e1e2e",
                       foreground="#cdd6f4")
        style.configure("Card.TLabelframe.Label",
                       background="#1e1e2e",
                       foreground="#89b4fa",
                       font=("Segoe UI", 11, "bold"))

    def create_header(self):
        """Create the header section"""
        header_frame = ttk.Frame(self.main_frame, style="Main.TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title = ttk.Label(header_frame, 
                         text="🔄 Bubble Sort",
                         style="Header.TLabel")
        title.pack()
        
        subtitle = ttk.Label(header_frame,
                            text="Optimized Exchange Sort Algorithm with Early Break",
                            style="SubHeader.TLabel")
        subtitle.pack()

    def create_input_section(self):
        """Create input section with text entry and file loading"""
        input_frame = ttk.LabelFrame(self.main_frame, 
                                     text=" Input Data ",
                                     style="Card.TLabelframe",
                                     padding=15)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Input label
        input_label = ttk.Label(input_frame,
                               text="Enter numbers (comma or space separated):",
                               style="SubHeader.TLabel")
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Input text widget with custom styling
        self.input_text = tk.Text(input_frame,
                                  height=3,
                                  bg="#313244",
                                  fg="#cdd6f4",
                                  insertbackground="#cdd6f4",
                                  font=("Consolas", 11),
                                  relief=tk.FLAT,
                                  padx=10,
                                  pady=10,
                                  wrap=tk.WORD)
        self.input_text.pack(fill=tk.X, pady=(0, 10))
        
        # File load button
        load_btn = ttk.Button(input_frame,
                             text="📂 Load from File",
                             style="Secondary.TButton",
                             command=self.load_file)
        load_btn.pack(anchor=tk.W)

    def create_output_section(self):
        """Create output section to display sorted array"""
        output_frame = ttk.LabelFrame(self.main_frame,
                                      text=" Sorted Output ",
                                      style="Card.TLabelframe",
                                      padding=15)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Output text widget
        self.output_text = tk.Text(output_frame,
                                   height=6,
                                   bg="#313244",
                                   fg="#a6e3a1",
                                   font=("Consolas", 11),
                                   relief=tk.FLAT,
                                   padx=10,
                                   pady=10,
                                   wrap=tk.WORD,
                                   state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)

    def create_stats_section(self):
        """Create statistics section for execution time and comparisons"""
        stats_frame = ttk.Frame(self.main_frame, style="Main.TFrame")
        stats_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Stats container with grid
        stats_container = tk.Frame(stats_frame, bg="#313244", padx=15, pady=15)
        stats_container.pack(fill=tk.X)
        stats_container.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Execution time
        time_frame = tk.Frame(stats_container, bg="#313244")
        time_frame.grid(row=0, column=0, padx=10)
        
        tk.Label(time_frame, text="⏱️ Execution Time",
                bg="#313244", fg="#a6adc8",
                font=("Segoe UI", 9)).pack()
        self.time_label = tk.Label(time_frame, text="-- ms",
                                   bg="#313244", fg="#f9e2af",
                                   font=("Segoe UI", 14, "bold"))
        self.time_label.pack()
        
        # Comparisons
        comp_frame = tk.Frame(stats_container, bg="#313244")
        comp_frame.grid(row=0, column=1, padx=10)
        
        tk.Label(comp_frame, text="🔍 Comparisons",
                bg="#313244", fg="#a6adc8",
                font=("Segoe UI", 9)).pack()
        self.comp_label = tk.Label(comp_frame, text="--",
                                   bg="#313244", fg="#89b4fa",
                                   font=("Segoe UI", 14, "bold"))
        self.comp_label.pack()
        
        # Swaps
        swap_frame = tk.Frame(stats_container, bg="#313244")
        swap_frame.grid(row=0, column=2, padx=10)
        
        tk.Label(swap_frame, text="🔄 Swaps",
                bg="#313244", fg="#a6adc8",
                font=("Segoe UI", 9)).pack()
        self.swap_label = tk.Label(swap_frame, text="--",
                                   bg="#313244", fg="#f38ba8",
                                   font=("Segoe UI", 14, "bold"))
        self.swap_label.pack()

    def create_buttons(self):
        """Create action buttons"""
        btn_frame = ttk.Frame(self.main_frame, style="Main.TFrame")
        btn_frame.pack(fill=tk.X)
        
        # Sort button
        sort_btn = ttk.Button(btn_frame,
                             text="▶ Sort Array",
                             style="Primary.TButton",
                             command=self.perform_sort)
        sort_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        clear_btn = ttk.Button(btn_frame,
                              text="🗑️ Clear All",
                              style="Secondary.TButton",
                              command=self.clear_all)
        clear_btn.pack(side=tk.LEFT)
        
        # Sample data button
        sample_btn = ttk.Button(btn_frame,
                               text="📊 Load Sample",
                               style="Secondary.TButton",
                               command=self.load_sample)
        sample_btn.pack(side=tk.RIGHT)

    def create_progress_window(self):
        """Create a modern progress window for sorting visualization"""
        self.progress_window = tk.Toplevel(self.root)
        self.progress_window.title("Sorting in Progress")
        self.progress_window.geometry("450x380")
        self.progress_window.configure(bg="#1e1e2e")
        self.progress_window.resizable(False, False)
        self.progress_window.transient(self.root)
        self.progress_window.grab_set()
        
        # Center the window
        self.progress_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 225
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 190
        self.progress_window.geometry(f"+{x}+{y}")
        
        # Main container
        container = tk.Frame(self.progress_window, bg="#1e1e2e", padx=30, pady=25)
        container.pack(fill=tk.BOTH, expand=True)
        
        # Animated icon
        self.progress_icon_label = tk.Label(container, text="🔄", 
                                            font=("Segoe UI", 36),
                                            bg="#1e1e2e", fg="#89b4fa")
        self.progress_icon_label.pack(pady=(0, 15))
        
        # Title
        tk.Label(container, text="Sorting Array...",
                font=("Segoe UI", 16, "bold"),
                bg="#1e1e2e", fg="#cdd6f4").pack()
        
        # Status label
        self.progress_status = tk.Label(container, text="Initializing...",
                                        font=("Segoe UI", 10),
                                        bg="#1e1e2e", fg="#a6adc8")
        self.progress_status.pack(pady=(5, 15))
        
        # Progress bar container
        progress_frame = tk.Frame(container, bg="#313244", padx=3, pady=3)
        progress_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Custom styled progress bar
        style = ttk.Style()
        style.configure("Custom.Horizontal.TProgressbar",
                       background="#89b4fa",
                       troughcolor="#45475a",
                       borderwidth=0,
                       lightcolor="#89b4fa",
                       darkcolor="#89b4fa")
        
        self.progress_bar = ttk.Progressbar(progress_frame,
                                            style="Custom.Horizontal.TProgressbar",
                                            length=380,
                                            mode='determinate')
        self.progress_bar.pack(fill=tk.X)
        
        # Percentage label
        self.progress_percent = tk.Label(container, text="0%",
                                         font=("Segoe UI", 12, "bold"),
                                         bg="#1e1e2e", fg="#a6e3a1")
        self.progress_percent.pack()
        
        # Stats frame
        stats_frame = tk.Frame(container, bg="#313244", padx=15, pady=10)
        stats_frame.pack(fill=tk.X, pady=(15, 0))
        stats_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Pass counter
        pass_frame = tk.Frame(stats_frame, bg="#313244")
        pass_frame.grid(row=0, column=0)
        tk.Label(pass_frame, text="Pass", bg="#313244", fg="#a6adc8",
                font=("Segoe UI", 9)).pack()
        self.progress_pass = tk.Label(pass_frame, text="0",
                                      bg="#313244", fg="#f9e2af",
                                      font=("Segoe UI", 14, "bold"))
        self.progress_pass.pack()
        
        # Comparisons counter
        comp_frame = tk.Frame(stats_frame, bg="#313244")
        comp_frame.grid(row=0, column=1)
        tk.Label(comp_frame, text="Comparisons", bg="#313244", fg="#a6adc8",
                font=("Segoe UI", 9)).pack()
        self.progress_comp = tk.Label(comp_frame, text="0",
                                      bg="#313244", fg="#89b4fa",
                                      font=("Segoe UI", 14, "bold"))
        self.progress_comp.pack()
        
        # Swaps counter
        swap_frame = tk.Frame(stats_frame, bg="#313244")
        swap_frame.grid(row=0, column=2)
        tk.Label(swap_frame, text="Swaps", bg="#313244", fg="#a6adc8",
                font=("Segoe UI", 9)).pack()
        self.progress_swap = tk.Label(swap_frame, text="0",
                                      bg="#313244", fg="#f38ba8",
                                      font=("Segoe UI", 14, "bold"))
        self.progress_swap.pack()
        
        # Animation state
        self.animation_icons = ["🔄", "🔃", "🔁", "🔂"]
        self.animation_index = 0
        self.animate_icon()
        
    def animate_icon(self):
        """Animate the sorting icon"""
        if hasattr(self, 'progress_window') and self.progress_window.winfo_exists():
            self.animation_index = (self.animation_index + 1) % len(self.animation_icons)
            self.progress_icon_label.config(text=self.animation_icons[self.animation_index])
            self.root.after(300, self.animate_icon)
    
    def update_progress(self, current_pass, total_passes, comparisons, swaps, status="", force_complete=False):
        """Update the progress window"""
        if hasattr(self, 'progress_window') and self.progress_window.winfo_exists():
            if force_complete:
                progress = 100
            else:
                progress = (current_pass / total_passes) * 100 if total_passes > 0 else 0
            self.progress_bar['value'] = progress
            self.progress_percent.config(text=f"{progress:.0f}%")
            self.progress_pass.config(text=str(current_pass))
            self.progress_comp.config(text=str(comparisons))
            self.progress_swap.config(text=str(swaps))
            if status:
                self.progress_status.config(text=status)
            self.progress_window.update()
    
    def close_progress_window(self):
        """Close the progress window"""
        if hasattr(self, 'progress_window') and self.progress_window.winfo_exists():
            self.progress_window.destroy()

    def bubble_sort_optimized(self, arr, show_progress=False):
        """
        Optimized Bubble Sort Algorithm
        
        Uses an exchange sort approach with early termination.
        If no swaps occur during a pass, the array is already sorted.
        
        Args:
            arr: List of numbers to sort
            show_progress: Whether to update progress window
            
        Returns:
            tuple: (sorted_array, comparisons, swaps)
        """
        n = len(arr)
        arr = arr.copy()  # Don't modify original
        comparisons = 0
        swaps = 0
        total_passes = n - 1
        
        # Calculate update interval - update less frequently for larger arrays
        update_interval = max(500, n * 5)  # Update every 500+ comparisons
        last_update = 0
        
        for i in range(n - 1):
            swapped = False  # Optimization flag
            
            # Last i elements are already in place
            for j in range(n - 1 - i):
                comparisons += 1
                
                # Compare adjacent elements (descending order)
                if arr[j] < arr[j + 1]:
                    # Exchange (swap) elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
                    swapped = True
            
            # Update progress only at end of each pass (much faster)
            if show_progress and (comparisons - last_update >= update_interval or i == n - 2):
                self.update_progress(i + 1, total_passes, comparisons, swaps,
                                    f"Pass {i + 1} of {total_passes}")
                last_update = comparisons
            
            # Early break: if no swaps occurred, array is sorted
            if not swapped:
                if show_progress:
                    self.update_progress(i + 1, total_passes, comparisons, swaps,
                                        "✅ Early termination - Array sorted!", force_complete=True)
                break
        
        if show_progress:
            self.update_progress(total_passes, total_passes, comparisons, swaps,
                                "✅ Sorting complete!", force_complete=True)
                
        return arr, comparisons, swaps

    def parse_input(self, text):
        """Parse input text to extract numbers"""
        # Remove brackets and split by comma, space, newline, or semicolon
        text = text.strip()
        text = re.sub(r'[\[\]\(\)\{\}]', '', text)
        numbers = re.split(r'[,\s;]+', text)
        
        result = []
        for num in numbers:
            num = num.strip()
            if num:
                try:
                    # Try integer first, then float
                    if '.' in num:
                        result.append(float(num))
                    else:
                        result.append(int(num))
                except ValueError:
                    pass
        return result

    def perform_sort(self):
        """Execute the bubble sort and display results"""
        input_data = self.input_text.get("1.0", tk.END).strip()
        
        if not input_data:
            messagebox.showwarning("No Input", 
                                  "Please enter numbers or load a file.")
            return
        
        # Parse input
        numbers = self.parse_input(input_data)
        
        if not numbers:
            messagebox.showerror("Invalid Input",
                               "Could not parse any valid numbers from input.")
            return
        
        if len(numbers) < 2:
            messagebox.showwarning("Insufficient Data",
                                  "Please enter at least 2 numbers to sort.")
            return
        
        # Store numbers for sorting thread
        self.numbers_to_sort = numbers
        
        # Create and show progress window
        self.create_progress_window()
        
        # Start sorting in a slight delay to allow progress window to render
        self.root.after(100, self.run_sort_with_progress)
    
    def run_sort_with_progress(self):
        """Run the sort with progress updates"""
        numbers = self.numbers_to_sort
        
        # Perform sort and measure time
        start_time = time.perf_counter()
        sorted_arr, comparisons, swaps = self.bubble_sort_optimized(numbers, show_progress=True)
        end_time = time.perf_counter()
        
        execution_time = (end_time - start_time) * 1000  # Convert to ms
        
        # Close progress window
        self.close_progress_window()
        
        # Update output
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        
        # Format output - only show sorted array
        output = str(sorted_arr)
        
        self.output_text.insert("1.0", output)
        self.output_text.config(state=tk.DISABLED)
        
        # Update statistics
        if execution_time < 1:
            self.time_label.config(text=f"{execution_time:.4f} ms")
        else:
            self.time_label.config(text=f"{execution_time:.2f} ms")
            
        self.comp_label.config(text=str(comparisons))
        self.swap_label.config(text=str(swaps))

    def load_file(self):
        """Load numbers from a file"""
        filetypes = [
            ("Text files", "*.txt"),
            ("CSV files", "*.csv"),
            ("All files", "*.*")
        ]
        
        filepath = filedialog.askopenfilename(
            title="Select a file with numbers",
            filetypes=filetypes
        )
        
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    content = file.read()
                    
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)
                
                # Validate that we can parse numbers
                numbers = self.parse_input(content)
                if numbers:
                    messagebox.showinfo("File Loaded",
                                       f"Successfully loaded {len(numbers)} numbers.")
                else:
                    messagebox.showwarning("Warning",
                                          "File loaded but no valid numbers found.")
                    
            except Exception as e:
                messagebox.showerror("Error",
                                    f"Could not read file:\n{str(e)}")

    def load_sample(self):
        """Load sample data for demonstration"""
        sample = "64, 34, 25, 12, 22, 11, 90, 45, 33, 77, 55, 88, 99, 10, 5"
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert("1.0", sample)

    def clear_all(self):
        """Clear all inputs and outputs"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.time_label.config(text="-- ms")
        self.comp_label.config(text="--")
        self.swap_label.config(text="--")


def main():
    root = tk.Tk()
    app = BubbleSortApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
