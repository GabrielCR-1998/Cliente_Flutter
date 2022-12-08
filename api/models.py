# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carreras(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Carreras'


class Cursos(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=16, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    codigo_carrera = models.ForeignKey(Carreras, models.DO_NOTHING, db_column='Codigo_Carrera')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cursos'


class Grupos(models.Model):
    idgrupo = models.AutoField(db_column='idGrupo', primary_key=True)  # Field name made lowercase.        
    codigo_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='Codigo_Curso', blank=True, null=True)  # Field name made lowercase.
    idperiodo = models.ForeignKey('Periodos', models.DO_NOTHING, db_column='idPeriodo', blank=True, null=True)  # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grupos'


class Matricula(models.Model):
    idmatricula = models.AutoField(db_column='idMatricula', primary_key=True)  # Field name made lowercase.    
    grupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    carrera = models.ForeignKey(Carreras, models.DO_NOTHING, db_column='Carrera', blank=True, null=True)  # Field name made lowercase.
    curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='Curso', blank=True, null=True)  # Field name made lowercase.
    estudiante = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Estudiante', blank=True, null=True)  # Field name made lowercase.
    tipomatricula = models.CharField(db_column='TipoMatricula', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Matricula'


class Periodos(models.Model):
    idperiodo = models.AutoField(db_column='idPeriodo', primary_key=True)  # Field name made lowercase.    
    fecha_incio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'Periodos'


class Usuarios(models.Model):
    identificacion = models.CharField(db_column='Identificacion', primary_key=True, max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=16, db_collation='Modern_Spanish_CI_AS')  
# Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'



