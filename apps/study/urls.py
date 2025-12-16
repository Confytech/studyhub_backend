# apps/study/urls.py
from django.urls import path
from .views import home, SubmitQuizAttemptView  # remove LessonListView, LessonDetailView

urlpatterns = [
    path('', home, name='home'),
    path('quizzes/<int:quiz_id>/submit/', SubmitQuizAttemptView.as_view(), name='submit-quiz'),
]

