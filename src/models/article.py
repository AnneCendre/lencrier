from dataclasses import dataclass
from typing import Optional

@dataclass
class Article:
    nom_lencrier: str
    id_lencrier: int
    titre: str
    date_lencrier: str
    content: str = ""
    date_time: Optional[str] = None

    def __post_init__(self):
        from utils.date_utils import date_fr_vers_iso
        if self.date_lencrier and not self.date_time:
            self.date_time = date_fr_vers_iso(self.date_lencrier)

        
    def __str__(self):
        return f"{self.id_lencrier} ({self.titre})"

    def __lt__(self, other):
        return self.id_lencrier < other.id_lencrier