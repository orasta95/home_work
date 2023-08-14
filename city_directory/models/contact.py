from django.db import models

class Contact(models.Model):
    phone = models.CharField('Phone number', max_length=12)
    second_phone = models.CharField('Phone number', max_length=12)
    mail = models.EmailField('Email')
    photo = models.ImageField('Photo', upload_to='city_directory.Image', height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['mail']

    def __str__(self) -> str:
        return self.mail