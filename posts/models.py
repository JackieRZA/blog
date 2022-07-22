
from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True,
        null=True
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        string = "<p>{0}) Title: {1}, Slug: {2}, Test: {3}, Created at: {4}</p>"
        output = string.format(self.id, self.title, self.slug, self.text, self.created_at)
        return output


class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f"Tag {self.title} with {self.posts.count()} post(s)"