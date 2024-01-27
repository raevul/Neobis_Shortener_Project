from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from rest_framework import status

from .models import URL
from .serializers import URLSerializer
from .shortener import Shortener


class URLSListView(ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class RedirectOriginalURLView(APIView):
    def get(self, request, token):
        short_link = URL.objects.filter(short_link=token)[0]
        return redirect(short_link.long_link)


class URLShortenerAPIView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)

        if serializer.is_valid():
            new_url = serializer.save()
            token = Shortener().generate_token()
            new_url.short_link = token
            new_url.save()
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

