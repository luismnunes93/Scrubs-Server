from rest_framework import generics, permissions


from polls.serializer import QuestionSerializer, ChoiceSerializer
from polls.models import Question, Choice


class QuestionList(generics.ListCreateAPIView):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ChoiceList(generics.ListCreateAPIView):
    model = Choice
    queryset = Choice.objects.filter(question__question_text__contains='up?')
    serializer_class = ChoiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]
