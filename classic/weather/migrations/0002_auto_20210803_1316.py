# Generated by Django 3.1.3 on 2021-08-03 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fine_Dust_ppm_10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_ppm', models.IntegerField()),
                ('max_ppm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fine_Dust_ppm_2_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_ppm', models.IntegerField()),
                ('max_ppm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('min_temp', models.IntegerField()),
                ('max_temp', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='weather',
            name='fine_dust_10',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='min_fine_dust_2_5',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temperature',
        ),
        migrations.AddField(
            model_name='weather',
            name='ppm_10',
            field=models.ForeignKey(db_column='ppm_10', default='', on_delete=django.db.models.deletion.CASCADE, to='weather.fine_dust_ppm_10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='ppm_2_5',
            field=models.ForeignKey(db_column='ppm_2_5', default='', on_delete=django.db.models.deletion.CASCADE, to='weather.fine_dust_ppm_2_5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weather',
            name='month',
            field=models.ForeignKey(db_column='month', default=-1, on_delete=django.db.models.deletion.CASCADE, to='weather.month'),
            preserve_default=False,
        ),
    ]
