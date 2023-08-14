from django.db import models

class Category(models.Model):
    name = models.CharField('Name', max_length=50)
    parent = models.ForeignKey('city_directory.category', related_name='child', on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name