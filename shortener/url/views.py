from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework import status
from django.conf import settings

from .models import URL
from .serializers import URLSerializer
from .shorten import Shortener


class URLSListView(APIView):
    def get(self, request):
        urls = URL.objects.all()
        return Response({'urls': URLSerializer(urls, many=True).data})

# class URLSListView(APIView):
#     def get(self, request):
#         urls = URL.objects.all()
#         short_links = [url.short_link for url in urls]
#         short_urls = map(lambda x: settings.HOST_URL + str(x), short_links)
#         return Response({'short_links': short_urls})


class RedirectOriginalURLView(APIView):
    def get(self, request, token):
        try:
            short_link = URL.objects.filter(short_link=token)[0]
            return redirect(short_link.long_link)
        except URL.DoesNotExist:
            return status.HTTP_404_NOT_FOUND


class URLShortenerAPIView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)

        if serializer.is_valid():
            new_url = serializer.save()
            token = Shortener().generate_token()
            new_url.short_link = token
            new_url.save()
            return Response({'short_link': settings.HOST_URL + token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

