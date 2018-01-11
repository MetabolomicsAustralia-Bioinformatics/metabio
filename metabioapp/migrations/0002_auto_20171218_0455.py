# Generated by Django 2.0 on 2017-12-18 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metabioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='uploadfile',
            old_name='path',
            new_name='upload_file',
        ),
        migrations.AddField(
            model_name='downloadfile',
            name='upload_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metabioapp.UploadFile'),
        ),
    ]
