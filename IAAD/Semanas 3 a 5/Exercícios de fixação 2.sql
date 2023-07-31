-- Apresente o comando SQL que retorna os nomes e localizações (cidades) de todos os projetos vinculados ao departamento Pesquisa, cujas localizações iniciam com a letra 'S'.
SELECT Projnome, Projlocal
FROM projeto, departamento
WHERE Dnum = Dnumero AND Dnome = 'Pesquisa' AND Projlocal LIKE 'S%';

-- Insira na tabela "projeto” as informações abaixo (apresente o comando SQL de inserção), em seguida execute novamente o comando da letra A e apresente a tabela resultante.
INSERT INTO `empresa_seunome`.`projeto` (`Projnome`, `Projnumero`, `Projlocal`, `Dnum`) VALUES ('ProjetoBSI', '40', 'Salvador', '5');

-- -- Apresente o comando SQL que retorna os nomes de todos(as) funcionários(as) que são supervisionados diretamente por Fernando. Apresente também a tabela resultante.
SELECT f.Pnome
FROM funcionario AS f, funcionario AS s
WHERE f.Cpf_supervisor = s.Cpf AND s.Pnome = 'Fernando';

-- Apresente o comando SQL que retorna os nomes dos departamentos e os nomes dos gerentes, mas apenas os departamentos gerenciados por homens. Apresente também a tabela resultante.
SELECT Dnome, Pnome
FROM departamento, funcionario
WHERE Cpf_gerente = Cpf AND Sexo = 'M';

/* Apresente o comando SQL que retorna os nomes dos(as) funcionários(as) e respectivos nomes dos projetos em que eles(as) atuam. Considerar apenas os projetos vinculados ao departamento 
cujo gerente é uma mulher, além disso, considerar apenas os(as) funcionários(as) que trabalham mais de 25 horas por semana */
SELECT func.Pnome, Projnome
FROM departamento, projeto, trabalha_em, funcionario AS func, funcionario AS sup
WHERE Dnumero = Dnum AND Cpf_gerente = sup.Cpf AND sup.Sexo = 'F'
AND Fcpf = func.Cpf AND Pnr = Projnumero AND Horas > 25.0;
