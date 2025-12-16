# apps/study/serializers.py
from rest_framework import serializers
from .models import Lesson, Quiz, QuizAttempt

# ----------------------------------
# Quiz serializers
# ----------------------------------
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "id",
            "question",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "is_premium",
            "coin_cost",
            "reward_coins"
        ]

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ["id", "quiz", "selected_option"]

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ["quiz", "selected_option", "is_correct", "coins_spent", "reward_coins_earned"]

# ----------------------------------
# Lesson serializers
# ----------------------------------
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "order"]

class LessonDetailSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "order", "quizzes"]

