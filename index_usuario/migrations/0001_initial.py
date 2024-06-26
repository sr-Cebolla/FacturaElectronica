# Generated by Django 5.0.6 on 2024-05-27 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Definicion',
            fields=[
                ('id_definicion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_definicion', models.CharField(max_length=30)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EconomiaEmisores',
            fields=[
                ('id_economia_emisores', models.AutoField(primary_key=True, serialize=False)),
                ('impacto', models.TextField()),
                ('consecuencias', models.TextField()),
                ('cumplimiento_fiscal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Emisores',
            fields=[
                ('id_emisores', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvacionImpuestos',
            fields=[
                ('id_evacion_impuestos', models.AutoField(primary_key=True, serialize=False)),
                ('riesgos_asociados', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedioAmbiente',
            fields=[
                ('id_medio_ambiente', models.AutoField(primary_key=True, serialize=False)),
                ('beneficios_generados', models.TextField(blank=True, null=True)),
                ('info_reduccion_residuos', models.TextField(blank=True, null=True)),
                ('beneficios_ecologicos', models.TextField(blank=True, null=True)),
                ('ahorro_recursos', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoEvacion',
            fields=[
                ('id_metodo_evacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id_poblacion', models.AutoField(primary_key=True, serialize=False)),
                ('impacto', models.TextField()),
                ('consecuencias', models.TextField()),
                ('cambio_cultural', models.TextField()),
                ('beneficios_sociales', models.TextField()),
                ('seguridad_de_datos', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Efectos',
            fields=[
                ('id_efectos', models.AutoField(primary_key=True, serialize=False)),
                ('id_efecto_economia_emisores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.economiaemisores')),
                ('id_efecto_evacion_impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.evacionimpuestos')),
                ('id_efecto_medio_ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.medioambiente')),
                ('id_efecto_poblacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.poblacion')),
            ],
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id_informacion', models.AutoField(primary_key=True, serialize=False)),
                ('ventajas', models.TextField()),
                ('desventajas', models.TextField()),
                ('requerimientos', models.TextField()),
                ('id_definicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.definicion')),
                ('id_efectos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.efectos')),
                ('id_emisores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.emisores')),
            ],
        ),
        migrations.AddField(
            model_name='evacionimpuestos',
            name='id_metodo_evacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_usuario.metodoevacion'),
        ),
    ]
