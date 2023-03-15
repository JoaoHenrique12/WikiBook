\i docker-entrypoint-initdb.d/types.sql

CREATE TABLE IF NOT EXISTS users (
  id BIGSERIAL,
  username varchar(75) UNIQUE NOT NULL,
  password char(64) NOT NULL,
  like_read boolean NOT NULL,
  gender gender,
  birth date NOT NULL,
  state state NOT NULL,

  image_link varchar(150),
  descricao text
);
/*
CREATE TABLE IF NOT EXISTS artigo (
  titulo varchar(50) PRIMARY KEY,
  dataCriacao date NOT NULL,
  qtdEdicoes integer NOT NULL DEFAULT 1,
  qtdPalavras bigint NOT NULL,
  qtdSubtitulos integer NOT NULL,
  qtdLinks integer NOT NULL,
  qtdImagens integer NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria (
  titulo varchar(50) PRIMARY KEY
);

-- Tabelas de relacionamentos.

-- Auto relacionamentos
CREATE TABLE IF NOT EXISTS pessoa_segue_pessoa (
  pessoa_segue varchar(75) NOT NULL,
  pessoa_seguida varchar(75) NOT NULL,

  CONSTRAINT FK_pessoa_segue_pessoa_seguidor FOREIGN KEY(pessoa_segue) REFERENCES pessoa(username),
  CONSTRAINT FK_pessoa_segue_pessoa_seguido FOREIGN KEY(pessoa_seguida) REFERENCES pessoa(username),

  CONSTRAINT PK_pessoa_segue_pessoa PRIMARY KEY (pessoa_segue,pessoa_seguida)
);

CREATE TABLE IF NOT EXISTS categoria_possui_categoria (
  titulo_dono varchar(50) NOT NULL,
  titulo_subcategoria varchar(50) NOT NULL,

  CONSTRAINT FK_categoria_possui_categoria_dono FOREIGN KEY(titulo_dono) REFERENCES categoria(titulo),
  CONSTRAINT FK_categoria_possui_categoria_subcategoria FOREIGN KEY(titulo_subcategoria) REFERENCES categoria(titulo),

  CONSTRAINT PK_categoria_possui_categoria PRIMARY KEY (titulo_dono,titulo_subcategoria)
);

-- Relacionamentos interage.

CREATE TABLE IF NOT EXISTS pessoa_interage_artigo (
  username varchar(75) NOT NULL,
  titulo varchar(50) NOT NULL,
  ofensivo boolean NOT NULL,
  gostei boolean NOT NULL,
  acesso timestamp NOT NULL DEFAULT NOW(),

  CONSTRAINT FK_pessoa_interage_artigo_username FOREIGN KEY(username) REFERENCES pessoa(username),
  CONSTRAINT FK_pessoa_interage_artigo_titulo FOREIGN KEY(titulo) REFERENCES artigo(titulo),

  CONSTRAINT PK_pessoa_interage_artigo PRIMARY KEY(username,titulo)
);

CREATE TABLE IF NOT EXISTS pessoa_interage_categoria (
  username varchar(75) NOT NULL,
  titulo varchar(50) NOT NULL,
  ofensivo boolean NOT NULL,
  gostei boolean NOT NULL,
  acesso timestamp NOT NULL DEFAULT NOW(),

  CONSTRAINT FK_pessoa_interage_categoria_username FOREIGN KEY(username) REFERENCES pessoa(username),
  CONSTRAINT FK_pessoa_interage_categoria_titulo FOREIGN KEY(titulo) REFERENCES categoria(titulo),

  CONSTRAINT PK_pessoa_interage_categoria PRIMARY KEY(username,titulo)
);

-- Relacionamentos comuns.
CREATE TABLE IF NOT EXISTS pessoa_le_artigo (
  username varchar(75) NOT NULL,
  titulo varchar(50) NOT NULL,
  acesso timestamp NOT NULL DEFAULT NOW(),
  tempoLido time,

  CONSTRAINT FK_pessoa_le_artigo_username FOREIGN KEY(username) REFERENCES pessoa(username),
  CONSTRAINT FK_pessoa_le_artigo_titulo FOREIGN KEY(titulo) REFERENCES artigo(titulo),

  CONSTRAINT PK_pessoa_le_artigo PRIMARY KEY(username,titulo,acesso)
);

CREATE TABLE IF NOT EXISTS artigo_pertence_categoria (
  titulo_artigo varchar(50) NOT NULL,
  titulo_categoria varchar(50) NOT NULL,

  CONSTRAINT FK_artigo_pertence_categoria_titulo_artigo FOREIGN KEY(titulo_artigo) REFERENCES artigo(titulo),
  CONSTRAINT FK_artigo_pertence_categoria_titulo_categoria FOREIGN KEY(titulo_categoria) REFERENCES categoria(titulo),

  CONSTRAINT PK_artigo_pertence_categoria PRIMARY KEY(titulo_categoria,titulo_artigo)
);

*/
