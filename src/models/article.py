class Article:
    def __init__(self, nomLencrier, idLencrier, titre, dateLencrier, content):
        self.nomLencrier = nomLencrier
        self.idLencrier = idLencrier
        self.titre = titre
        self.dateLencrier = dateLencrier
        self.content = content
        
    def __str__(self):
        return f"{self.idLencrier} ({self.titre})"

    def __lt__(self, other):
        return self.idLencrier < other.idLencrier