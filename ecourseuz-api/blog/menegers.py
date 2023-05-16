from django.db import models
from django.db.models import Count


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            comment_count=Count('comment'),
            view_count=Count('view')
        )
