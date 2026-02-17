from django.contrib import admin

# Register your models here.

from .models import Question, Parties, Answers

admin.site.register(Question)
admin.site.register(Parties)
admin.site.register(Answers)
