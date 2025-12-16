# apps/study/views.py
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Quiz, QuizAttempt
from .serializers import QuizAttemptSerializer, QuizResultSerializer

# ----------------------------------
# Home page view
# ----------------------------------
def home(request):
    return JsonResponse({
        "message": "Welcome to Confidence StudyHub!",
        "endpoints": {
            "users": "/api/users/",
            "study": "/api/study/",
            "payments": "/api/payments/"
        }
    })

# ----------------------------------
# Quiz submission API
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
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check premium & coins
        if quiz.is_premium and user.coins < quiz.coin_cost:
            return Response({"error": "Not enough coins"}, status=status.HTTP_400_BAD_REQUEST)

        if quiz.is_premium:
            user.coins -= quiz.coin_cost
            user.save()

        is_correct = (selected_option == quiz.correct_option)

        attempt, created = QuizAttempt.objects.update_or_create(
            user=user,
            quiz=quiz,
            defaults={"selected_option": selected_option, "is_correct": is_correct}
        )

        serializer = QuizResultSerializer(attempt)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

