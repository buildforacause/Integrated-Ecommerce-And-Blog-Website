from django.db import models


# Create your models here.
class BlogPost(models.Model):
    post_title = models.CharField(max_length=350)
    post_author = models.CharField(max_length=50)
    post_pub_date = models.DateField()
    post_content = models.CharField(max_length=5000000)
    image = models.ImageField(upload_to="blog/images", default="")
    post_genre = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.post_title
