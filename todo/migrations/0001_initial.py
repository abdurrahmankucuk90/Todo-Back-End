# Generated by Django 4.1 on 2022-09-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('describtion', models.TextField(verbose_name='description')),
                ('status', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending'), ('I', 'In-Progres')], max_length=2)),
                ('priority', models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣')], max_length=2)),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
