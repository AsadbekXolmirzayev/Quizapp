from django.urls import path
from . import views


urlpatterns = [
    path('category_list/', views.CategoryListAPIView.as_view()),
    path('question_list/<int:category_id>/', views.QuestionListAPIView.as_view()),
    path('answer/', views.AnswerApiView.as_view()),
]
