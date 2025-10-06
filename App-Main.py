import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import urllib.parse

class DuckDuckGoDorkerApp:
    """
    A GUI application using Tkinter to build and launch DuckDuckGo dork queries.
    """
    def __init__(self, master):
        """
        Initializes the application window, menus, and GUI elements.
        """
        self.master = master
        master.title("Advanced DuckDuckGo Dorker")
        master.geometry("550x500")  # Adjusted size for better layout

        self.create_menu()

        # --- Style Configuration ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", padding=6, font=('Helvetica', 10))
        style.configure("TEntry", padding=6, font=('Helvetica', 10))
        style.configure("TButton", padding=6, font=('Helvetica', 10, 'bold'))
        style.configure("TFrame", background="#f0f0f0")

        # --- Main Frame ---
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # --- Input Fields ---
        self.entries = {}
        dork_operators = {
            "main_query": "Main Search Term(s):",
            "intitle": "intitle: (Words in title)",
            "inurl": "inurl: (Words in URL)",
            "filetype": "filetype: (e.g., pdf, docx, xls)",
            "site": "site: (Search specific site)",
            "exclude_site": "-site: (Exclude specific site)",
            "exact_phrase": '"" (Exact Phrase)',
            "exclude_term": "- (Exclude Term)"
        }

        row_num = 0
        for key, label_text in dork_operators.items():
            label = ttk.Label(main_frame, text=label_text)
            label.grid(row=row_num, column=0, sticky=tk.W, padx=5, pady=5)
            entry = ttk.Entry(main_frame, width=40)
            entry.grid(row=row_num, column=1, sticky=tk.EW, padx=5, pady=5)
            self.entries[key] = entry
            row_num += 1

        main_frame.columnconfigure(1, weight=1)

        # --- Generated Query Display ---
        query_header = ttk.Label(main_frame, text="Generated Query:", font=('Helvetica', 10, 'italic'))
        query_header.grid(row=row_num, column=0, sticky=tk.W, padx=5, pady=10)

        self.generated_query_text = tk.StringVar()
        query_display = ttk.Label(main_frame, textvariable=self.generated_query_text, wraplength=500, font=('Courier', 9), foreground="blue")
        query_display.grid(row=row_num, column=1, sticky=tk.EW, padx=5, pady=10)
        row_num += 1

        # --- Buttons Frame ---
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row_num, column=0, columnspan=2, pady=15)

        search_btn = ttk.Button(button_frame, text="Generate & Search", command=self.generate_and_search)
        search_btn.pack(side=tk.LEFT, padx=10)

        copy_btn = ttk.Button(button_frame, text="Copy Query", command=self.copy_query)
        copy_btn.pack(side=tk.LEFT, padx=10)

        clear_btn = ttk.Button(button_frame, text="Clear Fields", command=self.clear_fields)
        clear_btn.pack(side=tk.LEFT, padx=10)

    def create_menu(self):
        """
        Creates the menu bar with File and Help options.
        """
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Clear Fields", command=self.clear_fields)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def show_about(self):
        """
        Displays an About dialog with application details.
        """
        about_text = (
            "Advanced DuckDuckGo Dorker\n"
            "Build your custom DuckDuckGo queries using various dork operators.\n"
            "Developed with Python and Tkinter.\n\n"
            "Innovate your search experience!"
        )
        messagebox.showinfo("About", about_text)

    def generate_and_search(self):
        """
        Constructs the DuckDuckGo query based on user input,
        displays it, and opens it in the default web browser.
        """
        query_parts = []

        # Main Query (mandatory)
        main_query = self.entries["main_query"].get().strip()
        if not main_query:
            messagebox.showwarning("Input Required", "Please enter the main search term(s).")
            return
        query_parts.append(main_query)

        # Dork Operators
        if self.entries["intitle"].get().strip():
            query_parts.append(f'intitle:"{self.entries["intitle"].get().strip()}"')
        if self.entries["inurl"].get().strip():
            query_parts.append(f'inurl:"{self.entries["inurl"].get().strip()}"')
        if self.entries["filetype"].get().strip():
            query_parts.append(f'filetype:{self.entries["filetype"].get().strip()}')
        if self.entries["site"].get().strip():
            query_parts.append(f'site:{self.entries["site"].get().strip()}')
        if self.entries["exclude_site"].get().strip():
            query_parts.append(f'-site:{self.entries["exclude_site"].get().strip()}')
        if self.entries["exact_phrase"].get().strip():
            query_parts.append(f'"{self.entries["exact_phrase"].get().strip()}"')
        if self.entries["exclude_term"].get().strip():
            excluded_terms = self.entries["exclude_term"].get().strip().split()
            for term in excluded_terms:
                query_parts.append(f'-{term}')

        # Combine query parts
        final_query = " ".join(query_parts)
        self.generated_query_text.set(final_query)

        # URL encode and construct the full DuckDuckGo URL
        encoded_query = urllib.parse.quote_plus(final_query)
        search_url = f"https://duckduckgo.com/?q={encoded_query}"
        print(f"Opening URL: {search_url}")  # Debug info in console

        webbrowser.open(search_url)

    def copy_query(self):
        """
        Copies the generated query to the clipboard.
        """
        query = self.generated_query_text.get()
        if query:
            self.master.clipboard_clear()
            self.master.clipboard_append(query)
            messagebox.showinfo("Copied", "The generated query has been copied to the clipboard.")
        else:
            messagebox.showwarning("No Query", "There is no generated query to copy.")

    def clear_fields(self):
        """
        Clears all input fields and the generated query display.
        """
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.generated_query_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = DuckDuckGoDorkerApp(root)
    root.mainloop()
