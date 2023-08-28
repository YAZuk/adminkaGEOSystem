from django.db import models


# from current_user import get_current_user

# Create your models here.


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    imei = models.CharField(max_length=1024, default="", verbose_name=u"IMEI")
    name = models.CharField(max_length=1024, default="", verbose_name=u"Название")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата и время создания")

    class Meta:
        verbose_name_plural = u"Устройства"

    def __str__(self):
        return self.name + ' ' + self.imei


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, default="", verbose_name=u"Название")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата и время создания")

    class Meta:
        verbose_name_plural = u"Компании"

    def __str__(self):
        return self.name


class Transport(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, default="", verbose_name=u"Название")
    vin = models.CharField(max_length=1024, default="", blank=True, null=True, verbose_name=u"VIN номер")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата и время создания")
    transport_img = models.ImageField(upload_to='', default="", blank=True, null=True, verbose_name=u"Изображение")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=u"Компания")
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name=u"Устройство")

    class Meta:
        verbose_name_plural = u"Транспорт"

    # created_by = models.ForeignKey('auth.User', default=get_current_user)

    def __str__(self):
        return self.name


class Act(models.Model):
    id = models.AutoField(primary_key=True)
    executor = models.CharField(max_length=1024, default="", verbose_name=u"Исполнитель")
    # description = models.CharField(max_length=1024, default="", verbose_name=u"Описание работ")
    description = models.TextField(max_length=4095, default="", verbose_name=u"Описание работ")
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name=u"Транспорт")

    class Meta:
        verbose_name_plural = u"Акты"
