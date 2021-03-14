from django import forms
from reviews.models import Review

class CreateReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = (
      "text",
      "rating",
    )
  def save(self, *args, **kwargs):
    review = super().save(commit=False)
    return review