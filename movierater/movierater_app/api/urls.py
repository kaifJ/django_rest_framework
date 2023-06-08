from django.urls import path
# from movierater_app.api.views import movie_list, movie_details
from movierater_app.api.views import WatchListAV, WatchListDetailsAV, StreamPlatformAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie_list"),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='movie_detail'),
    path("stream/", StreamPlatformAV.as_view(), name="stream")
]
