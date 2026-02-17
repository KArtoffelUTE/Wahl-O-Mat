from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Parties(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
     # logo-url = models.URLField(default='/static/images/default-logo.png') kommt eventuell später

    def __str__(self):
        return self.name

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)
    answer = models.IntegerField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.party.name} - {self.question}: {self.answer}"