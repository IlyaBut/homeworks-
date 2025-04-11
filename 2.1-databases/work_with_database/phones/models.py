from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length= 100, verbose_name="Модель")
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)