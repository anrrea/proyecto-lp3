CREATE TABLE ciudades(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

	CREATE TABLE marcas(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

	CREATE TABLE paises(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

	CREATE TABLE clientes (
     id INT PRIMARY KEY,
      nombre VARCHAR(100),
      correo VARCHAR(100),
      telefono VARCHAR(15)
    );

    CREATE TABLE productos (
    id INT PRIMARY KEY,
     nombre VARCHAR(100),
     descripcion TEXT,
     precio DECIMAL(10, 2)
    );

    CREATE TABLE empleados (
     id INT PRIMARY KEY,
     nombre VARCHAR(100),
     puesto VARCHAR(100)
    );

	CREATE TABLE sucursales (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(255)
    );

    CREATE TABLE impuestos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    tasa DECIMAL(5, 2)
    );

    CREATE TABLE descuentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    porcentaje DECIMAL(5, 2)
    );

    CREATE TABLE categorias (
    id INT PRIMARY KEY,
    nombre VARCHAR(100)
    );

    CREATE TABLE depositos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(255)
    );

    CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE,
    contrasena VARCHAR(100),
    nombre_completo VARCHAR(100),
    correo VARCHAR(100),
    rol VARCHAR(50)
    );

    CREATE TABLE cajas (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    sucursal_id INT,
    saldo_actual DECIMAL(10, 2),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(id)
    );

    CREATE TABLE proveedores (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    contacto VARCHAR(100),
    direccion VARCHAR(255),
    telefono VARCHAR(15)
    );

    CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    fecha DATE,
    cliente_id INT,
    total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    );

    CREATE TABLE devoluciones (
    id SERIAL PRIMARY KEY,
    venta_id INT,
    fecha DATE,
    motivo TEXT
);


