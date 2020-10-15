import Excpetion

class DadosMinimosExcepetion(Exception):
    def __init__(self, text):
        self.text = text