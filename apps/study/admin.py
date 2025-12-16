from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Subject, Topic, Lesson, Quiz
from .resources import (
    SubjectResource,
    TopicResource,
    LessonResource,
    QuizResource,
)


@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    resource_class = SubjectResource
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    resource_class = TopicResource
    list_display = ("title", "subject")
    list_filter = ("subject",)
    search_fields = ("title",)


@admin.register(Lesson)
class LessonAdmin(ImportExportModelAdmin):
    resource_class = LessonResource
    list_display = ("title", "topic", "order")
    list_filter = ("topic",)
    search_fields = ("title",)


@admin.register(Quiz)
class QuizAdmin(ImportExportModelAdmin):
    resource_class = QuizResource
    list_display = ("question", "lesson", "is_premium", "coin_cost")
    list_filter = ("is_premium",)
    search_fields = ("question",)

