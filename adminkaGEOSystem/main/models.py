from django.db import models


# from current_user import get_current_user

# Create your models here.

class Transport(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, default="")
    vin = models.CharField(max_length=1024, default="")
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Транспорт"

    # created_by = models.ForeignKey('auth.User', default=get_current_user)

    def __str__(self):
        return self.name
