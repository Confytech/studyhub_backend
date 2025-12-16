from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Subject, Topic, Lesson, Quiz
from .resources import SubjectResource, TopicResource, LessonResource, QuizResource

# -------------------------------
# Subject Admin
# -------------------------------
@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    resource_class = SubjectResource
    list_display = ("name", "slug")
    search_fields = ("name", "slug")

# -------------------------------
# Topic Admin
# -------------------------------
@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    resource_class = TopicResource
    list_display = ("title", "subject", "is_premium")
    list_filter = ("subject", "is_premium")
    search_fields = ("title", "subject__name")

# -------------------------------
# Lesson Admin
# -------------------------------
@admin.register(Lesson)
class LessonAdmin(ImportExportModelAdmin):
    resource_class = LessonResource
    list_display = ("title", "topic", "order")
    list_filter = ("topic",)
    search_fields = ("title", "topic__title")

# -------------------------------
# Quiz Admin
# -------------------------------
@admin.register(Quiz)
class QuizAdmin(ImportExportModelAdmin):
    resource_class = QuizResource
    list_display = ("question", "lesson", "is_premium", "coin_cost", "reward_coins")
    list_filter = ("is_premium", "lesson")
    search_fields = ("question", "lesson__title")

