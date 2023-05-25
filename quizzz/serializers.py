from rest_framework import serializers
from .models import Category, Question, Answers, Result


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class MiniAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'answer', 'created_date')


class QuestionGETSerializer(serializers.ModelSerializer):
    answers = MiniAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'category', 'questions', 'answers', 'created_date')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'author', 'category', 'questions', 'result', 'created_date')
