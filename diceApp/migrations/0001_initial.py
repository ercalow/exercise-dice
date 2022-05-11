# Generated by Django 4.0.4 on 2022-05-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('muscleGroup', models.CharField(choices=[('abs', 'Abs'), ('push', 'Push'), ('pull', 'Pull'), ('legs', 'Legs')], max_length=30)),
                ('muscleGroup2', models.CharField(choices=[('abs', 'Abs'), ('push', 'Push'), ('pull', 'Pull'), ('legs', 'Legs')], max_length=30)),
                ('difficulty', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('reps', models.IntegerField()),
                ('alwaysInclude', models.CharField(choices=[(False, 'No'), (True, 'Yes')], max_length=30)),
            ],
        ),
    ]