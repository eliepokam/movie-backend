# %%
from database import SessionLocal
from query_helpers import *

db = SessionLocal()
# %%
movie = get_movie(db , movie_id=1)
print(movie.title , movie.genres)

db.close()
# %%
elie = get_movies(db , limit = 5)
for film in elie :
    print(f"ID : {film.movieId} , Titre : {film.title} , Genres : {film.genres}")

db.close() 

# %%
rating = get_rating(db , movie_id=1 ,user_id= 1)
print(f"User ID : {rating.userId} , Movie ID : {rating.movieId} , Rating : {rating.rating}")
db.close()
# %%
rating = get_ratings(db , movie_id=1 ,min_rating = 3.5 , limit = 10)
for film in rating :
  print(f"ID : {film.movieId} , Note : {film.rating}")
db.close()

# %%
rating = get_ratings(db , movie_id=1 ,min_rating = 3.5 , limit = 10 , user_id= 1)
for film in rating :
  print(f"ID : {film.movieId} , Note : {film.rating}")
db.close()

# %%
tag = get_tag(db , user_id=2 , movie_id=60756 , tag_text="funny")

print(f"User ID : {tag.userId} , Movie ID : {tag.movieId} , Tag : {tag.tag}")

# %%
n_movies = get_movie_count(db)
print(f"Nombre de films : {n_movies}")

db.close()
# %%
n_rating = get_rating_count(db)
print(f"Nombre de films :{n_rating}")
# %%
