# Generated by Django 4.0.4 on 2022-05-27 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.DateField()),
                ('eye_color', models.CharField(choices=[('b', 'black'), ('y', 'yellow'), ('g', 'green'), ('r', 'red')], help_text='r : red, y : yello, b : black, g : green', max_length=1)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.species')),
            ],
        ),
    ]
