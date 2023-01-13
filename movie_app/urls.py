from django.contrib import admin
from django.urls import path, include
from movie_app.views import *

urlpatterns = [
    path('directors/', directors_view),
    path('directors/<int:id>/', director_detail_view),
    path('movies/', movies_view),
    path('movies/<int:id>/', movie_detail_view),
    path('reviews/', reviews_view),
    path('reviews/<int:id>/', review_detail_view),
    path('movies/reviews/', review_movies_view),

]