from django.db import models


class Pronounce(models.Model):
    pronounce = models.CharField(max_length=168)
    chineses = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.pronounce
