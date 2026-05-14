# lencrier

 cmd : 
`cendre@Terminus:~/dev/lencrier$ python3 ./src/01_lire_article.py`

modules :
pip install -r requirements.txt


# archi 
.
├── analyse.md
├── articles.db
├── exports
│   ├── test_Cendre.html                    # fichiers d'exemples plus légers
│   ├── test_Les amours de Cendre.html
│   └── test_Mes écrits manuscrits.html
├── exports (src)                           # exports complets des journaux
├── README.md
├── requirement.txt
├── result
│   ├── data.csv                            # export CSV (sans contenu)
│   ├── journaux.html                       # export HTML obtenu à partir du template.html
│   └── template.html
├── skel                                    # mise en forme sur le site journalintime
├── src
│   ├── __init__.py
│   ├── 01_lire_articles.py                 # lit les articles et les sauve dans la base de données
│   ├── 02_embeded.py                       # lecture sémantique
│   ├── exemple_create_table.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── article.py
│   │   ├── metadata.py
│   └── utils
│       ├── __init__.py
│       ├── database.py
│       ├── date_utils.py
│       ├── exporter.py
│       ├── importer.py
└── todo.md



