from dataclasses import dataclass


@dataclass
class Message:
    text: str
    alias: str

    def __str__(self):
        return f"{self.alias}\n{self.text}"
