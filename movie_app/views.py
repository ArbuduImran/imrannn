from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import *
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def directors_view(request):
    print(request.user)
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DirectorValidatorCreate(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        director = Director.objects.create(**serializer.validated_data)
        director.save()
        return Response(data=DirectorSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorValidatorCreate(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get("name")
        director.save()
        return Response(data={'message': 'data received!',
                              'movie': DirectorSerializer(director).data})


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        print(request.user)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = MovieValidatorsCreate(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        movie = Movie.objects.create(**serializer.validated_data)
        movie.save()
        return Response(data=MovieSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieDetailValidatorCreate(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        movie.save()
        return Response(data={'message': 'data received!',
                              'movie': MovieSerializer(movie).data})


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ReviewValidatorCreate(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        review = Review.objects.create(**serializer.validated_data)
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewValidatorCreate(data=request.data)
        serializer.is_valid(raise_exception=1)
        review.text = serializer.validated_data.get("text")
        review.movie_id = serializer.validated_data.get("movie_id")
        review.save()
        return Response(data={'message': 'data received!',
                              'review': ReviewSerializer(review).data})


@api_view(["GET"])
def review_movies_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)