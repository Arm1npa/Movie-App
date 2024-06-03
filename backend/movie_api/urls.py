from django.urls import path
from .views import *

urlpatterns = [
    path('trending-movies/', get_trending_movies, name='trending-movies'),
    path('tvshows/', get_tv_shows, name='get_tv_shows'),
    path('latest-movies/', get_latest_movies, name='latest-movies'),
    path('tv-genres/', get_tv_genres, name='tv-genres'),
    path('tvshows/genres/<int:genre_id>/',
         get_tv_series_by_genre, name='tv_series_by_genre'),
    path('movie-genres/', get_movie_genres, name='movie-genres'),
    path('movies/genres/<int:genre_id>/',
         get_movies_by_genre, name='movies_by_genre'),
    path('movie/<int:movie_id>/', fetch_movie_data, name="movie-info"),
    path('tv-show/<int:tv_show_id>/', fetch_tv_show_data, name="tv_show-info"),
    path('movies/search/', search_movies, name='search_movies'),
]
