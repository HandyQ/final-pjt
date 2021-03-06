from rest_framework import serializers
from .models import Movies, Rating
from reviews.serializers import ReviewSerializer

class RatingSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rating
        fields = (
            'id',
            'user_id',
            'movie_id',
            'grade',
            'content',
            'created_at',
            'updated_at',
            'user_name',
        )

class MovieSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(read_only=True, many=True)
    rating_count = serializers.IntegerField(source='rating_set.count', read_only=True)

    review_set = ReviewSerializer(read_only=True, many=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Movies
        fields = (
            'id',
            'title',
            'genre',
            'overview',
            'poster_path',
            'release_date',
            'vote_average',
            'vote_count',
            'popularity',
            'rating_set',
            'rating_count',
            'review_set',
            'review_count'
        )
