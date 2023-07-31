-- Apresente a consulta SQL que liste os nomes dos programadores e os nomes das startups que eles são vinculados.
SELECT nome_programador, nome_startup
FROM programador as p, startup as s
WHERE p.id_startup = s.id_startup;

-- Apresente a consulta SQL que liste os nomes dos(as) programadores(as) que programam em Java ou C.
SELECT nome_programador
FROM linguagem_programacao as lp, programador_linguagem as pl, programador as p
WHERE p.id_programador = pl.id_programador AND pl.id_linguagem = lp.id_linguagem
AND (lp.nome_linguagem = 'Java' OR lp.nome_linguagem = 'C');

-- Listar o nome e data de nascimento (no formato dd/mm/aaaa) de cada programadora cadastrada no BD Startup (apenas gênero feminino).
SELECT nome_programador, date_format(data_nascimento, '%d/%m/%Y') as 'data de nascimento'
FROM programador
WHERE genero = 'F';

-- Listar os nomes dos(as) programadores(as) que programam em PHP e nasceram entre 1980 e 1990.
SELECT nome_programador
FROM linguagem_programacao as lp, programador_linguagem as pl, programador as p
WHERE p.id_programador = pl.id_programador AND pl.id_linguagem = lp.id_linguagem
AND lp.nome_linguagem = 'PHP' AND (year(data_nascimento) BETWEEN 1980 AND 1990);

-- Listar os nomes dos(as) programadores(as) vinculados à startup “BSI Next Level” que tem menos de 35 anos.
SELECT nome_programador
FROM programador AS p, startup as s
WHERE p.id_startup = s.id_startup
AND nome_startup = 'BSI Next Level'
AND timestampdiff(year, p.data_nascimento, curdate()) <= 35;

/* Apresente a consulta SQL que lista o nome de cada programador(a), a data de nascimento no formato dd/mm/aaaa, a data de nascimento por extenso e 
a idade atual. */
SET LOCAL lc_time_names = 'pt_BR';
SELECT nome_programador, date_format(data_nascimento, '%d/%m/%Y') as 'dd/mm/aaaa', 
date_format(data_nascimento, '%d de %M de %Y') as Data_por_Extenso,  timestampdiff(year, data_nascimento, curdate()) as 'Idade'
FROM programador;

/* Apresente a consulta SQL que lista os nomes dos(as) programadores(as), suas idades, e os nomes das startups em que estão vinculados(as), mas 
APENAS os programadores(as) que estejam vinculados(as) às startups “Smart123” ou “BSI Next Level” e tenham atualmente entre 30 e 40 anos. */
SELECT nome_programador, timestampdiff(year, data_nascimento, curdate()) as idade, nome_startup
FROM programador as p, startup as s
WHERE p.id_startup = s.id_startup
AND (nome_startup = 'Smart123' OR nome_startup = 'BSI Next Level')
AND (timestampdiff(year, p.data_nascimento, curdate()) BETWEEN 30 AND 40);
