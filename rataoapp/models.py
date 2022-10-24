# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acervo(models.Model):
    item = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    autor = models.CharField(max_length=80, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    tombamento = models.IntegerField(blank=True, null=True)
    uni = models.CharField(max_length=10, blank=True, null=True)
    quant = models.CharField(max_length=10, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    local = models.CharField(max_length=30, blank=True, null=True)
    valor_unitario = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    formaaquisi = models.CharField(max_length=50, blank=True, null=True)
    not_fiscal = models.IntegerField(blank=True, null=True)
    fornecedor = models.CharField(max_length=50, blank=True, null=True)
    ne = models.CharField(max_length=20, blank=True, null=True)
    data = models.CharField(max_length=12, blank=True, null=True)
    processo = models.CharField(max_length=50, blank=True, null=True)
    foto = models.CharField(max_length=80, blank=True, null=True)
    responsavel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acervo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Classificacao(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=80, blank=True, null=True)
    classe = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classificacao'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fornecedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=83, blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    foto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedor'


class Local(models.Model):
    codigo = models.AutoField(primary_key=True)
    setor = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=200, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local'


class Marca(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'


class Material(models.Model):
    item = models.AutoField(db_column='ITEM', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=701, blank=True, null=True)  # Field name made lowercase.
    tombamento = models.IntegerField(db_column='TOMBAMENTO', blank=True, null=True)  # Field name made lowercase.
    uni = models.CharField(db_column='UNI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    quant = models.FloatField(db_column='QUANT', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    codlocal = models.IntegerField(blank=True, null=True)
    local = models.CharField(db_column='LOCAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valor_unitario = models.FloatField(db_column='VALOR_UNITARIO', blank=True, null=True)  # Field name made lowercase.
    valor_total = models.FloatField(db_column='VALOR_TOTAL', blank=True, null=True)  # Field name made lowercase.
    foto = models.CharField(max_length=70, blank=True, null=True)
    forn = models.CharField(max_length=100, blank=True, null=True)
    nf = models.CharField(max_length=20, blank=True, null=True)
    data_nf = models.CharField(max_length=14, blank=True, null=True)
    ne = models.CharField(max_length=14, blank=True, null=True)
    data_ne = models.CharField(max_length=14, blank=True, null=True)
    datareceb = models.CharField(max_length=12, blank=True, null=True)
    processo = models.CharField(max_length=25, blank=True, null=True)
    tipoentrada = models.CharField(max_length=23, blank=True, null=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    data_manute = models.CharField(max_length=12, blank=True, null=True)
    id_local = models.ForeignKey(Local, models.DO_NOTHING, db_column='id_local', blank=True, null=True)
    id_fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='id_fornecedor', blank=True, null=True)
    id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    id_classifica = models.ForeignKey(Classificacao, models.DO_NOTHING, db_column='id_classifica', blank=True, null=True)
    id_nota = models.ForeignKey('Notafiscal', models.DO_NOTHING, db_column='id_nota', blank=True, null=True)
    id_processo = models.ForeignKey('Processo', models.DO_NOTHING, db_column='id_processo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material'


class Notafiscal(models.Model):
    codigo = models.AutoField(primary_key=True)
    num_nota = models.CharField(max_length=10, blank=True, null=True)
    data_emissao = models.CharField(max_length=10, blank=True, null=True)
    data_recebimento = models.CharField(max_length=10, blank=True, null=True)
    valor_nota = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notafiscal'


class Processo(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=25, blank=True, null=True)
    data = models.CharField(max_length=10, blank=True, null=True)
    situacao = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processo'
