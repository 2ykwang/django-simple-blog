from django.http import JsonResponse
from markdownx.views import ImageUploadView


class CustomImageUploadView(ImageUploadView):
    def form_valid(self, form):

        response = super(ImageUploadView, self).form_valid(form)
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            image_path = form.save(commit=True)
            image_code = f"[![]({image_path})]({image_path})"
            return JsonResponse({"image_code": image_code})

        return response
