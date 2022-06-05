from django.shortcuts import render
from django.views.generic import View


class MainView(View):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
