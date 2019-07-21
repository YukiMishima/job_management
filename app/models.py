from django.db import models
# from django.core import validators
from django.utils import timezone


class Job(models.Model):

    SUPPORT_CHOICES = (
        (1, 'anatase'),
        (2, 'rutile'),
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )

    support = models.IntegerField(
        verbose_name='担体',
        choices=SUPPORT_CHOICES,
        default=1
    )

    memo = models.TextField(
        verbose_name='備考',
        max_length=500,
        blank=True,
        null=True,
    )

    send_date = models.DateField(
        verbose_name='投げた日',
        default=timezone.now,
    )

    get_date = models.DateField(
        verbose_name='返ってきた日',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ジョブ'
        verbose_name_plural = 'ジョブ'

