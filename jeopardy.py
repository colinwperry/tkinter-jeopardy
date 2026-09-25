import tkinter as tk

from PIL import Image, ImageTk


class JeopardyGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.title("Jeopardy Game")
        self.root.configure(bg="#2a81b8")
        self.FRAME_BG = "#1B5282"
        self.WIDGET_BG = "#3BBEFF"
        self.FONT_INFO = ("Arial", 16)

        self.image_sets = [
            {
                "question": "images/question_1.jpg",
                "answer": "images/answer_1.jpg",
            },
            {
                "question": "images/question_2.jpg",
                "answer": "images/answer_2.jpg",
            },
            {
                "question": "images/question_3.jpg",
                "answer": "images/answer_3.jpg",
            },
            {
                "question": "images/question_4.jpg",
                "answer": "images/answer_4.jpg",
            },
            {
                "question": "images/question_5.jpg",
                "answer": "images/answer_5.jpg",
            },
            {
                "question": "images/question_6.jpg",
                "answer": "images/answer_6.jpg",
            },
            {
                "question": "images/question_7.jpg",
                "answer": "images/answer_7.jpg",
            },
            {
                "question": "images/question_8.jpg",
                "answer": "images/answer_8.jpg",
            },
            {
                "question": "images/question_9.jpg",
                "answer": "images/answer_9.jpg",
            },
            {
                "question": "images/question_10.jpg",
                "answer": "images/answer_10.jpg",
            },
            {
                "question": "images/question_11.jpg",
                "answer": "images/answer_11.jpg",
            },
            {
                "question": "images/question_12.jpg",
                "answer": "images/answer_12.jpg",
            },
            {
                "question": "images/question_13.jpg",
                "answer": "images/answer_13.jpg",
            },
            {
                "question": "images/question_14.jpg",
                "answer": "images/answer_14.jpg",
            },
            {
                "question": "images/question_15.jpg",
                "answer": "images/answer_15.jpg",
            },
        ]

        self.create_board()

    def create_board(self):
        board_frame = tk.Frame(self.root, bg=self.FRAME_BG)
        board_frame.place(relx=0.5, rely=0.5, anchor="center")

        num_columns = 5
        row = 0
        col = 0

        self.buttons = []

        for idx, _ in enumerate(self.image_sets):
            button = tk.Button(
                board_frame,
                text=f"Question {idx + 1}",
                font=self.FONT_INFO,
                command=lambda idx=idx: self.reveal_question(idx),
                bg=self.WIDGET_BG,
                activebackground="#4682B4",
            )

            button.grid(
                row=row,
                column=col,
                padx=10,
                pady=10,
                ipadx=10,
                ipady=10,
            )

            self.buttons.append(
                {
                    "button": button,
                    "state": 0,  # 0 = Question, 1 = Answer
                    "idx": idx,
                }
            )

            col += 1

            if col == num_columns:
                col = 0
                row += 1

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def reveal_question(self, idx):
        button_info = self.buttons[idx]
        button = button_info["button"]
        image_set = self.image_sets[idx]

        if button_info["state"] == 0:
            question_image = Image.open(image_set["question"])
            question_image = question_image.resize((250, 200))

            question_image_tk = ImageTk.PhotoImage(question_image)

            button.config(
                image=question_image_tk,
                text="",
            )

            button.image = question_image_tk

            button_info["state"] = 1

        elif button_info["state"] == 1:
            answer_image = Image.open(image_set["answer"])
            answer_image = answer_image.resize((250, 200))

            answer_image_tk = ImageTk.PhotoImage(answer_image)

            button.config(
                image=answer_image_tk,
                text="",
            )

            button.image = answer_image_tk

            button_info["state"] = 0


if __name__ == "__main__":
    root = tk.Tk()
    game = JeopardyGame(root)
    root.mainloop()