from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from markdownx.views import ImageUploadView


class CustomImageUploadView(ImageUploadView):
    def form_valid(self, form):

        response = super(ImageUploadView, self).form_valid(form)
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            image_path = form.save(commit=True)
            image_code = f"[![]({image_path})]({image_path})"
            return JsonResponse({"image_code": image_code})

        return response


def handler404(request, exception=None):
    return redirect(reverse("apps.posts:post_list"))
