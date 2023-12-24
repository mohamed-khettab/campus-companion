import customtkinter
from ..models.schoology_model import SchoologyModel
from ..models.task_model import TaskModel
from ..models.notebook_model import NotebookModel
from ..models.button_model import ButtonModel
import textwrap

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class CampusCompanion(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Campus Companion")
        self.geometry(f"{1100}x{610}")
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=15)

        self.sections = SchoologyModel.get_sections()
        self.grades = SchoologyModel.get_grades(self.sections)
        self.task_counter = 0

        self.sidebar_left()
        self.main()
        self.sidebar_right()

        tasks = TaskModel.load_tasks()
        for task_text in tasks:
            self.create_task_widgets(task_text)

    def sidebar_left(self):
        self.sidebar_frame_left = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame_left.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame_left.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame_left,
            text="Campus\nCompanion",
            font=customtkinter.CTkFont(size=30, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.save_entry_button = customtkinter.CTkButton(
            self.sidebar_frame_left, text="Save Notebook Entry", command=self.save_notebook
        )
        self.save_entry_button.grid(row=1, column=0, padx=20, pady=10)

        self.upload_entry_button = customtkinter.CTkButton(
            self.sidebar_frame_left, text="Upload Notebook Entry", command=self.upload_notebook
        )
        self.upload_entry_button.grid(row=2, column=0, padx=20, pady=10)

        self.delete_entry_button = customtkinter.CTkButton(
            self.sidebar_frame_left, text="Delete Notebook Entry", command=self.delete_notebook
        )
        self.delete_entry_button.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame_left, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame_left,
            values=["Dark", "Light"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=20)

    def main(self):
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Quickly enter a task"
        )
        self.entry.grid(
            row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )

        self.add_task_button = customtkinter.CTkButton(
            master=self,
            text="Add Task",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.add_task,
        )
        self.add_task_button.grid(
            row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        self.textbox = customtkinter.CTkTextbox(self, width=300)
        self.textbox.grid(
            row=1, rowspan=2, column=1, padx=20, pady=(5, 0), sticky="nsew"
        )

        self.textbox.insert("0.0", "Type in your notebook here.")
        
        self.top_frame = customtkinter.CTkFrame(self, width=300, height=50)
        self.top_frame.grid(row = 0, column = 1, padx= 20, pady=20, sticky="nsew")

        self.bullet_point_button = customtkinter.CTkButton(self.top_frame, text="Add Bullet Point", command=self.insert_bullet_point, width=65, height=10)
        self.bullet_point_button.grid(row=0, column=0, padx=20, pady=(15,0), sticky="nsew")

        self.white_button = customtkinter.CTkButton(self.top_frame, text="Default", command= lambda: self.change_color("#FFFFFF"), width=65, height=10, fg_color="#FFFFFF", hover_color="#BDBDBD", text_color="#000000")
        self.white_button.grid(row=0, column=1, padx=(0,15), pady=(15,0), sticky="nsew")

        self.red_button = customtkinter.CTkButton(self.top_frame, text="Red", command= lambda: self.change_color("#F07751"), width=65, height=10, fg_color="#F07751", hover_color="#953636", text_color="#000000")
        self.red_button.grid(row=0, column=2, padx=(0,15), pady=(15,0), sticky="nsew")

        self.blue_button = customtkinter.CTkButton(self.top_frame, text="Blue", command= lambda: self.change_color("#59C4F5"), width=65, height=10, fg_color="#59C4F5", text_color="#000000")
        self.blue_button.grid(row=0, column=3, padx=(0,15), pady=(15,0), sticky="nsew")

        self.yellow_button = customtkinter.CTkButton(self.top_frame, text="Yellow", command= lambda: self.change_color("#FEEF6B"), width=65, height=10, fg_color="#FEEF6B", hover_color="#B1AA6E", text_color="#000000")
        self.yellow_button.grid(row=0, column=4, padx=(0,15), pady=(15,0), sticky="nsew")

        self.green_button = customtkinter.CTkButton(self.top_frame, text="Green", command= lambda: self.change_color("#81C784"), width=65, height=10, fg_color="#81C784", hover_color="#33691E", text_color="#000000")
        self.green_button.grid(row=0, column=5, padx=(0,15), pady=(15,0), sticky="nsew")

        


    def sidebar_right(self):
        self.sidebar_frame_right = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame_right.grid(row=0, column=3, rowspan=3, sticky="nsew")
        self.sidebar_frame_right.grid_rowconfigure(4, weight=1)

        self.upcoming_label = customtkinter.CTkLabel(
            self.sidebar_frame_right,
            text="Upcoming Tasks",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.upcoming_label.grid(row=0, column=0, padx=20, pady=(20, 5))

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.sidebar_frame_right, height=100
        )
        self.scrollable_frame.grid(
            row=1, rowspan=1, column=0, padx=20, pady=10, sticky="nsew"
        )
        self.grades_label = customtkinter.CTkLabel(
            self.sidebar_frame_right, text="Grades", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.grades_label.grid(
            row=2, column=0, padx=20, pady=5, sticky="nsew"
        )
        self.grades_frame = customtkinter.CTkFrame(self.sidebar_frame_right, width=10, corner_radius=5, height=160)
        self.grades_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        for i, (name, grade) in enumerate(self.grades):
            label = customtkinter.CTkLabel(self.grades_frame, text=f"{name}: {grade}")
            label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def add_task(self):
        task_text = self.entry.get()
        TaskModel.save_task(task_text)
        self.create_task_widgets(task_text)

    def create_task_widgets(self, task_text):
        check_box = customtkinter.CTkCheckBox(
            self.scrollable_frame,
            text="\n".join(textwrap.wrap(task_text, width=20))
        )
        check_box.grid(row=self.task_counter, column=0, padx=(10, 5), pady=10)
        delete_button = customtkinter.CTkButton(
            self.scrollable_frame,
            text="Delete",
            width=10,
            command=lambda: self.remove_task(task_text, check_box, delete_button)
        )
        delete_button.grid(row=self.task_counter, column=1, padx=(5, 10), pady=10, sticky="s")
        self.task_counter += 1

    def remove_task(self, task_text, check_box, delete_button):
        check_box.destroy()
        delete_button.destroy()
        TaskModel.remove_task(task_text)

    def save_notebook(self):
        notebook_text = self.textbox.get("1.0", "end-1c")
        NotebookModel.save_notebook(notebook_text)

    def delete_notebook(self):
        NotebookModel.delete_notebook(self.textbox)

    def upload_notebook(self):
        NotebookModel.upload_notebook(self.textbox)

    def insert_bullet_point(self):
        ButtonModel.insert_bullet_point(self.textbox)

    def change_color(self, color):
        ButtonModel.change_color(self.textbox, color)