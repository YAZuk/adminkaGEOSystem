from django.db import models


# from current_user import get_current_user

# Create your models here.


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    imei = models.CharField(max_length=1024, default="")
    name = models.CharField(max_length=1024, default="")
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = u"Устройство"

    def __str__(self):
        return self.name + ' ' + self.imei


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, default="")
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = u"Компания"

    def __str__(self):
        return self.name


class Transport(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, default="")
    vin = models.CharField(max_length=1024, default="")
    add_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = u"Транспорт"

    # created_by = models.ForeignKey('auth.User', default=get_current_user)

    def __str__(self):
        return self.name
