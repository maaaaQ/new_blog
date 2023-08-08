from django.db import models

# Create your models here.


class Post(models.Model):
    """модель данных о записи"""

    title = models.CharField("Заголовок записи", max_length=100)
    descriptions = models.TextField("Текс записи")
    autor = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публикации записи")
    image = models.ImageField("Изображение", upload_to="image/%Y")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.title}, {self.autor}"


class Comments(models.Model):
    """комментарии"""

    email = models.EmailField()
    name = models.CharField("Имя", max_length=50)
    text_comments = models.TextField("Текст комментария", max_length=5000)
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.name}, {self.post}"


class Likes(models.Model):
    """хранения лайков/дизлайков"""

    ip = models.CharField("IP-adress", max_length=25)
    pos = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE)
