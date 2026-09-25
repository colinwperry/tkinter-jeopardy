import tkinter as tk

from PIL import Image, ImageTk


class JeopardyGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.title("Jeopardy Game")
        self.root.configure(bg="#2a81b8")

        # List of images for questions and answers
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

        # Create the Jeopardy board
        self.create_board()

    def create_board(self):
        """Create a grid of buttons for the questions."""
        # Create a frame to hold the buttons
        board_frame = tk.Frame(self.root, bg="#1B5282")
        board_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Use 5 columns for the grid
        num_columns = 5
        row = 0
        col = 0

        self.buttons = []

        for idx, _ in enumerate(self.image_sets):
            button = tk.Button(
                board_frame,
                text=f"Question {idx + 1}",
                font=("Arial", 16),
                command=lambda idx=idx: self.reveal_question(idx),
                bg="#3BBEFF",
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

            # Move to the next row after 5 columns
            if col == num_columns:
                col = 0
                row += 1

        # Configure the root window for centering
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def reveal_question(self, idx):
        """Reveal the question or answer image based on the button state."""
        button_info = self.buttons[idx]
        button = button_info["button"]
        image_set = self.image_sets[idx]

        if button_info["state"] == 0:
            # Show the question image
            question_image = Image.open(image_set["question"])
            question_image = question_image.resize((250, 200))

            question_image_tk = ImageTk.PhotoImage(question_image)

            button.config(
                image=question_image_tk,
                text="",
            )

            # Keep a reference to prevent garbage collection
            button.image = question_image_tk

            button_info["state"] = 1

        elif button_info["state"] == 1:
            # Show the answer image
            answer_image = Image.open(image_set["answer"])
            answer_image = answer_image.resize((250, 200))

            answer_image_tk = ImageTk.PhotoImage(answer_image)

            button.config(
                image=answer_image_tk,
                text="",
            )

            # Keep a reference to prevent garbage collection
            button.image = answer_image_tk

            # Reset the button for the next round
            button_info["state"] = 0


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = JeopardyGame(root)
    root.mainloop()