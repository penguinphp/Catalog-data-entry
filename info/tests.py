from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral

class TestMineral(TestCase):
    def test_mineral(self):
        mineral = Mineral.objects.create(
            name="Andesite",
            image_filename="Mineral",
            image_caption="Shiny",
            category="Earth metal",
            formula="Squared",
            strunz_classification="50",
            color="Black",
            crystal_system="Clear",
            unit_cell="Clear",
            crystal_symmetry="Clear",
            cleavage="Clear",
            mohs_scale_hardness="Clear",
            luster="Clear",
            streak="Clear",
            diaphaneity="Clear",
            optical_properties="Clear",
            refractive_index="Clear",
            crystal_habit="Clear",
            specific_gravity="Clear"
        )
        self.assertEqual(mineral.name, "Andesite")

class MineralViewTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="Andesite",
            color="Black",
            image_caption="Iron"
        )
        self.mineral2 = Mineral.objects.create(
            name="Granite",
            color="Gray",
            image_caption="Polish"
        )

    def test_home_view(self):
        resp = self.client.get(reverse('minerals:list'))

