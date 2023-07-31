-- Obter o nome (primeiro e último), data de nascimento e endereço dos funcionários que ganham 30.000 ou mais.
SELECT Pnome, Unome, Datanasc, Endereco
FROM funcionario
WHERE Salario >= 30000;

-- Obter todas as informações dos funcionários que ganham 30.000 ou mais.
SELECT * FROM funcionario WHERE Salario >= 30000;

-- Obter a data de nascimento e o endereço do funcionário cujo nome é João B. Silva.
SELECT Datanasc, Endereco
FROM funcionario
WHERE Pnome = 'João' AND Minicial = 'B' AND Unome = 'Silva';

-- Obter o nome e endereço de todos os funcionários que trabalham para o departamento Pesquisa.
SELECT Pnome, Endereco
FROM funcionario, departamento
WHERE Dnr = Dnumero AND Dnome = 'Pesquisa';

/* Para cada projeto localizado em São Paulo, listar o número do projeto, nome do projeto, número e nome do departamento de controle, 
e nome do gerente do departamento. */
SELECT Projnumero, Projnome, Dnum, Dnome, Pnome
FROM projeto, departamento, funcionario
WHERE Dnum = Dnumero AND Projlocal = 'São Paulo' AND Cpf_gerente = Cpf;

-- Consulta com DISTINCT
SELECT DISTINCT Cpf_supervisor
FROM funcionario
WHERE Dnr = 5;
/* A consulta abaixo retornaria valores repetidos:
SELECT Cpf_supervisor
FROM funcionario
WHERE Dnr = 5; */

-- Consulta com ordenação
/* Ordem ascendente/crescente (padrão).
SELECT Salario
FROM funcionario
ORDER BY Salario; */
-- Ordem descendente/decrescente.
SELECT Salario
FROM funcionario
ORDER BY Salario Desc;

-- Ordenação de mais de um atributo.
SELECT Salario, Pnome, Unome
FROM funcionario
ORDER BY Salario, Pnome;

-- Obter os nome dos funcionários cujo último nome inicia com L.
SELECT Pnome, Unome
FROM funcionario
WHERE Unome LIKE 'L%'; -- O LIKE não é case-sensitive.

-- Obter os nomes dos projetos que terminam com a palavra 'ação'.
SELECT Projnome
FROM projeto
WHERE Projnome LIKE '%ação';

-- Obter os nomes dos funcionários que nasceram nos mêsde janeiro.
SELECT Pnome, Unome, Datanasc
FROM funcionario
WHERE Datanasc LIKE '_____01___';

/* Para cada funcionário, obtenha o nome do funcionário e o nome de seu supervisor.
OBS: Neste caso tem-se um autorrelacionamento, sendo necessário o uso de alias (pseudônimo/apelido). */
SELECT f.pnome AS Nome_Funcionário, s.pnome AS Nome_Supervisor
FROM funcionario AS f, funcionario AS s
WHERE f.Cpf_supervisor = s.Cpf;

-- Consulta com LIMIT
SELECT * FROM funcionario LIMIT 5;
-- Exibir a partir do 5º registro, limitando a 3 linhas. Recuperar 3 registros, a partir do 5º registro.
-- SELECT * FROM funcionario LIMIT 5, 3;