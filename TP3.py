import feedparser

juego=input("Te informare sobre tu juego favorito")

n=juego.lower()

TresDJ = "https://www.3djuegos.com/universo/rss/rss.php"

noticias3dj = feedparser.parse(TresDJ)['entries']

for n in noticias3dj:
    if juego in n.title.lower():
    
        print("Noticas relacionadas:")
        print("--- " + n.title )
 
    



