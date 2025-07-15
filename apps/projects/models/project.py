from django.db import models


# creating a model
class Project(models.Model):
    # creating some fields
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # creating a relationship to another model
    files = models.ManyToManyField('ProjectFile', related_name='projects')

    # creating a dynamic field to count files
    @property
    def amount_of_files(self):
        return self.files.count()


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']