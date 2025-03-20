Este documento nos ayudara a entender como se llevo a cabo el desafio. 

Lo primero que se realizo fue un analisis de la solicitud. en la cual se detallaba la necesidad de clonar un repositorio y hacerlo funcionar de forma local
![image](https://github.com/user-attachments/assets/66bf25d0-dd27-4f61-b0ed-a065a408dbc2)

armar un contenedor con una App (sencilla) que ejecutara un hola mundo
Para realizar esta tarea se uso flask, docker y python. Lo primero fue armar una pequeña app en python que al ejecutarla nos muestra un cartel hola mundo y lo expone 
en el puerto 5000 pero luego se modifico y se le asigno el puerto 8080 ya que es el puerto por defecto de las url que usa gcloud run. Con docker build se construyo la
imagen que luego seria almacenada en Docker Hub. 
