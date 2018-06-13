# Generated by Django 2.0.6 on 2018-06-13 06:23

from django.db import migrations, models
import ldapdb.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LdapGroup',
            fields=[
                ('dn', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('gid', ldapdb.models.fields.IntegerField(db_column='gidNumber', unique=True)),
                ('name', ldapdb.models.fields.CharField(db_column='cn', max_length=200, primary_key=True, serialize=False)),
                ('members', ldapdb.models.fields.ListField(db_column='memberUid')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
