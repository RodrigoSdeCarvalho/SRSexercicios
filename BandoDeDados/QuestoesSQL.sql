-- Testado no SQlite. Em https://sqliteonline.com/

-- O CPF é a chave primária da tabela Pessoa, pois não pode haver duas pessoas com o mesmo CPF.

CREATE TABLE Pessoa (
    CPF VARCHAR(11) NOT NULL PRIMARY KEY,
    NomeCompleto VARCHAR(100) NOT NULL,
    Idade INT NOT NULL,
    Telefone VARCHAR(11) NOT NULL
);

CREATE TABLE Cargos (
    IdCargo INTEGER NOT NULL PRIMARY KEY,
    Cargo VARCHAR(100) NOT NULL,
    SalarioPadrao DECIMAL(10, 2) NOT NULL
);

CREATE TABLE PessoaCargo (
    CPF VARCHAR(11) NOT NULL,
    IdCargo INTEGER NOT NULL,
    Salario DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (CPF, IdCargo),
    FOREIGN KEY (CPF) REFERENCES Pessoa (CPF),
    FOREIGN KEY (IdCargo) REFERENCES Cargos (IdCargo)
);

INSERT INTO Cargos (IdCargo, Cargo, SalarioPadrao) VALUES
(1, 'Dev Front-End', 4000.00),
(2, 'Dev Back-End', 4000.00),
(3, 'Gerente', 15000.00),
(4, 'Estagiário', 2000.00),
(5, 'Engenheiro de Machine Learning', 4000.00);

INSERT INTO Pessoa (CPF, NomeCompleto, Idade, Telefone) VALUES
('10668794941', 'Octávio Santos', 30, '47996960576'),
('10844565645', 'José Pereira', 25, '48998984521'),
('10047456552', 'Júlia Silva', 40, '11987654456'),
('15540843047', 'Maria Santana', 22, '15995653210');

INSERT INTO PessoaCargo (CPF, IdCargo, Salario) VALUES
('10668794941', 4, 2000.00),
('10668794941', 5, 2000.00),
('10844565645', 3, 17000.00),
('10047456552', 1, 4000.00),
('15540843047', 2, 4500.00);

SELECT Pessoa.NomeCompleto, SUM(PessoaCargo.Salario) AS SalarioTotal, SUM(Cargos.SalarioPadrao) AS SalarioPadraoTotal
FROM Pessoa
LEFT JOIN PessoaCargo ON Pessoa.CPF = PessoaCargo.CPF
LEFT JOIN Cargos ON PessoaCargo.IdCargo = Cargos.IdCargo
GROUP BY Pessoa.NomeCompleto
ORDER BY SalarioTotal ASC;
