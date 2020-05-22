from django.db import models


# Create your models here.
class Crit_model(models.Model):
    class Meta():
        db_table = 'Criteria Model'

    name = models.TextField()
    decision = models.TextField()


class Criteria(models.Model):
    class Meta():
        db_table = 'Criteria'

    crit1 = models.TextField()
    crit2 = models.TextField()
    crit3 = models.TextField()

    crit4 = models.TextField(max_length=5, default="image", editable=False)
    crit_model = models.OneToOneField(Crit_model, on_delete=models.CASCADE)

    # TODO fix this fucking hack
    def get_fields(self):
        array = [(field.name, field.value_to_string(self)) for field in Criteria._meta.fields]
        array.pop(0)
        array.pop(-1)
        return array


class Element(models.Model):
    class Meta():
        db_table = 'Element'

    name = models.TextField()
    attrib1 = models.TextField()
    attrib2 = models.TextField()
    attrib3 = models.TextField()
    image = models.ImageField(upload_to='pictures/')
    crit_model = models.ForeignKey(Crit_model, on_delete=models.CASCADE)

    # TODO fix this fucking hack
    def get_fields(self):
        array = [(field.name, field.value_to_string(self)) for field in Element._meta.fields]
        array.pop(0)
        array.pop(-1)
        return array
