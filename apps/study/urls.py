# apps/study/urls.py
from django.urls import path
from .views import (
    home,
    LessonListView,
    LessonDetailView,
    SubmitQuizAttemptView,
)

urlpatterns = [
    # Home
    path('', home, name='home'),

    # STEP 4 — Lessons & Quizzes
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    # Quiz submission
    path('quizzes/<int:quiz_id>/submit/', SubmitQuizAttemptView.as_view(), name='submit-quiz'),
]

