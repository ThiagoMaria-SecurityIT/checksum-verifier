import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class ChecksumApp:
    def __init__(self, root, core_logic):
        self.root = root
        self.core = core_logic
        self.setup_ui()
        
    def setup_ui(self):
        self.root.title("SHA256 Checksum Verifier")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # File to verify section
        ttk.Label(main_frame, text="File to verify:", font=('Arial', 10, 'bold')).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # File selection
        ttk.Label(main_frame, text="File path:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.file_path = tk.StringVar()
        self.file_entry = ttk.Entry(main_frame, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2, padx=(5, 5))
        
        ttk.Button(main_frame, text="Browse", command=self.browse_file).grid(
            row=1, column=2, pady=2, padx=(5, 0))
        
        # Calculate hash button
        ttk.Button(main_frame, text="Calculate SHA256", 
                  command=self.calculate_hash).grid(row=2, column=0, columnspan=3, pady=10)
        
        # Calculated hash display
        ttk.Label(main_frame, text="Calculated hash:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.calculated_hash = tk.StringVar()
        hash_entry = ttk.Entry(main_frame, textvariable=self.calculated_hash, 
                              width=70, state='readonly')
        hash_entry.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=2, padx=(5, 0))
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=15)
        
        # Expected hash section
        ttk.Label(main_frame, text="Expected hash source:", 
                 font=('Arial', 10, 'bold')).grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Method selection
        self.method_var = tk.StringVar(value="manual")
        methods_frame = ttk.Frame(main_frame)
        methods_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Radiobutton(methods_frame, text="Manual input", 
                       variable=self.method_var, value="manual").pack(side=tk.LEFT)
        ttk.Radiobutton(methods_frame, text="From URL", 
                       variable=self.method_var, value="url").pack(side=tk.LEFT, padx=(20, 0))
        ttk.Radiobutton(methods_frame, text="From file", 
                       variable=self.method_var, value="file").pack(side=tk.LEFT, padx=(20, 0))
        
        # Manual input
        self.manual_frame = ttk.Frame(main_frame)
        self.manual_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        ttk.Label(self.manual_frame, text="Paste hash:").grid(row=0, column=0, sticky=tk.W)
        self.manual_hash = tk.StringVar()
        ttk.Entry(self.manual_frame, textvariable=self.manual_hash, width=70).grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        self.manual_frame.columnconfigure(1, weight=1)
        
        # URL input
        self.url_frame = ttk.Frame(main_frame)
        self.url_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        ttk.Label(self.url_frame, text="Checksum URL:").grid(row=0, column=0, sticky=tk.W)
        self.url_path = tk.StringVar()
        ttk.Entry(self.url_frame, textvariable=self.url_path, width=60).grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 5))
        ttk.Button(self.url_frame, text="Load", command=self.load_from_url).grid(row=0, column=2)
        self.url_frame.columnconfigure(1, weight=1)
        
        # File input
        self.file_input_frame = ttk.Frame(main_frame)
        self.file_input_frame.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        ttk.Label(self.file_input_frame, text="Checksum file:").grid(row=0, column=0, sticky=tk.W)
        self.checksum_file_path = tk.StringVar()
        ttk.Entry(self.file_input_frame, textvariable=self.checksum_file_path, width=50).grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 5))
        ttk.Button(self.file_input_frame, text="Browse", command=self.browse_checksum_file).grid(row=0, column=2)
        ttk.Button(self.file_input_frame, text="Load", command=self.load_from_file).grid(row=0, column=3, padx=(5, 0))
        self.file_input_frame.columnconfigure(1, weight=1)
        
        # Expected hash display
        ttk.Label(main_frame, text="Expected hash:").grid(row=10, column=0, sticky=tk.W, pady=(10, 2))
        self.expected_hash = tk.StringVar()
        expected_entry = ttk.Entry(main_frame, textvariable=self.expected_hash, 
                                  width=70, state='readonly')
        expected_entry.grid(row=10, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 2), padx=(5, 0))
        
        # Verify button
        ttk.Button(main_frame, text="Verify Checksum", 
                  command=self.verify_checksum, style='Accent.TButton').grid(
            row=11, column=0, columnspan=3, pady=20)
        
        # Result display
        self.result_text = tk.Text(main_frame, height=6, width=70, state='disabled')
        self.result_text.grid(row=12, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Show manual frame by default
        self.show_selected_method()
        self.method_var.trace('w', lambda *args: self.show_selected_method())
    
    def show_selected_method(self):
        """Show/hide method-specific frames"""
        method = self.method_var.get()
        self.manual_frame.grid_remove()
        self.url_frame.grid_remove()
        self.file_input_frame.grid_remove()
        
        if method == "manual":
            self.manual_frame.grid()
        elif method == "url":
            self.url_frame.grid()
        elif method == "file":
            self.file_input_frame.grid()
    
    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select file to verify",
            initialdir=os.path.expanduser("~/Downloads")
        )
        if filename:
            self.file_path.set(filename)
    
    def browse_checksum_file(self):
        filename = filedialog.askopenfilename(
            title="Select checksum file",
            filetypes=[("All files", "*.*"), ("Text files", "*.txt")]
        )
        if filename:
            self.checksum_file_path.set(filename)
    
    def calculate_hash(self):
        if not self.file_path.get():
            messagebox.showerror("Error", "Please select a file first")
            return
        
        try:
            file_hash = self.core.calculate_sha256(self.file_path.get())
            self.calculated_hash.set(file_hash)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate hash: {str(e)}")
    
    def load_from_url(self):
        if not self.url_path.get():
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        try:
            checksums = self.core.download_checksum_file(self.url_path.get())
            self.select_checksum_from_list(checksums)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load from URL: {str(e)}")
    
    def load_from_file(self):
        if not self.checksum_file_path.get():
            messagebox.showerror("Error", "Please select a checksum file")
            return
        
        try:
            checksums = self.core.load_checksum_file(self.checksum_file_path.get())
            self.select_checksum_from_list(checksums)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load from file: {str(e)}")
    
    def select_checksum_from_list(self, checksums: dict):
        """Let user select which checksum to use from a list"""
        if not checksums:
            messagebox.showinfo("Info", "No checksums found in the file")
            return
        
        # Create selection window
        select_window = tk.Toplevel(self.root)
        select_window.title("Select checksum")
        select_window.geometry("500x300")
        
        ttk.Label(select_window, text="Select the checksum for your file:").pack(pady=10)
        
        # Listbox with filenames
        listbox = tk.Listbox(select_window, width=80, height=10)
        listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        for filename in checksums.keys():
            listbox.insert(tk.END, filename)
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                filename = listbox.get(selection[0])
                self.expected_hash.set(checksums[filename])
                select_window.destroy()
        
        ttk.Button(select_window, text="Select", command=on_select).pack(pady=10)
    
    def verify_checksum(self):
        if not self.calculated_hash.get():
            messagebox.showerror("Error", "Please calculate the file hash first")
            return
        
        if not self.expected_hash.get():
            messagebox.showerror("Error", "Please provide an expected hash")
            return
        
        # For manual method, get from manual input
        if self.method_var.get() == "manual":
            self.expected_hash.set(self.manual_hash.get())
        
        is_valid = self.core.verify_checksum(
            self.calculated_hash.get(), 
            self.expected_hash.get()
        )
        
        self.display_result(is_valid)
    
    def display_result(self, is_valid: bool):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        
        filename = os.path.basename(self.file_path.get())
        
        if is_valid:
            result_text = f"✓ VERIFICATION SUCCESSFUL\n\n"
            result_text += f"File: {filename}\n"
            result_text += f"Status: Checksum matches - file is authentic\n"
            result_text += f"Hash: {self.calculated_hash.get()}"
            self.result_text.config(bg="#d4edda", fg="#155724")
        else:
            result_text = f"✗ VERIFICATION FAILED\n\n"
            result_text += f"File: {filename}\n"
            result_text += f"Status: Checksum DOES NOT match - file may be corrupted or tampered with\n\n"
            result_text += f"Calculated: {self.calculated_hash.get()}\n"
            result_text += f"Expected:   {self.expected_hash.get()}"
            self.result_text.config(bg="#f8d7da", fg="#721c24")
        
        self.result_text.insert(1.0, result_text)
        self.result_text.config(state='disabled')