from django.db import models

class PdfExtraModel(models.Model):
    type = models.CharField(max_length=125,null=True)
    file = models.FileField()
    format = models.CharField(max_length=125,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    result = models.TextField(null=True)



