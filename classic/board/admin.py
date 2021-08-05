from django.contrib import admin
from board.models import Question, Answer


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
