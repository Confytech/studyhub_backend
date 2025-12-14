from django.contrib import admin
from .models import Subject, Topic, Lesson, Quiz

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject")
    list_filter = ("subject",)
    search_fields = ("title",)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "order")
    list_filter = ("topic",)
    search_fields = ("title",)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("question", "lesson", "is_premium", "coin_cost")
    list_filter = ("is_premium",)
    search_fields = ("question",)

