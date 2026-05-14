from dataclasses import dataclass

@dataclass
class Metadata:
    id_lencrier: int
    embedding: str
    nb_caracteres: int
    nb_paragraphes: int


    def __str__(self):
        return f"{self.id_lencrier} ({self.nb_caracteres} caractères"