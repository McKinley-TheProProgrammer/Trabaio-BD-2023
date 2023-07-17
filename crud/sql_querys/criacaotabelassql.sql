
CREATE TABLE IF NOT EXISTS Usuario (
	id SERIAL PRIMARY KEY, 
    matricula INT NOT NULL UNIQUE,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL,
    senha VARCHAR(150) NOT NULL,
    curso VARCHAR(150) NOT NULL
    
);

CREATE TABLE IF NOT EXISTS Departamento(
	id SERIAL,
    codigo_depto INT NOT NULL,
    nome VARCHAR(150) NOT NULL,
    PRIMARY KEY(codigo_depto)
);


CREATE TABLE IF NOT EXISTS Disciplina(
	id SERIAL,
    cod_disciplina VARCHAR(30) NOT NULL,
    nome VARCHAR(150) NOT NULL,
    codigo_depto INT NOT NULL,
    FOREIGN KEY (codigo_depto) REFERENCES Departamento(codigo_depto),
    PRIMARY KEY(cod_disciplina)
);


CREATE TABLE IF NOT EXISTS Turma(
	id SERIAL PRIMARY KEY,
    turma VARCHAR(2) NOT NULL,
    periodo VARCHAR(30) NOT NULL,
    professor VARCHAR(100),
    horario TEXT,
    vagas_ocupadas INT NOT NULL,
    total_vagas INT NOT NULL,
    cod_disciplina VARCHAR(30) NOT NULL,
    cod_depto INT NOT NULL,
    FOREIGN KEY (cod_disciplina) REFERENCES Disciplina(cod_disciplina),
	FOREIGN KEY (cod_depto) REFERENCES Departamento(codigo_depto)
);


CREATE TABLE IF NOT EXISTS Nota(
    usuario_id SERIAL PRIMARY KEY,
    nota_disciplina INT NOT NULL,
    descricao VARCHAR(10000) NOT NULL,
    dataDePostagem TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id) ON DELETE CASCADE
);