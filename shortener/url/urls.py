from django.urls import path
from url.views import UrlShortenerAPIView, UrlShortenerCreateAPIView

app_name = 'url'


urlpatterns = [
    path('url/', UrlShortenerAPIView.as_view()),
    path('create/', UrlShortenerCreateAPIView.as_view()),
]
