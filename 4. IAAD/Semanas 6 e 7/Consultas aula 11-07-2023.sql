/* Retorne os nomes de todos(as) programadores(as) e os nomes das respectivas startups em que eles(elas) trabalham. Apresente a consulta de três formas: 
(I) junção na cláusula where, (II) conexão interna (inner join), (III) junção natural. */

-- (I) Junção na cláusula where
SELECT nome_programador, nome_startup
FROM programador as p, startup as s
WHERE p.id_startup = s.id_startup;

-- (II) Inner join
SELECT nome_programador, nome_startup
FROM programador as p INNER JOIN startup as s
ON p.id_startup = s.id_startup;

-- (III) Natural Join
SELECT nome_programador, nome_startup
FROM programador NATURAL JOIN startup;

/* Retorne os nomes e identificadores dos(as) programadores(as) que não programam nas linguagens de programação cadastradas no BD Startup. 
Apresente a consulta de três formas: (I) left join (exclusiva), (II) not in, (III) not exists. */

-- (I) Left join exclusivo
SELECT p.nome_programador, p.id_programador
FROM programador as p LEFT JOIN programador_linguagem as pl
ON p.id_programador = pl.id_programador
WHERE pl.id_linguagem IS NULL;

-- (II) Not in
SELECT nome_programador, id_programador
FROM programador
WHERE id_programador NOT IN (SELECT id_programador FROM programador_linguagem);

-- (III) Not exists
SELECT nome_programador, id_programador
FROM programador as p
WHERE NOT EXISTS (SELECT * FROM programador_linguagem as pl WHERE p.id_programador = pl.id_programador);

/* Retorne o nome de cada startup e a quantidade de programadores(as) de cada uma delas. Inclua na consulta as startups com zero programadores. */
SELECT nome_startup, count(id_programador) as quantidade_de_programadores
FROM startup NATURAL LEFT JOIN programador
GROUP BY id_startup;

/* Retorne o nome de cada startup e o nomes dos programadores que trabalham nelas. */
SELECT nome_startup, group_cONcat(" ", nome_programador) as nomes_programadores
FROM startup NATURAL LEFT JOIN programador
GROUP BY id_startup;

/* Retorne o código e nome de cada linguagem de programação (LP), seguido do número de programadores(as) (quantidade total) que programam na LP. Devem 
aparecer no resultado da consulta apenas as LP com mais de 1 programador(a). Ou seja, retornar as linguagens de programação que têm mais de um(a) programador(a). */
SELECT id_linguagem, nome_linguagem, count(id_programador) as quantidade_de_programadores
FROM linguagem_programacao NATURAL LEFT JOIN programador_linguagem
GROUP BY id_linguagem
HAVING count(id_programador) > 1;

/* Especifique uma visão (view) em SQL que obtenha para cada departamento: o nome do departamento, nome do gerente, quantidade de funcionários, total de 
salários, menor salário, maior salário e média de salários. */
-- OBS.: Visões são tabelas temporárias.
CREATE VIEW relatorio_departamento
AS SELECT Dnome as nome_departamento,
g.Pnome as nome_gerente,
COUNT(f.Cpf) as quantidade_funciONarios,
SUM(f.Salario) as total_salario,
MIN(f.Salario) as menor_salario,
MAX(f.Salario) as maior_salario,
AVG(f.Salario) as média_salario
FROM departamento LEFT JOIN funciONario as f ON Dnumero = f.Dnr
LEFT JOIN funciONario as g ON g.Cpf = Cpf_gerente
GROUP BY Dnome;

SELECT * FROM relatorio_departamento;

/* Sobre a visão definida acima, retorne o(s) departamento(s) com mais de um funcionário e cuja média de salário seja maior que R$ 32.000. */
SELECT nome_departamento
FROM relatorio_departamento
WHERE quantidade_funciONarios > 1 AND média_salario > 32000;
