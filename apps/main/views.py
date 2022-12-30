from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponse


class MainView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse("apps.posts:post_list"))


def AdsView(request, *args, **kwargs):
    return HttpResponse("google.com, pub-3049139078910304, DIRECT, f08c47fec0942fa0")
