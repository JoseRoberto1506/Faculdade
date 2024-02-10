-- JOIN com WHERE
SELECT carros.marca
FROM carros, marcas
WHERE carros.marca = marcas.marca;

-- INNER JOIN
SELECT m.marca, c.carro
FROM marcas as m INNER JOIN carros as c
ON m.marca = c.marca;

-- NATURAL JOIN
SELECT marca, carro
FROM marcas NATURAL JOIN carros;

-- LEFT JOIN
SELECT m.marca, c.carro
FROM marcas as m LEFT JOIN carros as c
ON m.marca = c.marca;

-- LEFT JOIN exclusivo
SELECT m.marca, c.carro
FROM marcas as m LEFT JOIN carros as c
ON m.marca = c.marca
WHERE c.marca IS NULL;

-- RIGHT JOIN
SELECT m.marca, c.carro
FROM marcas as m RIGHT JOIN carros as c
ON m.marca = c.marca;

-- RIGHT JOIN exclusivo
SELECT m.marca, c.carro
FROM marcas as m RIGHT JOIN carros as c
ON m.marca = c.marca
WHERE m.marca IS NULL;

-- FULL OUTER JOIN com RIGHT JOIN exclusivo
SELECT m.marca, c.carro
FROM marcas as m LEFT JOIN carros as c
ON m.marca = c.marca
UNION ALL
SELECT m.marca, c.carro
FROM marcas as m RIGHT JOIN carros as c
ON m.marca = c.marca
WHERE m.marca IS NULL;

-- FULL OUTER JOIN com LEFT JOIN exclusivo
SELECT m.marca, c.carro
FROM marcas as m LEFT JOIN carros as c
ON m.marca = c.marca
WHERE c.marca IS NULL
UNION ALL
SELECT m.marca, c.carro
FROM marcas as m RIGHT JOIN carros as c
ON m.marca = c.marca;

-- FULL OUTER JOIN exclusivo
SELECT m.marca, c.carro
FROM marcas as m LEFT JOIN carros as c
ON m.marca = c.marca
WHERE c.marca IS NULL
UNION ALL
SELECT m.marca, c.carro
FROM marcas as m RIGHT JOIN carros as c
ON m.marca = c.marca
WHERE m.marca IS NULL;

-- CROSS JOIN
SELECT m.marca, c.carro
FROM marcas as m CROSS JOIN carros as c;

-- Obter o CPF dos funcionários do departamento 5 e o CPF dos supervisores dos funcionários do departamento 5.
SELECT Cpf FROM funcionario WHERE Dnr = 5
UNION
SELECT Cpf_supervisor FROM funcionario WHERE Dnr = 5;

/* Obter os nomes de todos os projetos que envolvem algum funcionário cujo sobrenome é ‘Wong’ como trabalhador vinculado ao projeto OU como gerente do 
departamento que controla o projeto. */
SELECT Projnome
FROM projeto, trabalha_em, funcionario
WHERE Unome = 'Wong' 
AND Fcpf = Cpf AND Projnumero = Pnr
UNION
SELECT Projnome
FROM projeto, departamento, funcionario
WHERE Unome = 'Wong' 
AND Cpf_gerente = Cpf AND Dnum = Dnumero;

-- Para cada funcionário, obtenha o nome do funcionário e o nome de seu supervisor (retornar os nulos).
SELECT f.Pnome as Nome_Funcionário, s.Pnome as Nome_Supervisor
FROM funcionario as f LEFT JOIN funcionario as s
ON f.Cpf_supervisor = s.Cpf;