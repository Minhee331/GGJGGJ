# Generated by Django 2.1.1 on 2020-10-09 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookID', to='home.Book'),
        ),
    ]