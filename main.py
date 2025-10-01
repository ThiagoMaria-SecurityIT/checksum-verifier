import tkinter as tk
from checksum_core import ChecksumVerifier
from gui_layout import ChecksumApp

def main():
    # Initialize core logic
    core_logic = ChecksumVerifier()
    
    # Create main window
    root = tk.Tk()
    
    # Create and run the application
    app = ChecksumApp(root, core_logic)
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()