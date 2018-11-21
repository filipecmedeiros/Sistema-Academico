CREATE OR REPLACE FUNCTION TurmaPeriodo (disciplina VARCHAR(255), periodo VARCHAR(255))

	RETURNS TABLE (matricula VARCHAR(6), nome VARCHAR(255)) as $$
	BEGIN
			RETURN QUERY
			SELECT M.matricula, A.nome
			FROM academico_matricula M, academico_turma T,
				 academico_disciplina D, academico_aluno A, academico_periodo P
			WHERE D.nome = disciplina AND
				T.disciplina_id = D.id AND
				P.semestre = periodo AND
				M.matricula = T.matricula_id AND
				A.cpf = M.matricula;
	END;
$$  LANGUAGE plpgsql;
													  
SELECT * FROM TurmaPeriodo ('ALGEBRA LINEAR I', '2018.2');

CREATE OR REPLACE FUNCTION MatriculaDisciplinas (matricula VARCHAR, disciplina_id INT[], periodo VARCHAR(6))
	RETURNS VOID AS $MatriculaDisciplinas$
	DECLARE
		disc INT;
		BEGIN
			FOREACH disc IN ARRAY disciplina_id LOOP
				INSERT INTO academico_turma (matricula_id, disciplina_id, periodo_id) 
				VALUES (matricula, disc, periodo);
			END LOOP;
			EXCEPTION WHEN check_violation THEN
				RAISE;
		COMMIT;

	END;
$MatriculaDisciplinas$ LANGUAGE plpgsql;
 
SELECT MatriculaDisciplinas ('68965320259', '{2, 3, 36}', '2018.2');

