# Generated by Django 3.1.1 on 2020-09-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('published', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
            ],
        ),
    ]
