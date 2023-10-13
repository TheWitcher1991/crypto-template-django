from django.http import JsonResponse
from django.views import View


class IndexProc(View):
    def post(self, request):
        return JsonResponse(data={}, status=200)
