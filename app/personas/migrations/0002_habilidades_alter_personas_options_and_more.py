# Generated by Django 4.0.3 on 2022-03-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidad Personas',
            },
        ),
        migrations.AlterModelOptions(
            name='personas',
            options={'ordering': ['name'], 'verbose_name': 'Personas', 'verbose_name_plural': 'Persona'},
        ),
        migrations.AlterUniqueTogether(
            name='personas',
            unique_together={('name', 'correo')},
        ),
        migrations.AddField(
            model_name='personas',
            name='habilidades',
            field=models.ManyToManyField(to='personas.habilidades'),
        ),
    ]