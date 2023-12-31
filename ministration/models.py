from django.db import models

class MinistrationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(appointment_count=models.Count('appointment'))

class Ministration(models.Model):
    minisid = models.AutoField(db_column='MinisID', primary_key=True)
    name_ministration = models.CharField(db_column='Name_ministration', max_length=70)
    
    objects = MinistrationManager()

    class Meta:
        managed = False
        db_table = 'ministration'

    def __str__(self):
        return self.name_ministration

    def delete(self, *args, **kwargs):
        if self.appointment_count > 0:
            raise ValueError("Cannot delete a ministration with associated appointments.")
        super().delete(*args, **kwargs)
