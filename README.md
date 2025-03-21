El siguiente documento nos ayudara a entender como se llevo a cabo el desafio. 

Lo primero que se realizo fue un analisis de la solicitud. en la cual se detallaba la necesidad de clonar un repositorio y hacerlo funcionar de forma local y exponerlo en el puerto 80 tal como se muestra en la siguiente imagen.
![image](https://github.com/user-attachments/assets/02bc52a7-56dc-4dcf-b1dd-0454e1a93b70)
![image](https://github.com/user-attachments/assets/bf2723ad-183d-4744-9182-75b4cc6e7b89)

La segunda etapada de este desafio consitia en armar un contenedor con una App (sencilla) que ejecutara un "hola mundo y mi nombre"
Para realizar esta tarea se uso docker, flask y python. Lo primero fue armar una pequeña app en python que al ejecutarla nos muestra un cartel "Hola mundo, soy Bryan Delgado" y lo expone 
en el puerto 5000(puerto que usa flask por defecto) pero luego se modifico y se le asigno el puerto 8080 ya que es el puerto por defecto de las url que usa gcloud run. Con docker build se construyo la imagen que primero seria probada de forma local como se muestra en la siguiente imagen y luego seria almacenada en mi repositorio de Docker Hub, mediante un push con nombre_usuario/appn_name:tag 
![image](https://github.com/user-attachments/assets/02bc52a7-56dc-4dcf-b1dd-0454e1a93b70)
![image](https://github.com/user-attachments/assets/9e576e8d-4736-43c9-b697-0b5c47a27e11)

La tercera etapa del desafio esta estrechamente relacionada con la cuarta y quinta etapa. Se pedia armar un Pipelne usando Github Actions para automatizar el procosedo de Dockerizar la App, subirla a DockerHub y luego desplegarla en mi proveedor cloud y todo esto deba ocurrir de forma automatica cada vez que yo hago un push a la rama principal "main". 
Para poder realizar esta parte del desafio tuve que investigar un poco ya que no tengo mucha experiencia en las nubes sugeridas lo cual me llevo algo de tiempo. Lo primero que hice fue armar un repositorio en Github, conectarlo con DockerHub y guardar las credenciales en los secret de github asi no queda ninguna dato sensible hardcodeado en el repositorio. Luege creer un archivo llamado ci-cd.yml 
