# Generated by Django 5.2.3 on 2025-06-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('year', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('category', models.SmallIntegerField(choices=[(1, 'AVENTURA'), (2, 'FANTASIA'), (3, 'RPG'), (4, 'SOBREVIVENCIA'), (5, 'TERROR'), (6, 'PLATAFORMA'), (7, 'QUEBRA-CABECA'), (8, 'FPS')])),
                ('isUsed', models.BooleanField()),
                ('image', models.ImageField(null=True, upload_to='game/images')),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
    ]
