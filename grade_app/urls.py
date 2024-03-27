from django.urls import path
from .views import Grades, All_grades

urlpatterns = [
    path("", All_grades.as_view(), name="all_grades"),
    path("<int:id>/", Grades.as_view(), name="grades"),
]