from django.db import models


# creating a model
class ProjectFile(models.Model):
    # creating some fields
    file_name = models.CharField(max_length=120)
    file_path = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file_name


    class Meta:
        ordering = ['-created_at']