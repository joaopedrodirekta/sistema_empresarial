# Generated by Django 5.1.6 on 2025-02-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_funcionarios/'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='admissao',
            field=models.DateField(help_text='Formato: dd/mm/aaaa'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cracha_vale_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='data_nascimento',
            field=models.DateField(help_text='Formato: dd/mm/aaaa'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='desligamento',
            field=models.DateField(blank=True, help_text='Formato: dd/mm/aaaa', null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='desmobilizacao',
            field=models.DateField(blank=True, help_text='Formato: dd/mm/aaaa', null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='mobilizacao',
            field=models.DateField(blank=True, help_text='Formato: dd/mm/aaaa', null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='validade_cnh',
            field=models.DateField(blank=True, help_text='Formato: dd/mm/aaaa', null=True),
        ),
    ]
