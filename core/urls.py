from django.urls import path
from .views import QuestionListView, PartyListView, AnswerListView, PartyCreateView, AnswerCreateView, AnalyzeView, QuestionCreateView



urlpatterns = [
    path('fragen/', QuestionListView.as_view()),
    path('fragen/create/', QuestionCreateView.as_view()),
    path('parteien/', PartyListView.as_view()),
    path('parteien/antworten/', AnswerListView.as_view()),
    path('parteien/create/', PartyCreateView.as_view()),
    path('parteien/create/answer/', AnswerCreateView.as_view()),
    path('analyze/', AnalyzeView.as_view()),
]
