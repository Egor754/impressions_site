# Generated by Django 4.0 on 2021-12-19 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Долгота')),
                ('description', models.TextField(verbose_name='Описание')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories', to='auth.user', verbose_name='Пользователь')),
            ],
        ),
    ]
