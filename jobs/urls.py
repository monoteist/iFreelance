from django.urls import path
from .views import HomePageView, jobs, FollowerListView, FollowerDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('api/v1/jobs/', jobs, name='jobs'),
    #path('api/v1/followers/', get_followers, name='get_followers')
    path('api/v1/followers/', FollowerListView.as_view(), name='get_followers'),
    path('api/v1/followers/<int:pk>', FollowerDetailView.as_view())

]
