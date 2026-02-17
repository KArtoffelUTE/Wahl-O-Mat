from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Question, Parties, Answers
from .serializers import QuestionSerializer, PartySerializer, AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class PartyListView(ListAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartySerializer

class AnswerListView(ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

class PartyCreateView(CreateAPIView):
     queryset = Parties.objects.all()
     serializer_class = PartySerializer

class AnswerCreateView(CreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

class QuestionCreateView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnalyzeView(APIView):
    def post(self, request):
        user_answer = request.data
        parties = Parties.objects.all()
        results = []
        total_questions = len(user_answer)

        for party in parties:
            party_answers = Answers.objects.filter(party=party)
            score = 0

            for pa in party_answers:
                qid = str(pa.question.id)   # Note: Könnte Fehler verursachen, wenn user_answer keys int sind, dann einfach ohne str() verwenden
                if qid in user_answer:
                    user_value = user_answer[qid]
                    party_value = pa.answer
                    score += 1 - abs(user_value - party_value) / 2
            percent = (score / total_questions) * 100
            percent = round(percent, 2)


            results.append({'party': party.name, 'score': percent})

        results.sort(key=lambda x: x['score'], reverse=True)
        return Response(results)