-- Table: destinos_administrador

-- DROP TABLE destinos_administrador;

CREATE TABLE destinos_administrador
(
  id serial NOT NULL,
  username character varying(15) NOT NULL,
  password character varying(15) NOT NULL,
  e_mail character varying(50) NOT NULL,
  CONSTRAINT destinos_administrador_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE destinos_administrador
  OWNER TO postgres;
