#node.py

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

    def __str__(self):
        output = f'{entry}'
        return output

    def __repr__(self):
        output = f'{entry}'
        return output
