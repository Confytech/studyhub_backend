# apps/study/views.py
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Lesson, Quiz, QuizAttempt
from .serializers import (
    LessonSerializer,
    LessonDetailSerializer,
    QuizAttemptSerializer,
    QuizResultSerializer,
)

# ----------------------------------
# Home page view
# ----------------------------------
def home(request):
    return JsonResponse({
        "message": "Welcome to Confidence StudyHub!",
        "endpoints": {
            "users": "/api/users/",
            "study": {
                "lessons": "/api/study/lessons/",
                "lesson_detail": "/api/study/lessons/<id>/",
                "quiz_submit": "/api/study/quizzes/<quiz_id>/submit/",
            },
            "payments": "/api/payments/"
        }
    })

# ----------------------------------
# List all lessons (STEP 4 ✅)
# GET /api/study/lessons/
# ----------------------------------
class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.select_related("topic").prefetch_related("quizzes")
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

# ----------------------------------
# Lesson detail + quizzes
# GET /api/study/lessons/<id>/
# ----------------------------------
class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.select_related("topic").prefetch_related("quizzes")
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated]

# ----------------------------------
# Quiz submission API (STEP 4 ✅)
# POST /api/study/quizzes/<quiz_id>/submit/
# ----------------------------------
class SubmitQuizAttemptView(generics.CreateAPIView):
    serializer_class = QuizAttemptSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        quiz_id = kwargs.get("quiz_id")
        selected_option = request.data.get("selected_option")

        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------
        # Premium check
        # ----------------------------------
        if quiz.is_premium:
            if user.coins < quiz.coin_cost:
                return Response(
                    {"error": "Not enough coins"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.coins -= quiz.coin_cost
            user.save()

        # ----------------------------------
        # Mark result
        # ----------------------------------
        is_correct = (selected_option == quiz.correct_option)

        attempt, created = QuizAttempt.objects.update_or_create(
            user=user,
            quiz=quiz,
            defaults={
                "selected_option": selected_option,
                "is_correct": is_correct,
                "coins_spent": quiz.coin_cost if quiz.is_premium else 0,
                "reward_coins_earned": quiz.reward_coins if is_correct else 0,
            }
        )

        # Reward coins if correct
        if is_correct and quiz.reward_coins:
            user.coins += quiz.reward_coins
            user.save()

        serializer = QuizResultSerializer(attempt)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )

