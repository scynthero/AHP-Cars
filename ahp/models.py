from django.db import models
import itertools

# Create your models here.
class Crit_model(models.Model):
    class Meta():
        db_table = 'Criteria Model'

    name = models.TextField()
    decision = models.TextField(default='[["0"]]')


class Criteria(models.Model):
    class Meta():
        db_table = 'Criteria'

    crit1 = models.TextField("Criterion 1",max_length=100)
    crit2 = models.TextField("Criterion 2",max_length=100)
    crit3 = models.TextField("Criterion 3",max_length=100)
    crit4 = models.TextField("Wygląd", max_length=5, default="image", editable=False)
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
    attrib1 = models.TextField("Attribute 1")
    attrib2 = models.TextField("Attribute 2")
    attrib3 = models.TextField("Attribute 3")
    image = models.ImageField("Wygląd",upload_to='pictures/')
    crit_model = models.ForeignKey(Crit_model, on_delete=models.CASCADE)

    # TODO fix this fucking hack
    def get_fields(self):
        array = [(field.name, field.value_to_string(self)) for field in Element._meta.fields]
        array.pop(0)
        array.pop(-1)
        return array

    def get_pairs(self):
        array = []
        for pair in itertools.combinations([field.value_to_string(self) for field in Element._meta.fields], 2):
            array.append((pair))

        return array
