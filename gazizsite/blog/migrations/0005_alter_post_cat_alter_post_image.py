# Generated by Django 4.1.3 on 2022-11-25 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_cat_post_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
