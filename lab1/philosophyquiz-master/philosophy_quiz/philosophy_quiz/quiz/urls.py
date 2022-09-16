from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("quiz/", views.QuizView.as_view(), name="quiz"),
    path("quiz/leaderboard/", views.LeaderBoardView.as_view(), name="leaderboard"),
    path("gate/", views.GateView.as_view(), name="gate"),
    path("start_quiz/", views.StartQuiz.as_view(), name="start_quiz"),
    path("add_result/", views.AddResultView.as_view(), name="add_result"),
    path("quiz/<str:slug>/", views.UserView.as_view(), name="quiz_results"),


]
