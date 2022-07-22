from django.contrib import admin

from posts.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "slug", "created_at")
    fields = ("author", "title", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")
    raw_id_fields = ("author",)


class Tag(models.Model):
    title = models.CharField(max_lenght=100)
    posts = models.ManyToManyField(Post)

    def__str__(self):
        return f"Tag: "