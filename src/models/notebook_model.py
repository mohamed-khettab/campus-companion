import tkinter.filedialog
import os

class NotebookModel:
    def save_notebook(notebook_text):
        default_folder = os.path.join(os.getcwd(), "data", "notebooks")
        file_path = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            initialdir=default_folder,
        )

        if file_path:
            with open(file_path, "w") as file:
                file.write(notebook_text)

    def delete_notebook(textbox):
        textbox.delete("1.0", "end")

    def upload_notebook(textbox):
        file_path = tkinter.filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")]
        )

        if file_path:
            with open(file_path, "r") as file:
                notebook_text = file.read()
                textbox.delete("1.0", "end")
                textbox.insert("1.0", notebook_text)