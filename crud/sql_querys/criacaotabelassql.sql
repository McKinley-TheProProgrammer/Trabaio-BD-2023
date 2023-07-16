CREATE TABLE IF NOT EXISTS Usuario (
	id SERIAL, 
    matricula INT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(150),
    senha VARCHAR(150),
    curso VARCHAR(150)
    
);

CREATE TABLE IF NOT EXISTS Departamento(
	id SERIAL,
    codigo_depto VARCHAR(7),
    nome VARCHAR(150) ,
    PRIMARY KEY(codigo_depto)
);


CREATE TABLE IF NOT EXISTS Disciplina(
	id SERIAL,
    cod_disciplina VARCHAR(7),
    nome VARCHAR(150) ,
    codigo_depto VARCHAR(7),
    FOREIGN KEY (codigo_depto) REFERENCES Departamento(codigo_depto),
    PRIMARY KEY(cod_disciplina)
);


CREATE TABLE IF NOT EXISTS Turma(
	id SERIAL,
    cod_disciplina varchar(7),
    cod_depto varchar(7),
    FOREIGN KEY (cod_disciplina) REFERENCES Disciplina(cod_disciplina),
	FOREIGN KEY (cod_depto) REFERENCES Departamento(codigo_depto)
);

CREATE TABLE IF NOT EXISTS Nota(
    usuario_id SERIAL,
    usuario_mat INT PRIMARY KEY,
    usuario_nome VARCHAR(50),
    descricao VARCHAR(10000),
    dataDePostagem TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_mat) REFERENCES Usuario(matricula),
	FOREIGN KEY (usuario_nome) REFERENCES Usuario(nome)
    
);