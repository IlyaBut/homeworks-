from django.db import models

# Создаем таблицу тегов.
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название тега")

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    # Добавляем отношение М2м.
    tags = models.ManyToManyField(Tag, related_name="article", through ="Scope")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


# Создаем промежуточную таблицу. Таблица-связка Scope
class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="scopes")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="scopes")
    is_main = models.BooleanField(default = False, verbose_name="основной тэг")


