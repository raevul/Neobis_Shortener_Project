from django.urls import path
from url.views import RedirectOriginalURLView, URLShortenerAPIView, URLSListView

app_name = 'url'

urlpatterns = [
    path('', URLSListView.as_view()),
    path('shorten/', URLShortenerAPIView.as_view()),
    path('<str:token>/', RedirectOriginalURLView.as_view()),
]
