'''
CREAR ENTORNOS VIRTUALES

n entorno virtual es una carpeta que contiene una instalación aislada de Python y sus paquetes.

Esto permite que cada proyecto tenga sus propias dependencias.

Crear una carpeta para el proyecto
mkdir analisis_datos
cd analisis_datos
Crear el entorno virtual
python -m venv .venv

La carpeta .venv almacenará el intérprete y los paquetes del proyecto.

Activar el entorno en PowerShell
.\.venv\Scripts\Activate.ps1

Cuando esté activo, la terminal mostrará algo parecido a:

(.venv) PS C:\proyectos\analisis_datos>
Posible error de permisos en PowerShell

Si PowerShell impide ejecutar el script de activación, se puede usar temporalmente:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Después:

.\.venv\Scripts\Activate.ps1
Activación desde CMD
.venv\Scripts\activate
Activación en Linux o macOS
source .venv/bin/activate
Desactivar el entorno
deactivate

Eliminar el entorno virtual:
Remove-Item -Recurse -Force .venv   
'''


