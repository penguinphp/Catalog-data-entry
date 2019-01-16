from django.db import migrations
import json


def load_data(apps, schema_editor):
    print("Loading data into database")

    try:
        Mineral = apps.get_model('info', 'Mineral')
        with open('static/data/minerals.json', encoding='utf8') as file:
            minerals = json.load(file)
            for mineral in minerals:
                Mineral(
                    name=mineral.get('name', ''),
                    image_filename=mineral.get('image filename', ''),
                    image_caption=mineral.get('image caption', ''),
                    category=mineral.get('category', ''),
                    formula=mineral.get('formula', ''),
                    strunz_classification=mineral.get('strunz classification', ''),
                    color=mineral.get('color', ''),
                    crystal_system=mineral.get('crystal system', ''),
                    unit_cell=mineral.get('unit cell', ''),
                    crystal_symmetry=mineral.get('crystal symmetry', ''),
                    cleavage=mineral.get('cleavage', ''),
                    mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
                    luster=mineral.get('luster', ''),
                    streak=mineral.get('streak', ''),
                    diaphaneity=mineral.get('diaphaneity', ''),
                    optical_properties=mineral.get('optical properties', ''),
                    refractive_index=mineral.get('refractive index', ''),
                    crystal_habit=mineral.get('crystal habit', ''),
                    specific_gravity=mineral.get('specific gravity', ''),
                    group=mineral.get('group', ''),
                ).save()

    except LookupError:
        # The old app isn't installed.
        return
    except FileNotFoundError:
        print("That file does not exist.")
        return
    # Now this is where we write the logic to read your minerals.json file in.
    # Then load it from JSON into your Mineral model so it saves them to Database.



class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(load_data, migrations.RunPython.noop),
    ]

    dependencies = [
        # TODO: Fix appname to your apps name
        ('info', '0001_initial'),
    ]


