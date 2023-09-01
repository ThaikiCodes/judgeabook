from dataclasses import dataclass
import jsonpickle

@dataclass
class Zodiac:
    sign: str
    age: int
    year: int
    traits: list[str]
    emotion: str
