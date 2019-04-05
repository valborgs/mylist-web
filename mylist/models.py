from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

from PIL import Image
# Create your models here.


class MylistQuarter(models.Model):
    quarter = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.quarter)



class MylistYear(models.Model):
    year = models.IntegerField(unique=True)

    production_img = models.ImageField(default='default.gif', upload_to='productions')

    year_slug = models.SlugField(blank=True, allow_unicode=True, unique=True, db_index=True)

    class Meta:
        verbose_name_plural = "Years"

    def __str__(self):
        return str(self.year)

    def imgsave(self, *args, **kwargs):
        super(MylistProduction, self).save(*args, **kwargs)

        img = Image.open(self.production_img.path)

        if img.height > 320 or img.width > 320:
            output_size = (320,320)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.year_slug = slugify(self.year, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)


class MylistProduction(models.Model):
    production_name = models.CharField(max_length=200, unique=True)
    production_info = models.TextField()
    production_img = models.ImageField(default='default.gif', upload_to='productions')

    production_slug = models.SlugField(blank=True, allow_unicode=True, unique=True, db_index=True)

    class Meta:
        verbose_name_plural = "Productions"

    def imgsave(self, *args, **kwargs):
        super(MylistProduction, self).save(*args, **kwargs)

        img = Image.open(self.production_img.path)

        if img.height > 320 or img.width > 320:
            output_size = (320,320)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.production_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.production_slug = slugify(self.production_name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)




class MylistGenre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)
    genre_img = models.ImageField(default='default.gif', upload_to='genres')

    genre_slug = models.SlugField(blank=True, allow_unicode=True, unique=True, db_index=True)

    class Meta():
        verbose_name_plural = "Genres"

    def imgsave(self, *args, **kwargs):
        super(MylistGenre, self).save(*args, **kwargs)

        img = Image.open(self.genre_img.path)

        if img.height > 320 or img.width > 320:
            output_size = (320,320)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.genre_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.genre_slug = slugify(self.genre_name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)




class MylistTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    summary = models.TextField()
    title_img = models.ImageField(default='default.gif', upload_to='titles')

    title_slug = models.SlugField(blank=True, allow_unicode=True, unique=True, db_index=True)

    genre1 = models.ForeignKey(MylistGenre,
                              default=1,
                              verbose_name="Genres",
                              on_delete=models.SET_DEFAULT)
    genre2 = models.ForeignKey(MylistGenre,
                              verbose_name="Genres",
                              default=None,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='genre2')
    genre3 = models.ForeignKey(MylistGenre,
                              verbose_name="Genres",
                              default=None,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='genre3')

    production = models.ForeignKey(MylistProduction,
                                   default=1,
                                   verbose_name="Productions",
                                   on_delete=models.SET_DEFAULT)
    year = models.ForeignKey(MylistYear,
                             default=1,
                             verbose_name="Years",
                             on_delete=models.SET_DEFAULT)
    quarter = models.ForeignKey(MylistQuarter,
                                default=1,
                                on_delete=models.SET_DEFAULT,
                                validators=[MinValueValidator(1),
                                MaxValueValidator(4)])

    viewcount = models.IntegerField(default=0)
    userlikes = models.IntegerField(default=0)
    userdislikes = models.IntegerField(default=0)

    def imgsave(self, *args, **kwargs):
        super(MylistGenre, self).save(*args, **kwargs)

        img = Image.open(self.title_img.path)

        if img.height > 320 or img.width > 320:
            output_size = (320,320)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.title_slug = slugify(self.title, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)
