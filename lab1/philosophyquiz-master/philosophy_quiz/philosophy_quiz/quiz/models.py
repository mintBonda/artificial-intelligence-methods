
from django.db import models
from datetime import date

from django.urls import reverse


class User(models.Model):
    name = models.CharField("Имя", max_length=30)
    score = models.PositiveSmallIntegerField("Баллы", default=0)
    date = models.DateField("Дата", default=date.today)
    time = models.TimeField("Время", default='14:30')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("quiz_results", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Question(models.Model):
    title = models.CharField("Название", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def answers(self):
        answer = Answer.objects.filter(question=self)
        return answer


class Answer(models.Model):
    text = models.CharField("Текст вопроса", max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
