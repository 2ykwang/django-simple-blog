from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from markdownx.views import ImageUploadView


class CustomImageUploadView(ImageUploadView):
    def form_valid(self, form):

        response = super(ImageUploadView, self).form_valid(form)
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            image_path = form.save(commit=True)
            image_code = f'[![]({image_path}){{loading="lazy"}}]({image_path})'
            return JsonResponse({"image_code": image_code})

        return response


class CustomHandler404(View):
    def get(self, request, *args, **kwargs):
        return render(request, "errors/404.html", status=404)
