from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField


# Create your models here.



class Group(MPTTModel):
    title = models.CharField(max_length=20, verbose_name='Краткое наименование')
    full_title = models.CharField(max_length=100, verbose_name='Полное наименование')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Вышестоящее подразделение')
    slug = models.SlugField()





    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = "/%s" % self.slug
        page = self
        while page.parent:
            url = "/%s%s" % (page.parent.slug, url)
            page = page.parent
        return url


class Unit(models.Model):
    employeeName = models.CharField(max_length=50, verbose_name='ФИО сотрудника')
    employeePost = models.CharField(max_length=50, verbose_name='Должность')
    dateOfJoining = models.DateField()
    slug = models.SlugField(max_length=150, null=True)
    group = TreeForeignKey('Group', on_delete=models.CASCADE, related_name='units', verbose_name='Подразделение')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.employeeName
