# Generated by Django 2.1.1 on 2018-10-05 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookpool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=30)),
                ('issuedate', models.DateField()),
                ('buydate', models.DateField(blank=True, null=True)),
                ('publisher', models.CharField(max_length=30)),
                ('bookid', models.CharField(blank=True, max_length=30, null=True)),
                ('isbn', models.CharField(db_column='ISBN', max_length=45)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
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
                ('borrowtime', models.DateTimeField(auto_now=True)),
                ('returntime', models.DateTimeField()),
                ('note', models.TextField()),
                ('bookid', models.ForeignKey(db_column='bookid', on_delete=django.db.models.deletion.DO_NOTHING, to='bookbor.Bookpool')),
                ('memberid', models.ForeignKey(db_column='memberid', on_delete=django.db.models.deletion.DO_NOTHING, to='member.Members')),
            ],
            options={
                'db_table': 'bookrecord',
            },
        ),
    ]