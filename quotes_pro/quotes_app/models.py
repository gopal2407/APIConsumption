from django.db import models


class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"ID: {self.id} - {self.author}: {self.quote}"
