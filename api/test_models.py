# %%
from database import SessionLocal
from models import Movie , Rating , Tag , Link 

db = SessionLocal()
# %%
# Tester la recuperation des films
movies = db.query(Movie).limit(10).all()
movies
for movie in movies :
    print(f"ID:  {movie.movieId} , Titre : {movie.title} ,Genre :  {movie.genres}")
# %%
# Recuperer les films du genre "Action"
action_movies = db.query(Movie).filter(Movie.genres == "Action").limit(10)
for movie in action_movies :
    print(f"ID:  {movie.movieId} , Titre : {movie.title} ,Genre :  {movie.genres}")
    
# %%
# Tester la recuperation de quelques evaluations
Ratings = db.query(Rating).limit(5).all()
for rating in Ratings :
    print(f"User ID : {rating.userId} , Movie ID : {rating.movieId} , Rating : {rating.rating}")
    
# %%
# Recuperer les notes superieurs ou egal a 4
hight_four = (
    db.query(Movie.title , Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
)

for title , rating in hight_four :
    print(title , rating)
# %%
# Recuperation des tags associes aux films
tags = db.query(Tag).limit(5).all()
for tag in tags :
    print(f"User ID : {tag.userId} , Movie ID : {tag.movieId} ,Tag : {tag.tag}")
# %%
# la classe link
links = db.query(Link).limit(5).all()

for link in links :
    print(f"Movie ID : {link.movieId} , IMDB ID : {link.imdbId} , TMDB ID : {link.tmdbId}")
# %%
# fermer la session
db.close()
# %%
