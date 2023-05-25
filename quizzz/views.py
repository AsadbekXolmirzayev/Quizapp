import profile

import jwt
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Question, Answers, Result
from .serializers import CategorySerializer, QuestionGETSerializer, ResultSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionGETSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs['category_id']
        queryset = queryset.filter(category_id=category_id)
        return queryset


class AnswerApiView(APIView):

    def post(self, request, *args, **kwargs):
        author_id = request.user.id
        category_id = request.data.get('category_id')
        questions = request.data.get('questions')
        result = Result.objects.create(category_id=category_id, author_id=author_id)
        count = 0
        for i in questions:
            question_id = int(i.get('question_id'))
            answer_id = int(i.get('answers_id'))
            try:
                question = Question.objects.get(id=question_id)
                answer = Answers.objects.get(id=answer_id)
            except (Question.DoesNotExist, Answers.DoesNotExist):
                break

            if answer.is_true:
                count += 20
            result.questions.add(question)
        result.result = count
        result.save()
        return Response("Result was saved")
