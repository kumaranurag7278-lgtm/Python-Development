"""A single quiz question: text plus True/False answer."""


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
