from django.db import models

# Create your models here.
def user_directory_path(instance,filename):
    return 'image/{0}'.format(filename)
TYPE_CHOICES = [
    ('web','Web development'),
    ('mobile','Mobile development'),
    ('ml','Machine Learning'),
    ('ta','Task Automatization'),

]

class DataCard(models.Model):
    image = models.ImageField(upload_to=user_directory_path, default='image/myimage.jpg')
    titleApp = models.CharField(max_length=50)
    shortDescription = models.CharField(max_length=50)
    longDescription = models.CharField(max_length=160)
    githubLink = models.CharField(max_length=200)
    youtubeLink = models.CharField(max_length=200)
    launchLink = models.CharField(max_length=200)
    date = models.DateField(auto_created=True)
    appType = models.CharField(max_length=20, choices=TYPE_CHOICES, default="web")

    def __str__(self):
        return f'{self.titleApp}'
