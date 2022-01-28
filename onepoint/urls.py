from django import views
from django.urls import path
from .views import NewJoinerGradeView, JoiningDateView

urlpatterns = [
    path('grade/',NewJoinerGradeView.as_view(), name='grades'),
    path('grade/<int:PSID>/', NewJoinerGradeView.as_view(), name='grade'),
    path('joining_date/<int:PSID>/', JoiningDateView.as_view(), name='joining_date'),
]