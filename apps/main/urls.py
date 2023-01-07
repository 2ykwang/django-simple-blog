from django.urls import path

from .apps import MainConfig as Config
from .views import AdsView, MainView

app_name = Config.name

urlpatterns = [
    path("", MainView.as_view(), name="main_index"),
    path("ads.txt", AdsView, name="ads"),
]
