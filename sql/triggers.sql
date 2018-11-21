CREATE OR REPLACE FUNCTION validacao_periodo ()
	RETURNS trigger AS $validacao_periodo$
	BEGIN
		IF (NEW."inicioMatricula" >= NEW."finalMatricula") THEN
			RAISE EXCEPTION 'Data inicial de matrícula é maior ou igual a data final';
		END IF;
		RETURN NEW;
	END;
$validacao_periodo$ LANGUAGE plpgsql;

CREATE TRIGGER novo_periodo BEFORE INSERT OR UPDATE ON academico_periodo
	FOR EACH ROW EXECUTE PROCEDURE validacao_periodo();
	
INSERT INTO academico_periodo(semestre, "inicioMatricula", "finalMatricula")
VALUES ('2020.1', '2018-01-01', '2018-01-30');

INSERT INTO academico_periodo(semestre, "inicioMatricula", "finalMatricula")
VALUES ('2020.2', '2018-06-30', '2018-06-01');


CREATE OR REPLACE FUNCTION validacao_turma ()
	RETURNS trigger AS $validacao_turma$
	DECLARE
		disciplina VARCHAR;
		periodo VARCHAR;
		
	BEGIN
		SELECT nome INTO disciplina FROM academico_disciplina WHERE id = NEW.disciplina_id;
		SELECT semestre INTO periodo FROM academico_periodo WHERE semestre = NEW.periodo_id;

		IF ((SELECT COUNT(*) FROM TurmaPeriodo(disciplina, periodo)) >= 30) THEN
			RAISE EXCEPTION 'A turma % já atingiu o limite máximo de alunos (30)', disciplina;
		END IF;

		RETURN NEW;
	END;
$validacao_turma$ LANGUAGE plpgsql;

CREATE TRIGGER validacao_turma BEFORE INSERT OR UPDATE ON academico_turma
	FOR EACH ROW EXECUTE PROCEDURE validacao_turma();

INSERT INTO academico_turma (disciplina_id, matricula_id, periodo_id)
VALUES (36, '70644381272', '2018.2');


CREATE OR REPLACE FUNCTION periodo_matricula ()
	RETURNS trigger AS $periodo_matricula$
	DECLARE
		disciplina VARCHAR;
		periodo VARCHAR;
		dataAtual DATE;
		dataInicio DATE;
		dataFinal DATE;
	BEGIN
		SELECT nome INTO disciplina FROM academico_disciplina WHERE id = NEW.disciplina_id;
		SELECT semestre INTO periodo FROM academico_periodo WHERE semestre = NEW.periodo_id;
		
		SELECT NOW() INTO dataAtual;
		SELECT "inicioMatricula" INTO dataInicio FROM academico_periodo WHERE semestre = periodo;
		SELECT "finalMatricula" INTO dataFinal FROM academico_periodo WHERE semestre = periodo;
		IF (dataAtual < dataInicio) THEN
			RAISE EXCEPTION 'Espere pela abertura do período de matrícula';
		END IF;
		IF (dataAtual > dataFinal) THEN
			RAISE EXCEPTION 'O período de matrícula já foi finalizado';
		END IF;
		RETURN NEW;
	END;
$periodo_matricula$ LANGUAGE plpgsql;

CREATE TRIGGER periodo_matricula BEFORE INSERT OR UPDATE ON academico_turma
	FOR EACH ROW EXECUTE PROCEDURE periodo_matricula();

INSERT INTO academico_turma (disciplina_id, matricula_id, periodo_id)
VALUES (36, '85726672291', '2019.1');

INSERT INTO academico_turma (disciplina_id, matricula_id, periodo_id)
VALUES (36, '85726672291', '2018.2');