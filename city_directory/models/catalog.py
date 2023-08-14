from django.db import models

class Catalog(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.CharField('Description', max_length=150)
    address = models.CharField('Address', max_length=120)
    city = models.CharField('City', max_length=50)
    category = models.ForeignKey('city_directory.category', on_delete=models.CASCADE, related_name='catalogs')
    contact = models.ForeignKey('city_directory.contact', on_delete=models.CASCADE, related_name='catalogs')


    class Meta:
        ordering = ['name', 'city']
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'

    def __str__(self) -> str:
        return self.name