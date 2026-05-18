# Name: Kris Kleiner
# Date: May 2026
# Assignment: Module 10 - GUI ToDo
# Purpose: Create a Tkinter To-Do List GUI with menu, scrolling, task entry,
#          right-click delete, and exit option.

import tkinter as tk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kleiner-ToDo")

        # Create menu bar
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0, bg="#1E3A5F", fg="#F4A261")
        file_menu.add_command(label="Exit", command=root.quit)

        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        # Instruction label
        self.label = tk.Label(
            root,
            text="Add a task below. Right-click a task to delete it.",
            bg="#1E3A5F",
            fg="#F4A261",
            pady=8
        )
        self.label.pack(fill=tk.X)

        # Entry box
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(fill=tk.X, padx=5, pady=5)
        self.entry.bind("<Return>", self.add_task)

        # Add button
        self.add_button = tk.Button(
            root,
            text="Add Task",
            command=self.add_task,
            bg="#F4A261",
            fg="black"
        )
        self.add_button.pack(fill=tk.X, padx=5, pady=5)

        # Frame for listbox and scrollbar
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks = tk.Listbox(
            frame,
            yscrollcommand=self.scrollbar.set,
            bg="#1E3A5F",
            fg="white",
            selectbackground="#F4A261",
            selectforeground="black",
            font=("Arial", 11)
        )
        self.tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.tasks.yview)

        # Mac + Windows right-click support
        self.tasks.bind("<Button-2>", self.delete_task)
        self.tasks.bind("<Button-3>", self.delete_task)

    def add_task(self, event=None):
        task = self.entry.get().strip()

        if task:
            self.tasks.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def delete_task(self, event):
        selected_task = self.tasks.nearest(event.y)

        if selected_task >= 0:
            self.tasks.delete(selected_task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
