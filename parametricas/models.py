from django.db import models


class ParametricaQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(is_deleted=False)


class ParametricaManager(models.Manager):
    def get_queryset(self):
        return ParametricaQuerySet(self.model, using=self._db)

    def not_deleted(self):
        return self.get_queryset().not_deleted()


class Parametrica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    valor = models.IntegerField(null=True)
    codigo = models.CharField(max_length=10, null=True)
    tabla = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=25, default='HABILITADO', null=True)
    is_deleted = models.BooleanField(default=False)

    objects = ParametricaManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    @property
    def is_deleted_property(self):
        return self.is_deleted

    class Meta:
        db_table = 'parametricas'
        ordering = ['id']  # Opcional: ordenamiento por id

    def __str__(self):
        return self.nombre  # O lo que prefieras mostrar
