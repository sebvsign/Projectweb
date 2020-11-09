from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectowebApp', '0002_auto_20201105_2249'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
