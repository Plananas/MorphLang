from Syntax.AbstractSyntaxTree import AbstractSyntaxTree


class Input:
    def __init__(self, prompt=None):
        self.prompt = prompt

    def __repr__(self):
        return f"Input(prompt={self.prompt})"