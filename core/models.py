from django.db import models


class CoreModel(models.Model):
    class Meta:
        abstract = True

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
