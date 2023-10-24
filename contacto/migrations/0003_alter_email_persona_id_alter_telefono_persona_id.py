# Generated by Django 4.2.6 on 2023-10-24 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_alter_telefono_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='persona_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='contacto.personas'),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='persona_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefonos', to='contacto.personas'),
        ),
    ]
