# Generated by Django 3.2.9 on 2021-12-10 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='посетитель'),
        ),
        migrations.AddField(
            model_name='page',
            name='gallery',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, to='cms.gallery'),
        ),
        migrations.AddField(
            model_name='page',
            name='seo',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, to='cms.seo'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='seo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cms.seo', verbose_name='SEO-блок'),
        ),
        migrations.AddField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.gallery', verbose_name='галерея'),
        ),
        migrations.AddField(
            model_name='hall',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.cinema', verbose_name='кинотеатр'),
        ),
        migrations.AddField(
            model_name='hall',
            name='gallery',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, to='cms.gallery'),
        ),
        migrations.AddField(
            model_name='film',
            name='gallery',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, to='cms.gallery'),
        ),
        migrations.AddField(
            model_name='cinema',
            name='gallery',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, to='cms.gallery'),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('date', 'time', 'hall')},
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('row_number', 'place_number', 'schedule')},
        ),
        migrations.AlterUniqueTogether(
            name='hall',
            unique_together={('name', 'cinema')},
        ),
        migrations.AlterUniqueTogether(
            name='film',
            unique_together={('name', 'premiere_date')},
        ),
        migrations.AlterUniqueTogether(
            name='cinema',
            unique_together={('city', 'address')},
        ),
    ]
