# Generated by Django 3.2.3 on 2021-10-01 14:54

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('status', model_utils.fields.StatusField(choices=[('Available', 'Available'), ('Not available', 'Not available')], default='Available', max_length=100, no_check_for_status=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['title', 'price'],
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('rating', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
