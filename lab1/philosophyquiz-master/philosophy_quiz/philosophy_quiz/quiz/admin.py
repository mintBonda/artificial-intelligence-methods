from django.contrib import admin
from django.forms import TextInput, Textarea

from .models import User, Question, Answer
# Register your models here.
from django.db import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "score", "date", "time")
    readonly_fields = ("name", "score", "date", "time")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.CharField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40, 'size': '24'})},
    }


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "is_correct", "question")
    list_display_links = ("question",)


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

