from import_export import resources
from .models import Subject, Topic, Lesson, Quiz

# -------------------------------
# Subject Resource
# -------------------------------
class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'slug')
        export_order = ('id', 'name', 'slug')

# -------------------------------
# Topic Resource
# -------------------------------
class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'subject', 'description', 'is_premium')
        export_order = ('id', 'title', 'subject', 'description', 'is_premium')

# -------------------------------
# Lesson Resource
# -------------------------------
class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'topic', 'content', 'order')
        export_order = ('id', 'title', 'topic', 'content', 'order')

# -------------------------------
# Quiz Resource
# -------------------------------
class QuizResource(resources.ModelResource):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'is_premium', 'coin_cost', 'reward_coins')
        export_order = ('id', 'lesson', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'is_premium', 'coin_cost', 'reward_coins')

