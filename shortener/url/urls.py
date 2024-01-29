from django.urls import path
from url.views import RedirectOriginalURLView, URLShortenerAPIView, URLSListView

app_name = 'url'

urlpatterns = [
    path('', URLSListView.as_view(), name='home'),
    path('shorten/', URLShortenerAPIView.as_view(), name='shorten'),
    path('<str:token>/', RedirectOriginalURLView.as_view(), name='redirect_url'),
]
