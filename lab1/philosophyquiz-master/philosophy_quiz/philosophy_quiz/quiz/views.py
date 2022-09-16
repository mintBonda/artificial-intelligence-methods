import random as rand
import re

from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserForm

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from quiz.models import User, Question, Answer


class HomePageView(ListView):
    model = User
    template_name = "quiz/homepage.html"


class GateView(ListView):
    model = User
    template_name = "quiz/gate.html"


class UserView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = "quiz/results.html"
    slug_field = "name"


class QuizView(ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = "quiz/quiz.html"

    def get_queryset(self):
        my_ids = list(Question.objects.values_list('id', flat=True))
        rand_ids = rand.sample(my_ids, 15)
        result = Question.objects.filter(id__in=rand_ids)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.session['user']
        return context


class LeaderBoardView(ListView):
    model = User
    context_object_name = 'leaderboard_list'
    template_name = "quiz/leaderboard.html"
    queryset = User.objects.order_by('-score', 'time')


class StartQuiz(View):
    def post(self, request):
        request.session['user'] = request.POST.get("name")
        return redirect("quiz")


class AddResultView(View):
    def post(self, request):
        user_name = request.POST.get("name", None)
        time = (request.POST.get("time", None))

        # получение правильных ответов на вопросы
        queryset = Answer.objects.filter(is_correct=True)
        correct_answers = {}
        for answer in queryset:
            correct_answers[answer.question.id] = answer.id

        # получение ответов от пользователя
        intermediate_dict = dict(request.POST)
        user_answers = {}
        for key in intermediate_dict:
            if re.match(r'q\d', key):
                user_answers_value = [int(num_answer) for num_answer in intermediate_dict[key]]
                user_answers[int(key[1:])] = user_answers_value[0]

        result = 0
        for key in user_answers:
            if key in correct_answers and user_answers[key] == correct_answers[key]:
                result += 1

        user_results = {'name': user_name, 'score': result, 'time': time}

        form = UserForm(user_results)
        if form.is_valid():
            form.save()
            user = User.objects.get(name=user_name)
            return redirect(user.get_absolute_url())
        return redirect("/")
