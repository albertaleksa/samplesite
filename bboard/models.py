from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published date')

    class Meta:
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'
        ordering = ['-published']
