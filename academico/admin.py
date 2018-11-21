from django.contrib import admin

from .models import Aluno, TipoMatricula, Departamento, Professor, Curso, Matricula, Disciplina
from .models import PreRequisito, DisciplinaCurso, Periodo, Situacao, Historico, Turma
# Register your models here.


class AlunoAdmin (admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'dataNascimento',
                    'sexo', 'cep', 'complemento']
    search_display = ['sexo', 'created', 'modified']
    list_filter = ['sexo']
    search_fields = ['nome']

admin.site.register(Aluno, AlunoAdmin)


class TipoMatriculaAdmin (admin.ModelAdmin):
    list_display = ['id', 'tipo']
    search_display = ['id', 'tipo']
    list_filter = ['id', 'tipo']

admin.site.register(TipoMatricula, TipoMatriculaAdmin)


class DepartamentoAdmin (admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_display = ['id', 'nome']
    list_filter = ['id', 'nome']

admin.site.register(Departamento, DepartamentoAdmin)


class ProfessorAdmin (admin.ModelAdmin):
    list_display = ['cfe', 'nome', 'dataNascimento',
                    'sexo', 'cep', 'complemento', 'departamento']
    search_display = ['sexo', 'created', 'modified']
    list_filter = ['sexo']

admin.site.register(Professor, ProfessorAdmin)


class CursoAdmin (admin.ModelAdmin):
    list_display = ['nome', 'creditos', 'cargaHoraria',
                    'cargaHorariaObrigatoria', 'departamento']
    search_display = ['departamento', 'nome']
    list_filter = ['departamento', 'nome']

admin.site.register(Curso, CursoAdmin)


class MatriculaAdmin (admin.ModelAdmin):
    list_display = ['matricula', 'cpf', 'curso',
                    'tipoMatricula', 'dataAdmissao']
    search_display = ['curso', 'tipoMatricula']
    list_filter = ['curso', 'tipoMatricula']

admin.site.register(Matricula, MatriculaAdmin)


class DisciplinaAdmin (admin.ModelAdmin):
    list_display = ['nome', 'cargaHoraria',
                    'creditos', 'professor', 'departamento']
    search_display = ['departamento', 'nome']
    list_filter = ['departamento', 'nome']

admin.site.register(Disciplina, DisciplinaAdmin)


class PreRequisitoAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'preRequisito']
    search_display = ['disciplina', 'preRequisito']
    list_filter = ['disciplina', 'preRequisito']

admin.site.register(PreRequisito, PreRequisitoAdmin)


class DisciplinaCursoAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'curso', 'obrigatoria']
    search_display = ['curso', 'disciplina', 'obrigatoria']
    list_filter = ['curso', 'disciplina', 'obrigatoria']

admin.site.register(DisciplinaCurso, DisciplinaCursoAdmin)


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['semestre']
    search_display = ['semestre']
    list_filter = ['semestre']

admin.site.register(Periodo, PeriodoAdmin)


class SituacaoAdmin(admin.ModelAdmin):
    list_display = ['situacao']
    search_display = ['situacao']
    list_filter = ['situacao']
    search_fields = ['situacao']

admin.site.register(Situacao, SituacaoAdmin)


class HistoricoAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'disciplina', 'periodo', 'notaFinal']
    search_display = ['disciplina', 'periodo']
    list_filter = ['disciplina', 'periodo']

admin.site.register(Historico, HistoricoAdmin)


class TurmaAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'disciplina', 'periodo', 'notaFinal']
    search_display = ['disciplina', 'periodo']
    list_filter = ['disciplina', 'periodo']

admin.site.register(Turma, TurmaAdmin)
