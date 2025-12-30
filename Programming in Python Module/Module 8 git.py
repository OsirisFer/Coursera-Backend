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
git status  # Ver donde estoy y el estado de los archivos en el repositorio
git branch --show-current  # Mostrar la rama actual a la que apunto
git rev-parse HEAD  # Mostrar a que commit estoy apuntando
git add <nombre_archivo>  # Agregar archivos al área de preparación (staging area)
git commit -m "mensaje"  # Confirmar los cambios con un mensaje descriptivo
git push  --u origin <nombre_rama>  # Subir los cambios al repositorio remoto o sino para hacerlo a  main directo es git push -u origin main
git pull  # Descargar y fusionar cambios del repositorio remoto
git fetch  # Descargar cambios del repositorio remoto sin fusionarlos
git branch  # Listar, crear o eliminar ramas
git checkout <nombre_rama>  # Sin el -b solo te mueves a la rama existente
git checkout -B <nombre_rama> # Con el -b creas y te mueves a la rama nueva, con -B fuerzas la creación de la rama nueva
git merge <nombre_rama>  # Fusionar una rama en la rama actual
git log  --pretty=oneline  # Ver el historial de commits en una sola línea por commit
git remote -v  # Remote lo que hace es listar los repositorios remotos vinculados al repositorio local
git log --merge # Ver el historial de commits con detalles de fusiones
git diff  # Mostrar las diferencias entre archivos o commits
git diff main..feature_branch  # Mostrar las diferencias entre dos ramas
git blame <nombre_archivo>  # Mostrar quién modificó cada línea de un archivo



El orden generalmente es: 
git init -> git status -> git add -> git commit -> git pull -> git push



"""
