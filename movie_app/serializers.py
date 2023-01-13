from rest_framework import serializers
from movie_app.models import *


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movie_count')

    def get_movie_count(self, director):
        return director.movie_count


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie')


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_reviews(self, movie):
        return [i.stars for i in movie.reviews.all()]

    def get_rating(self, movie):
        return movie.rating


class DirectorsCreateSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class MovieValidatorsCreate(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(min_length=1)
    duration = serializers.IntegerField(min_value=1)
    director_id = serializers.IntegerField(min_value=1)


class MovieDetailValidatorCreate(MovieValidatorsCreate):
    pass


class ReviewValidatorCreate(serializers.Serializer):
    text = serializers.CharField(min_length=2)
    movie_id = serializers.IntegerField(min_value=1)


class DirectorValidatorCreate(serializers.Serializer):
    name = serializers.CharField(max_length=150)
