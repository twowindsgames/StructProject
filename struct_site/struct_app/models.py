from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from datetime import date
from django.db.models import *


class Group(MPTTModel):
    title = models.CharField(max_length=20, verbose_name='Краткое наименование', blank=True)
    full_title = models.CharField(max_length=100, verbose_name='Полное наименование', blank=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
        db_index=True, verbose_name='Вышестоящее подразделение'
    )
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
        employees = Employee.objects.filter(group=self, )
        employees_count = employees.count()
        if (employees_count == 0):
            return {"employees_count": 0, "aver_age": 0, "aver_exp": 0}
        aver_age = self.get_avg_2date(employees, 'birthday_date')
        aver_exp = self.get_avg_2date(employees, 'date_of_joining')

        return {"employees_count": employees_count, "aver_age": int(aver_age), "aver_exp": int(aver_exp)}

    def get_avg_2date(self, employees, field):
        return employees.aggregate(
            result=Avg(
                date.today() - F(field),
                output_field=models.DateTimeField()
            )
        )['result'].days / 365

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя сотрудника', blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия сотрудника', blank=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество сотрудника', blank=True)
    post = models.CharField(max_length=50, verbose_name='Должность', blank=True)
    date_of_joining = models.DateField(auto_now=False, blank=True)
    birthday_date = models.DateField(auto_now=False, blank=True)
    slug = models.SlugField(max_length=150, null=True)
    group = TreeForeignKey('Group', on_delete=models.CASCADE, related_name='employees', verbose_name='Подразделение')
    image = models.ImageField(
        upload_to='employee_photos/', blank=True, null=True,
        default='employee_photos/default/default.jpg', )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def delete(self, using=None, keep_parents=False):
        if self.image.url != '/media/employee_photos/default/default.jpg':
            self.image.delete()
        super().delete()

    def __str__(self):
        return self.name
