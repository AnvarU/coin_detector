import os

from django.conf import settings
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import UploadFileForm
from .utils import CoinDetector


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg',])


class UploadFileView(CreateView):
    def post(self, request):
        form = UploadFileForm(request.FILES)
        image_file = form.data.get('image', None)

        if image_file.name and image_file.name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            with open(os.path.join(settings.BASE_DIR, 'media', 'detector', image_file.name), 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
                f.close()

            detector = CoinDetector.predict(
                os.path.join(settings.BASE_DIR, 'media', 'detector', image_file.name), 
                os.path.join(settings.BASE_DIR, 'media', 'detector', 'new_' + image_file.name))
            context = {
                'color1': detector.average_color[0],
                'color2': detector.average_color[1],
                'color3': detector.average_color[2],
                'total_value': detector.total_value,
                'count_coins': detector.count_coins,
                'size': " x ".join(map(str, detector.size))
            }
            return render(request, 'detector/index.html', context)

    def get(self, request):
        return render(request, 'detector/upload.html')
