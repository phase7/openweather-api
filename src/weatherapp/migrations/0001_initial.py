# Generated by Django 4.2 on 2024-03-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.PositiveIntegerField()),
                ('pressure', models.IntegerField()),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_degree', models.IntegerField()),
                ('wind_direction', models.CharField(max_length=20, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='weatherdata',
            index=models.Index(fields=['city', '-timestamp'], name='weatherapp__city_ef9104_idx'),
        ),
    ]