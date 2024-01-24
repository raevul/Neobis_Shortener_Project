from rest_framework.response import Response
from rest_framework.views import APIView


class UrlAPIView(APIView):
    developers = {
        'name': 'ular',
        'age': 22,
    }

    def get(self, request):
        return Response(self.developers)
