# Generated by Django 4.1.3 on 2022-12-09 01:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_created_cart_deleted_at_cart_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_deleted',
            field=models.BooleanField(db_index=True, default=False, editable=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='restored_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
