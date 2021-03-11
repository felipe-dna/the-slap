from django.db import models


class Post(models.Model):
    content = models.TextField(max_length=500)
    emotion = models.CharField(max_length=100)

    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
