from django.db import models


class ChineseWord(models.Model):
    word = models.CharField(max_length=168)
    pronounce = models.CharField(max_length=168)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.word
