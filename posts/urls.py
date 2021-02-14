from django.urls import path

from . import views

urlpatterns = [
    path("", views.CoursesView.as_view()),
    path("filter/", views.FilterCoursesView.as_view(), name='filter'),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="courses_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]