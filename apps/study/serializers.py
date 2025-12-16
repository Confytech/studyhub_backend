# apps/study/serializers.py
from rest_framework import serializers
from .models import Lesson, Quiz, QuizAttempt

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ["id", "quiz", "selected_option"]

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ["quiz", "selected_option", "is_correct", "coins_spent"]

