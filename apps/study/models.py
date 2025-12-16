from django.db import models
from django.conf import settings

# ----------------------------------
# USER MODEL
# ----------------------------------
User = settings.AUTH_USER_MODEL

# ----------------------------------
# SUBJECT
# ----------------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# ----------------------------------
# TOPIC
# ----------------------------------
class Topic(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="topics"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject.name} - {self.title}"

# ----------------------------------
# LESSON
# ----------------------------------
class Lesson(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.topic.title} - {self.title}"

# ----------------------------------
# QUIZ
# ----------------------------------
class Quiz(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="quizzes"
    )
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(
        max_length=1,
        choices=[
            ("A", "Option A"),
            ("B", "Option B"),
            ("C", "Option C"),
            ("D", "Option D"),
        ]
    )
    is_premium = models.BooleanField(default=False)
    coin_cost = models.PositiveIntegerField(default=0)
    reward_coins = models.PositiveIntegerField(default=0)  # coins earned for correct answer

    def __str__(self):
        return self.question[:50]

# ----------------------------------
# QUIZ ATTEMPT
# ----------------------------------
class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz_attempts")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")
    selected_option = models.CharField(max_length=1)
    is_correct = models.BooleanField()
    coins_spent = models.PositiveIntegerField(default=0)
    reward_coins_earned = models.PositiveIntegerField(default=0)
    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "quiz")  # ensures one attempt per user per quiz
        ordering = ["-attempted_at"]

    def __str__(self):
        return f"{self.user} → {self.quiz.id} ({'✔' if self.is_correct else '✘'})"

