from import_export import resources
from .models import Subject, Topic, Lesson, Quiz


class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject


class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic


class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson


class QuizResource(resources.ModelResource):
    class Meta:
        model = Quiz

