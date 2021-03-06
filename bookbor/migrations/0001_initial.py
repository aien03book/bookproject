# Generated by Django 2.1.1 on 2018-10-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookpool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=145)),
                ('author', models.CharField(max_length=140)),
                ('issuedate', models.DateField()),
                ('buydate', models.DateField(blank=True, null=True)),
                ('publisher', models.CharField(max_length=30)),
                ('bookid', models.CharField(blank=True, max_length=30, null=True)),
                ('isbn', models.CharField(db_column='ISBN', max_length=45)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('bookimage', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'bookpool',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookrecord',
            fields=[
                ('terms', models.AutoField(primary_key=True, serialize=False)),
                ('borrowtime', models.DateTimeField()),
                ('returntime', models.DateTimeField()),
                ('note', models.TextField()),
            ],
            options={
                'db_table': 'bookrecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=45)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('memberid', models.CharField(blank=True, max_length=45, null=True)),
                ('joindate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'members',
                'managed': False,
            },
        ),
    ]
