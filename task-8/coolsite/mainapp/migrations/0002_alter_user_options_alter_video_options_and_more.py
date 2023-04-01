# Generated by Django 4.1.7 on 2023-04-02 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username', 'last_name', 'first_name'], 'verbose_name': 'Пользователь/автор', 'verbose_name_plural': 'Пользователи/авторы'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['pk'], 'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='login',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='video',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='get_videos', to='mainapp.user', verbose_name='Автор'),
        ),
    ]
