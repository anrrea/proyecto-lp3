CREATE TABLE ciudades (
    ciudad_id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) unique 
);

SELECT id, descripcion 
FROM ciudades;

CREATE TABLE paises (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE nacionalidades (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,        
    descripcion VARCHAR(255) UNIQUE, 
    cantidad INTEGER NOT NULL,         
    precio_unitario DECIMAL(10, 2) NOT NULL 
);

CREATE TABLE personas (
    id_persona SERIAL PRIMARY KEY,  
    nombres VARCHAR(100) NOT NULL,  
    apellidos VARCHAR(100) NOT NULL,  
    nro_cedula INTEGER NOT NULL UNIQUE,  
    fecha_nacimiento DATE NOT NULL,  
    direccion VARCHAR(255) NOT NULL  
);

CREATE TABLE proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    id_persona INTEGER,  
    ruc VARCHAR(20) NOT NULL,  
    razon_social VARCHAR(150) NOT NULL,  
    registro DATE NOT NULL,  
    estado VARCHAR(20) NOT NULL,  
    FOREIGN KEY (id_persona) REFERENCES personas(id_persona) 
);

CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,         
    id_persona INTEGER,                    
    nombre VARCHAR(100) NOT NULL,          
    apellido VARCHAR(100) NOT NULL,        
    cedula VARCHAR(20) NOT null UNIQUE,           
    direccion VARCHAR(255),                 
    telefono VARCHAR(20),                   
    fecha_registro DATE NOT NULL ,  
    FOREIGN KEY (id_persona) REFERENCES personas(id_persona) ON DELETE SET null
);

CREATE TABLE sucursales (
    id_sucursal SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT null UNIQUE,
    direccion VARCHAR(200) NOT NULL,
    telefono integer not null
);

CREATE TABLE depositos (
    id_deposito SERIAL PRIMARY KEY,
    id_sucursal INTEGER,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono INTEGER,
    capacidad INTEGER,
    FOREIGN KEY (id_sucursal) REFERENCES sucursales(id_sucursal) ON DELETE SET null
);

CREATE TABLE estado_civil (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) NOT NULL
);

CREATE TABLE sexo (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) NOT NULL
);

CREATE TABLE marcas (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) NOT NULL
);

CREATE TABLE tipo_producto (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) NOT NULL
);
