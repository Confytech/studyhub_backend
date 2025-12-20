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
            "lessons": "/api/study/lessons/",
            "lesson_detail": "/api/study/lessons/<id>/",
            "quiz_detail": "/api/study/quizzes/<id>/",
            "quiz_submit": "/api/study/quizzes/<quiz_id>/submit/",
        }
    })

# ----------------------------------
# List all lessons
# GET /api/study/lessons/
# ----------------------------------
class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

# ----------------------------------
# Lesson detail + quizzes
# GET /api/study/lessons/<id>/
# ----------------------------------
class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related("quizzes")
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated]

# ----------------------------------
# Quiz detail (FIXES 404)
# GET /api/study/quizzes/<id>/
# ----------------------------------
class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        quiz = self.get_object()
        return Response({
            "id": quiz.id,
            "question": quiz.question,
            "option_a": quiz.option_a,
            "option_b": quiz.option_b,
            "option_c": quiz.option_c,
            "option_d": quiz.option_d,
            "is_premium": quiz.is_premium,
            "coin_cost": quiz.coin_cost,
            "reward_coins": quiz.reward_coins,
        })

# ----------------------------------
# Quiz submission
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
            return Response({"error": "Quiz not found"}, status=404)

        # Premium check
        if quiz.is_premium:
            if user.coins < quiz.coin_cost:
                return Response({"error": "Not enough coins"}, status=400)
            user.coins -= quiz.coin_cost
            user.save()

        is_correct = selected_option == quiz.correct_option

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

        if is_correct and quiz.reward_coins:
            user.coins += quiz.reward_coins
            user.save()

        return Response(
            QuizResultSerializer(attempt).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )

