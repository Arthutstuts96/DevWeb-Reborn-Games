from django.urls import include, path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('', ReviewListView.as_view(), name='list'),
    path('criar/', CreateReview.as_view(), name="create-review"),
]