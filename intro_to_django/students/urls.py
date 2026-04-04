from django.urls import path
from .views import StudentListView, StudentCreateView, LoadTestDataView

urlpatterns = [
    path('', StudentListView.as_view(), name="student_list"),
    path('add/', StudentCreateView.as_view(), name="student_add"),
    path("load-data/", LoadTestDataView.as_view(), name="load_test_data")
]

