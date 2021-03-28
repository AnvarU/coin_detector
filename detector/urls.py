from django.urls import path
from django.conf.urls.static import static

from .views import UploadFileView


urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
]