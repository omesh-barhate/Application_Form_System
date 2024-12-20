# Generated by Django 4.1.7 on 2023-06-20 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='fy_sem1',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='fy_sem2',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='gap_certificate',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='migration_certificate',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='sy_sem1',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='sy_sem2',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ty_bms_market_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
                ('sy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem1_marksheet')),
                ('sy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem2_marksheet')),
            ],
        ),
        migrations.CreateModel(
            name='ty_bms_hr_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
                ('sy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem1_marksheet')),
                ('sy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem2_marksheet')),
            ],
        ),
        migrations.CreateModel(
            name='ty_bammc_journal_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
                ('sy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem1_marksheet')),
                ('sy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem2_marksheet')),
            ],
        ),
        migrations.CreateModel(
            name='ty_bammc_advert_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
                ('sy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem1_marksheet')),
                ('sy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.sy_sem2_marksheet')),
            ],
        ),
        migrations.CreateModel(
            name='sy_bms_market_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('fy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.fy_sem1_marksheet')),
                ('fy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.fy_sem2_marksheet')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
            ],
        ),
        migrations.CreateModel(
            name='sy_bms_hr_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('fy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.fy_sem1_marksheet')),
                ('fy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.fy_sem2_marksheet')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
            ],
        ),
        migrations.CreateModel(
            name='sy_bammc_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('fy_sem1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.fy_sem1_marksheet')),
                ('fy_sem2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.fy_sem2_marksheet')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
            ],
        ),
        migrations.CreateModel(
            name='fy_bammc_form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.academicyear')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.document')),
                ('hsc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.hsc_marksheet')),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.personal_details')),
                ('ssc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.ssc_marksheet')),
                ('subjects_choosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_app.subjects_selected')),
            ],
        ),
    ]
