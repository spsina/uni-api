# Generated by Django 2.1.7 on 2019-04-24 14:09

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_student_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/', validators=[users.utils.validate_image_size]),
        ),
    ]
