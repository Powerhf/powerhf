# Generated by Django 5.0 on 2024-06-28 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_premonsoonimages_pmcl'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentsOfRepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(null=True, upload_to='Documents_repository/%y', verbose_name='Files')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentRepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(choices=[('Feul Pump Automation Work For Gilbarco', 'Feul Pump Automation Work For Gilbarco'), ('DG RNR, For ATC, Ascend, TVI', 'DG RNR, For ATC, Ascend, TVI'), ('EV Charger I&C, PM & BDN Calls For Gilbarco', 'EV Charger I&C, PM & BDN Calls For Gilbarco'), ('Retail DG Repair', 'Retail DG Repair'), ('5G Upgradation For ATC', '5G Upgradation For ATC'), ('FTTH For Microscan', 'FTTH For Microscan')], max_length=100, null=True, verbose_name='Project Types')),
                ('region', models.CharField(choices=[('East', 'East'), ('West', 'West'), ('North', 'North'), ('South', 'South')], max_length=100, null=True, verbose_name='Regions')),
                ('site_docs_id', models.CharField(max_length=100, null=True, verbose_name='SiteID & DocumentID')),
                ('circles', models.CharField(choices=[('JK', 'JK'), ('UPE', 'UPE'), ('UPW', 'UPW'), ('HP, HR & PB', 'HP, HR & PB'), ('DL', 'DL'), ('MU, MH & GJ', 'MU, MH & GJ'), ('RJ & MP', 'RJ & MP'), ('CG', 'CG'), ('AS & NE', 'AS & NE'), ('WB & KOL', 'WB & KOL'), ('OD', 'OD'), ('JH', 'JH'), ('BH', 'BH'), ('AP & TS', 'AP & TS'), ('TN', 'TN'), ('KN', 'KN'), ('KL', 'KL')], max_length=50, verbose_name='Circles')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(related_name='Documents', to='app.documentsofrepository')),
            ],
        ),
    ]
