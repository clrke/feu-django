from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class SerializeableModel(models.Model):
    class Meta:
        abstract = True

    def serialize(self):
        dictionary = {}

        for field in self._meta.get_all_field_names():
            dictionary[field] = self.__getattribute__(field)

        return dictionary


class Task(SerializeableModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    assigned_to = models.ForeignKey(User)
    is_completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%s] %s %s" % (self.assigned_to, self.title,
                'OK' if self.is_completed else '')


class StatusPost(SerializeableModel):
    body = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s: %s" % (self.author, self.body)

