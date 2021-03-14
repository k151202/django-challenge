from django.views.generic import CreateView
from django.shortcuts import redirect, reverse
from books.models import Book
from movies.models import Movie
from . import forms, models

class CreateBookReview(CreateView):
  model = Book
  form_class = forms.CreateReviewForm

  def form_valid(self, form):
    pk = self.kwargs.get("pk")
    book = Book.objects.get_or_none(pk=pk)
    review = form.save(pk)
    review.created_by = self.request.user
    review.book = book
    review.save()

    return redirect(reverse("books:book", kwargs={"pk": pk}))

class CreateMovieReview(CreateView):
  model = Movie
  form_class = forms.CreateReviewForm
  
  def form_valid(self, form):
    pk = self.kwargs.get("pk")
    movie = Movie.objects.get_or_none(pk=pk)
    review = form.save()
    review.created_by = self.request.user
    review.movie = movie
    review.save()

    return redirect(reverse("movies:movie", kwargs={"pk": pk}))

def delete(request, review_pk, pk):
  kind = request.GET.get("kind")
  if kind == "movie":
    models.Review.objects.filter(pk=review_pk).delete()
    return redirect(reverse("movies:movie", kwargs={"pk": pk}))
  elif kind == "book":
    models.Review.objects.filter(pk=review_pk).delete()
    return redirect(reverse("books:book", kwargs={"pk": pk}))
  else:
    return redirect(reverse("core:home"))

