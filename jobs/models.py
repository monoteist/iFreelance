from django.db import models


class Follower(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.email