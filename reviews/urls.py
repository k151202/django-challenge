from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
  path("book/create/<int:pk>", views.CreateBookReview.as_view(), name="book"),
  path("movie/create/<int:pk>", views.CreateMovieReview.as_view(), name="movie"),
  path("<int:review_pk>/delete/<int:pk>", views.delete, name="delete"),
  ]