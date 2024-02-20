# Generated by Django 5.0.1 on 2024-02-19 17:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torre_crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='deporte',
        ),
        migrations.AlterUniqueTogether(
            name='jugador',
            unique_together={('id_equipo', 'dorsal')},
        ),
        migrations.RemoveField(
            model_name='partido',
            name='deporte',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='instalacion',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='local',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='visitante',
        ),
        migrations.AddField(
            model_name='equipo',
            name='id_deporte',
            field=models.ForeignKey(db_column='id_deporte', default=0, on_delete=django.db.models.deletion.RESTRICT, to='torre_crud.deporte'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='id_equipo',
            field=models.ForeignKey(db_column='id_equipo', default=0, on_delete=django.db.models.deletion.RESTRICT, to='torre_crud.equipo'),
        ),
        migrations.AddField(
            model_name='partido',
            name='id_deporte',
            field=models.ForeignKey(db_column='id_deporte', default=0, on_delete=django.db.models.deletion.RESTRICT, to='torre_crud.deporte'),
        ),
        migrations.AddField(
            model_name='partido',
            name='id_instalacion',
            field=models.ForeignKey(blank=True, db_column='id_instalacion', default=0, null=True, on_delete=django.db.models.deletion.RESTRICT, to='torre_crud.instalacion'),
        ),
        migrations.AddField(
            model_name='partido',
            name='id_local',
            field=models.ForeignKey(db_column='id_local', default=0, on_delete=django.db.models.deletion.RESTRICT, related_name='local_partidos', to='torre_crud.equipo'),
        ),
        migrations.AddField(
            model_name='partido',
            name='id_visitante',
            field=models.ForeignKey(db_column='id_visitante', default=0, on_delete=django.db.models.deletion.RESTRICT, related_name='visitante_partidos', to='torre_crud.equipo'),
        ),
        migrations.AlterField(
            model_name='partido',
            name='puntos_local',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='partido',
            name='puntos_visitante',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='equipo',
        ),
    ]