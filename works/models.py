from django.db import models

# Create your models here.


class Project (models.Model):

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Project name',
        help_text='Name of project'
    )
    description = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name='Project descripton',
        help_text='Name of project'
    )
    date_of_create = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of create',
        help_text='',
    )

    web_site = models.URLField(
        null=False,
        blank=True,
        verbose_name='Web site Address',
        help_text=''
    )

    categories = models.ManyToManyField(
        "Category",
        blank=False,
        verbose_name="Categories",
        help_text='',
    )
    portfolio = models.ImageField(
        blank=True,
        null=False,
        default='',
        verbose_name="Cover_image",
        help_text='',
    )


class Category(models.Model) :
    name = models.CharField(
        max_length=50,
        verbose_name='Category name',
        help_text='',
    )
    description = models.TextField(
            blank=True,
            verbose_name='Descritpion',
            help_text='',
        )