from django.db import models
from app_users.models import Users


class Posts(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'Posts'


class Comments(models.Model):
    commenter = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'Comments'


class PostLikes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "PostLikes"


class CommentLikes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'CommentLikes'
