# Generated by Django 2.2.6 on 2020-03-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del consultorio', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Consultorios',
            },
        ),
    ]
