from django.core.validators import FileExtensionValidator, validate_image_file_extension
from django.forms import Form, FileField


class UploadFileForm(Form):
    image = FileField(validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg',])])

    # def __init__(self, file_data):
    #     self.image = file_data.get('image', None)
    #     return super(UploadFileForm, self).__init__(file_data)