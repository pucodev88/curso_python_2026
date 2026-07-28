# 🐍 Curso de Programación con Python

Bienvenidos al repositorio del curso de **Programación con Python**.
En este espacio se almacenarán los ejercicios, ejemplos, actividades y avances del proyecto que desarrollaremos durante las clases.

## 📌 Descripción del curso
Este curso tiene como objetivo enseñar los fundamentos de la programación utilizando Python.
Durante las clases aprenderemos a analizar problemas, crear algoritmos, escribir código, utilizar Git y GitHub, trabajar con bases de datos y desarrollar un
proyecto integrador.

## 🎯 Objetivos
Al finalizar el curso, los estudiantes podrán:
* Comprender los conceptos básicos de programación.
* Crear programas utilizando Python.
* Utilizar variables, operadores y estructuras de control.
* Crear funciones y organizar el código.
* Trabajar con listas, tuplas, diccionarios y archivos.
* Utilizar Git y GitHub para controlar versiones.
* Crear y administrar entornos virtuales.
* Conectarse a bases de datos.
* Desarrollar un proyecto práctico.

## 📚 Contenidos principales
1. Introducción a la programación.
2. Instalación y configuración de Python.
3. Uso de Visual Studio Code.
4. Variables y tipos de datos.
5. Entrada y salida de información.
6. Operadores.
7. Condicionales.
8. Bucles.
9. Funciones.
10. Colecciones de datos.
11. Manejo de errores.
12. Archivos.
13. Git y GitHub.
14. Bases de datos.
15. Desarrollo de un proyecto.

## 🛠️ Herramientas
Para trabajar en el curso utilizaremos:
* Python
* Visual Studio Code
* Git
* GitHub
* PostgreSQL
* Django
* FastAPI

## ✅ Requisitos
Antes de comenzar, verifica que tengas instalado:

```bash
python --version
```

```bash
git --version
```
También debes tener instalado **Visual Studio Code**.

## 📂 Estructura del repositorio

│   README.md
│   
├───ejercicios
│       01_hola_python.py
│       02_variables.py
│       03_entrada_salida.py
│       04_conversiones.py
│       05_operadores.py
│       06_fstrings.py
│       07_idea_proyecto.py
│       
└───proyecto_integrador

### Descripción de las carpetas

* `ejercicios/`: ejercicios desarrollados durante las clases.
* `proyecto/`: código del proyecto integrador.
* `recursos/`: diapositivas, documentos y material de apoyo.
* `tareas/`: actividades enviadas para trabajo autónomo.

## 🚀 Cómo utilizar este repositorio

### 1. Clonar el repositorio

```bash
git clone https://github.com/pucodev88/nombre-del-repositorio.git
```

### 2. Ingresar a la carpeta

```bash
cd nombre-del-repositorio
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual en Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Ejecutar un archivo de Python

```bash
python ejercicios/01_hola_mundo.py
```

---

## 🧪 Primer ejercicio

Crea un archivo llamado `01_hola_mundo.py`:

```python
print("Hola, mundo")
print("Bienvenidos al curso de Python")
```

Para ejecutarlo:

```bash
python ejercicios/01_hola_mundo.py
```

## 💾 Comandos básicos de Git

Ver el estado del repositorio:

```bash
git status
```

Agregar los cambios:

```bash
git add .
```

Guardar los cambios:

```bash
git commit -m "Agrega ejercicios de la primera clase"
```

Enviar los cambios a GitHub:

```bash
git push
```

Descargar los cambios más recientes:

```bash
git pull
```

---

## 📋 Recomendaciones

* Crea un archivo diferente para cada ejercicio.
* Utiliza nombres claros para tus variables.
* Escribe comentarios cuando sea necesario.
* Guarda frecuentemente tus avances.
* Realiza commits con mensajes descriptivos.
* No compartas contraseñas ni datos sensibles.
* No subas el entorno virtual `.venv` a GitHub.

---

## 📝 Normas para nombrar archivos

Utiliza nombres en minúsculas y separados por guion bajo:

```text
01_hola_mundo.py
02_variables.py
03_entrada_salida.py
04_conversiones.py
05_operadores.py
06_fstrings.py
07_idea_proyecto.py
```

Evita nombres como:

```text
Ejercicio Final Nuevo 2.py
```
## 🌿 Archivo `.gitignore`

El archivo `.gitignore` permite indicar qué archivos no deben subirse a GitHub.

Ejemplo:

```gitignore
.venv/
__pycache__/
.env
*.pyc
```

## 🔐 Variables de entorno

Las contraseñas y datos sensibles deben guardarse en un archivo `.env`.

Ejemplo:

```env
DB_NAME=curso_python
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

El archivo `.env` no debe subirse a GitHub.

## 👨‍💻 Autor

**Andrés Jaramillo**

GitHub: `pucodev88`

---

## 📄 Licencia

Este repositorio se utilizará con fines educativos.


