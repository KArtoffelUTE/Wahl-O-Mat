from rest_framework import serializers
from .models import Question, Parties, Answers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'