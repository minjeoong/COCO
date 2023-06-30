from django.db import models

class Town(models.Model):
    townname = models.CharField(max_length = 30, null = False, unique=True)
    usercount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'town'

    def __str__(self):
        return self.townname