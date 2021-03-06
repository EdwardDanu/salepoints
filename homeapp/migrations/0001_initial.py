# Generated by Django 3.2 on 2022-03-09 20:45

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AEDaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('balance', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=None, max_length=100)),
                ('modelindex', models.IntegerField()),
                ('entryindex', models.IntegerField()),
                ('entrysid', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandsection', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('trending', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Deposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.CharField(blank=True, max_length=50)),
                ('reference', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('sfirstname', models.CharField(max_length=50)),
                ('slastname', models.CharField(max_length=50)),
                ('scurrency', models.CharField(max_length=10)),
                ('samount', models.FloatField(blank=True, null=True)),
                ('referenceb', models.CharField(blank=True, max_length=50)),
                ('rfirstname', models.CharField(max_length=50)),
                ('rlastname', models.CharField(max_length=50)),
                ('rcurrency', models.CharField(max_length=10)),
                ('ramount', models.FloatField(blank=True, null=True)),
                ('vcurrency', models.CharField(max_length=10)),
                ('vamount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandsection', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('trending', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Hair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandsection', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('trending', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Perfumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandsection', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('trending', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='USDaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('balance', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='PerfumesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Perfumes', verbose_name='Image')),
                ('entry', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='perfumesphoto', to='homeapp.perfumes')),
            ],
        ),
        migrations.CreateModel(
            name='HairImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Hair', verbose_name='Image')),
                ('entry', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hairphoto', to='homeapp.hair')),
            ],
        ),
        migrations.CreateModel(
            name='FootwearImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Footwear', verbose_name='Image')),
                ('entry', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='footwearphoto', to='homeapp.footwear')),
            ],
        ),
        migrations.CreateModel(
            name='ClothingImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Clothing', verbose_name='Image')),
                ('entry', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='clothingphoto', to='homeapp.clothing')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
