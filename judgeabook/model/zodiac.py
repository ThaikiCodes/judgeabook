from dataclasses import dataclass
import jsonpickle


@dataclass
class Zodiac:
    sign: str
    year: int
    traits: list[str]
