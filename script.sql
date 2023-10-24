CREATE DATABASE CONTACTO;

use CONTACTO;

CREATE TABLE Personas (
    nombre_completo VARCHAR(100) NOT NULL,
    numero_documento BIGINT PRIMARY KEY,
    direccion VARCHAR(200) NOT NULL
);

CREATE TABLE Telefonos (
    persona_id BIGINT,
    numero_telefono BIGINT PRIMARY KEY,
    FOREIGN KEY (persona_id) REFERENCES Personas(numero_documento)
);
CREATE TABLE Emails (
    persona_id BIGINT,
    email VARCHAR(100) PRIMARY KEY,
    FOREIGN KEY (persona_id) REFERENCES Personas(numero_documento)
);