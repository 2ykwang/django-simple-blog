from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse("apps.posts:post_list"))
