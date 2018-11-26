from django.test import TestCase
from django.urls import reverse

from .models import Mineral

class TestMineral(TestCase):
    """Test Model"""
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
        """Tests home view"""
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['mineral_list'])
        self.assertIn(self.mineral2, resp.context['mineral_list'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral1.name)
        self.assertContains(resp, self.mineral2.name)

    def test_detail_view(self):
        """Tests detail view"""
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral2, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral2.name)
        self.assertContains(resp, self.mineral2.color)
        self.assertContains(resp, self.mineral2.image_caption)

