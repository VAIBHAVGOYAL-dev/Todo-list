from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=256, blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todo_list'