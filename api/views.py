from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    def get(self, request, format=None):
        content = {
            "user": str(request.user),
        }
        return Response(content)
