class Card:
    def __init__(self, id: int, front: str, back: str):
        self.id = id
        self.front = front
        self.back = back
    
    def __str__(self):
        return f"[{self.id}] {self.front} -> {self.back}"
