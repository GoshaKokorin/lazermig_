from rest_framework import serializers

from lazermig_.apps.news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['title', 'slug', 'image', 'short_description', 'tags']


class NewsDetailSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['title', 'slug', 'image', 'description', 'tags', 'date']
