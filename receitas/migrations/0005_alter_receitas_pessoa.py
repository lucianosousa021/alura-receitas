# Generated by Django 3.2.5 on 2021-07-25 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        #('alura_receita', '0004_receitas_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alura_receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]