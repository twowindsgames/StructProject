from django.db import models
import math

from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
from datetime import date, datetime
from PIL import Image





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

    def get_absolute_url(self):
        url = "/%s" % self.slug
        page = self
        while page.parent:
            url = "/%s%s" % (page.parent.slug, url)
            page = page.parent
        return url

    def get_group_stat(self):
        groupUnits = Unit.objects.filter(group=self, )
        unitsCount = groupUnits.count()
        if unitsCount == 0:
            return {"unitsCount": 0, "averAge": 0, "averExp": 0}
        averAge = 0
        averExp = 0
        for unit in groupUnits:
            averAge += unit.get_age()
            averExp += unit.get_experience()
        averAge /= unitsCount
        averExp /= unitsCount
        return {"unitsCount": unitsCount, "averAge": int(averAge), "averExp": int(averExp)}

    def __str__(self):
        return self.title


class Unit(models.Model):
    employeeName = models.CharField(max_length=50, verbose_name='ФИО сотрудника')
    employeePost = models.CharField(max_length=50, verbose_name='Должность')
    dateOfJoining = models.DateField()
    birthdayDate = models.DateField(auto_now=False, null=True, blank=True)
    slug = models.SlugField(max_length=150, null=True)
    group = TreeForeignKey('Group', on_delete=models.CASCADE, related_name='units', verbose_name='Подразделение')
    image = models.ImageField(upload_to='unit_photos/', blank=True, null=True, )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def get_age(self):
        today = date.today()
        age = today.year - self.birthdayDate.year - (
                (today.month, today.day) < (self.birthdayDate.month, self.birthdayDate.day))
        return age

    def get_experience(self):
        today = date.today()
        experience = today.year - self.dateOfJoining.year - (
                (today.month, today.day) < (self.dateOfJoining.month, self.dateOfJoining.day))
        return experience

    def __str__(self):
        return self.employeeName
