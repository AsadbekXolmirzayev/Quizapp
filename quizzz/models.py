from django.db import models
from account.models import Account


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questions = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questions


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=225)
    is_true = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer


class Result(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='quest')
    result = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result}"
