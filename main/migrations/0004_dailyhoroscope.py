# Generated by Django 3.0 on 2020-07-20 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200711_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyHoroscope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='zodiac2.jpg', upload_to='')),
                ('zodiac', models.CharField(choices=[('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces')], max_length=50)),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Normal', 'Normal'), ('Career', 'Career'), ('Love', 'Love'), ('Health', 'Health')], max_length=50)),
                ('content', models.TextField()),
                ('astroprofile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Astro_Profile')),
            ],
        ),
    ]