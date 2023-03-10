# Generated by Django 4.0.6 on 2022-08-01 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleetvehicle', '0001_initial'),
        ('employees', '0001_initial'),
        ('inspectionsvehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_backdoors',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_backdoors_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_coolingunit',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_coolingunit_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_leftwall',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_leftwall_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fleetvehicle.trailer'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_pollutants',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_rightwall',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_rightwall_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_seal',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_seal_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_tires',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_tires_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_under',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_box_under_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Cajas'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_carrier',
            field=models.CharField(choices=[('Transportes Refrigerados Rivas', 'Transportes Refrigerados Rivas')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_document_circulation',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_document_departamentmotors',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_document_invoice',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_document_physicalmechanics',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_document_securepolicy',
            field=models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_inspector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.employee'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_defense',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_defense_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Tractocamiones'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_engine',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_engine_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Tractocamiones'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_fueltank',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_fueltank_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Tractocamiones'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fleetvehicle.truck'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_tires',
            field=models.CharField(choices=[('Con anomalías', 'Con anomalías'), ('Sin anomalías', 'Sin anomalías')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='inspection_truck_tires_image',
            field=models.ImageField(null=True, upload_to='Inspecciones/Tractocamiones'),
        ),
    ]
