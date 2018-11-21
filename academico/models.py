from django.db import models

# Create your models here.


class Aluno(models.Model):
    cpf = models.CharField('CPF', primary_key=True, max_length=11)
    nome = models.CharField('Nome', max_length=255)
    dataNascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=1)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    complemento = models.CharField(
        'Complemento', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']


class TipoMatricula(models.Model):
    tipo = models.CharField('Tipo', max_length=255)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Tipo de matrícula'
        verbose_name_plural = 'Tipos de matrícula'
        ordering = ['tipo']


class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nome']


class Professor (models.Model):
    cfe = models.CharField('CFE', primary_key=True, max_length=11)
    nome = models.CharField('Nome', max_length=255)
    dataNascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=1)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    complemento = models.CharField(
        'Complemento', max_length=500, null=True, blank=True)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name='Departamento')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['nome']


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    creditos = models.IntegerField('Créditos')
    cargaHoraria = models.IntegerField('Carga Horária')
    cargaHorariaObrigatoria = models.IntegerField('Carga Horária Obrigatória')
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name='Departamento')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['departamento', 'nome']


class Matricula(models.Model):
    matricula = models.CharField('Matrícula', primary_key=True, max_length=25)
    cpf = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, verbose_name='Aluno')
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, verbose_name='Curso')
    tipoMatricula = models.ForeignKey(
        TipoMatricula, on_delete=models.CASCADE, verbose_name='Tipo de Matrícula')
    dataAdmissao = models.DateField('Data de Admissão')

    def __str__(self):
        return self.matricula

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering = ['matricula']


class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=255)
    cargaHoraria = models.IntegerField('Carga Horária')
    creditos = models.IntegerField('Créditos')
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Professor')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']


class PreRequisito (models.Model):
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    preRequisito = models.ForeignKey(
        Disciplina, related_name='PreRequisito', on_delete=models.CASCADE, verbose_name='Pré-Requisito')

    def __str__(self):
        return str(str(self.disciplina) + '-' + str(self.preRequisito))

        class Meta:
            verbose_name = 'Pré-Requisito'
            verbose_name_plural = 'Pré-Requisitos'
            ordering = ['disciplina', 'preRequisito']


class DisciplinaCurso(models.Model):
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, verbose_name='Curso')
    obrigatoria = models.BooleanField('Obrigatória')

    def __str__(self):
        return str(str(self.disciplina) + ' do curso de ' + str(self.curso))

    class Meta:
        verbose_name = 'Disciplina do Curso'
        verbose_name_plural = 'Disciplinas do Curso'
        ordering = ['curso', 'disciplina']


class Periodo(models.Model):
    semestre = models.CharField('Semestre', primary_key=True, max_length=6)
    inicioMatricula = models.DateField('Inicio da data de matrícula')
    finalMatricula = models.DateField('Data final de matrícula')

    def __str__(self):
        return self.semestre

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
        ordering = ['-semestre']


class Situacao(models.Model):
    situacao = models.CharField('Situação', max_length=255)

    def __str__(self):
        return self.situacao

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'
        ordering = ['situacao']


class Historico(models.Model):
    matricula = models.ForeignKey(
        Matricula, on_delete=models.CASCADE, verbose_name='Matrícula')
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, verbose_name='Período')
    notaFinal = models.DecimalField(
        'Nota Final', max_digits=4, decimal_places=2, null=True, blank=True)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE, verbose_name='Situação')

    def __str__(self):
        return self.matricula + ' matriculou-se em ' + self.disciplina + ' no período ' + self.periodo

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'
        ordering = ['periodo', 'matricula']


class Turma(models.Model):
    matricula = models.ForeignKey(
        Matricula, on_delete=models.CASCADE, verbose_name='Matrícula')
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, verbose_name='Período')
    notaFinal = models.DecimalField(
        'Nota Final', max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.matricula) + ' matriculou-se em ' + str(self.disciplina) + ' no período ' + str(self.periodo)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['disciplina', 'periodo', 'matricula']
