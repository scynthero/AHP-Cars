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
    crit4 = models.TextField()
    crit5 = models.TextField(max_length=5,default="image",editable=False)
    crit_model = models.OneToOneField(Crit_model, on_delete=models.CASCADE)
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Criteria._meta.fields]

class Element(models.Model):
    class Meta():
        db_table = 'Element'

    crit1 = models.TextField()
    crit2 = models.TextField()
    crit3 = models.TextField()
    crit4 = models.TextField()
    image = models.ImageField()
    crit_model = models.ForeignKey(Crit_model, on_delete=models.CASCADE)
