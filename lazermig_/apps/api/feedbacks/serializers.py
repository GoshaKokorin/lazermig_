from rest_framework import serializers

from lazermig_.apps.feedbacks.models import FeedbackCall, FeedbackQuestion


class FeedbackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackCall
        fields = ['name', 'number']


class FeedbackQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackQuestion
        fields = ['name', 'number', 'text']
