# Generated by Django 2.1.2 on 2018-11-21 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0006_auto_20181121_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico',
            name='situacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academico.Situacao', verbose_name='Situação'),
            preserve_default=False,
        ),
    ]
