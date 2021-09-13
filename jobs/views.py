
from jobs.models import Follower
from django.http.response import HttpResponse
from django.views import View
from .scrapping import habr_parsing
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework import generics
from .serializers import FollowersSerializer

class HomePageView(View):
    def get(self, request):
        jobs = habr_parsing('python')
        return render(request, 'index.html', {'jobs': jobs})

    def post(self, request):
        email = request.POST.get('email')
        f = Follower.objects.filter(email=email)
        if f:
            return HttpResponse('Такой email уже сущетвует!')
        if email:
            f = Follower(email=email)
            f.save()
        return redirect('index')


def jobs(request):
    jobs = habr_parsing('python')
    return JsonResponse({'jobs': jobs})

class FollowerListView(generics.ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowersSerializer

class FollowerDetailView(generics.RetrieveAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowersSerializer



# def get_followers(request):
#     followers = Follower.objects.all()
#     print(followers)
#     return JsonResponse(
#         {'followers': [{'email': f.email} for f in followers]}
#     )


