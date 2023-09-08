from rest_framework import serializers

from lazermig_.apps.news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['title', 'slug', 'image', 'short_description', 'tags']


class NewsDetailSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    related_news = NewsListSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['title', 'slug', 'image', 'description', 'tags', 'date', 'related_news']

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        queryset = News.objects.filter(is_active=True).exclude(id=obj.id)[:3]
        serializer = NewsListSerializer(queryset, many=True)
        ret['related_news'] = serializer.data
        return ret
