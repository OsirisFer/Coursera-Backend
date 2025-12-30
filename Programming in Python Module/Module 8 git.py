# Continuos Integration es una práctica de desarrollo de software donde los desarrolladores integran 
# su código en un repositorio compartido con frecuencia,  preferiblemente varias veces al día. 
# Cada integración es verificada por una construcción automatizada (incluyendo pruebas) para detectar errores lo antes posible.
# Un ejemplo de esto es GitHub Actions, que permite automatizar flujos de trabajo como pruebas y despliegues.
# Continuous Delivery resumido es dejar el código listo para producción en cualquier momento
# Continuous Deployment va un paso más allá y automatiza el despliegue del código a producción después de pasar todas las pruebas.
"""
Comandos Unix:
cd ..  # Moverse al directorio padre
mkdir <nombre_directorio>  # Crear un nuevo directorio
ls  # Listar archivos y directorios en el directorio actual
pwd  # Mostrar la ruta del directorio actual
man <comando>  # Mostrar el manual de un comando
touch <nombre_archivo>  # Crear un nuevo archivo vacío
clear # Limpiar la pantalla de la terminal
mv <origen> <destino>  # Mover o renombrar un archivo o directorio
cat <nombre_archivo>  # Mostrar el contenido de un archivo
wc -l <nombre_archivo>  # Contar las líneas de un archivo
less <nombre_archivo>  # Ver el contenido de un archivo página por página
grep <patrón> <nombre_archivo>  # Buscar un patrón en un archivo
pipes (|)  # Usar la salida de un comando como entrada para otro comando
flags (-)  # Modificadores que cambian el comportamiento de los comandos

GIT COMMANDS:
git init  # Inicializar un nuevo repositorio Git
git clone <url_repositorio>  # Clonar un repositorio remoto
git status  # Ver el estado de los archivos en el repositorio
git add <nombre_archivo>  # Agregar archivos al área de preparación (staging area)
git commit -m "mensaje"  # Confirmar los cambios con un mensaje descriptivo
git push  # Subir los cambios al repositorio remoto
git pull  # Descargar y fusionar cambios del repositorio remoto
git fetch  # Descargar cambios del repositorio remoto sin fusionarlos
git branch  # Listar, crear o eliminar ramas
git checkout -B <nombre_rama> # Cambiar a una rama o crear una nueva rama y cambiar a ella  
git merge <nombre_rama>  # Fusionar una rama en la rama actual
git log  # Ver el historial de commits
git remote -v  # Remote lo que hace es listar los repositorios remotos vinculados al repositorio local

El orden generalmente es: 
git init -> git status -> git add -> git commit -> git pull -> git push




"""
