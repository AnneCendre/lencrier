from datetime import datetime


mois_fr = {
    "janvier": 1, "février": 2, "mars": 3, "avril": 4,
    "mai": 5, "juin": 6, "juillet": 7, "août": 8,
    "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12
}


def date_fr_vers_iso(date_str):
    # Exemple d'entrée : "27 août 2023 à 8h37"
    date_part, time_part = date_str.split(" à ")

    # --- Partie date ---
    jour, mois_str, annee = date_part.split(" ")
    mois = mois_fr[mois_str]

    # --- Partie heure ---
    heure = int(time_part.split("h")[0])
    minute = int(time_part.split("h")[1])

    # Construire l'objet datetime
    dt = datetime(int(annee), mois, int(jour), heure, minute)

    # Retour ISO 8601
    return dt.isoformat(timespec="minutes")
