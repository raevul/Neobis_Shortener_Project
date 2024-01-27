from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Url
from .serializers import UrlSerializer


class UrlShortenerAPIView(ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlShortenerCreateAPIView(CreateAPIView):
    serializer_class = UrlSerializer


class Redirector(View):
    def get(self, request, short_url, *args, **kwargs):
        short_url = settings.HOST_URL + '/' + self.kwargs['short_url']
        redirect_link = Url.objects.filter(short_url=short_url).first().long_url
        return redirect(redirect_link)
