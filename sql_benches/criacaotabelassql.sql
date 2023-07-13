CREATE TABLE Usuario (
	id int,
    matricula int,
    nome varchar(50),
    email varchar(150) unique key,
    senha varchar(150),
    curso varchar(150),
    primary key(matricula)

);

CREATE TABLE Departamento(
	id int,
    codigo_depto varchar(7) primary key,
    nome varchar(150) 
);


CREATE TABLE Discplina(
	id int,
    codigo varchar(7) primary key,
    nome varchar(150) ,
    codigo_depto varchar(3),
    foreign key (codigo_depto) references Departamento.codigo_depto
);


CREATE TABLE Turma(
	id int primary key,
    cod_disciplina varchar(7),
    cod_depto varchar(7),
    foreign key (cod_disciplina) references Disciplina.codigo ,
	foreign key (cod_depto) references Departamento.codigo
);

CREATE TABLE Nota(
	id int primary key,
    descricao varchar(10000),
    dataDePostagem datetime,
    foreign key (usuario_id) references Usuario.id,
    foreign key (usuario_mat) references Usuario.mat,
    foreign key (usuario_nome) references Usuario.nome
	
);