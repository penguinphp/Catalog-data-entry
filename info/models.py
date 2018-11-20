from django.db import models

class Mineral(models.Model):
    name = models.CharField(max_length=200)
    image_filename = models.CharField(max_length=200)
    image_caption = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    formula = models.CharField(max_length=200)
    strunz_classification = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    crystal_system = models.CharField(max_length=200)
    unit_cell = models.CharField(max_length=200)
    crystal_symmetry = models.CharField(max_length=200)
    cleavage = models.CharField(max_length=200)
    mohs_scale_hardness = models.CharField(max_length=200)
    luster = models.CharField(max_length=200)
    streak = models.CharField(max_length=200)
    diaphaneity = models.CharField(max_length=200)
    optical_properties = models.CharField(max_length=200)
    refractive_index = models.CharField(max_length=200)
    crystal_habit = models.CharField(max_length=200)
    specific_gravity = models.CharField(max_length=200)

    def __str__(self):
        return self.name

