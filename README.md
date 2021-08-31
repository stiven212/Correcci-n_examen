# Correccion_examen
# Ejercicio 1
## Dentro de couchdb se crea una base de datos llamada "olimpiccities" en la cual se guardaran los tweets recopilados en la ubicación insertada con las coordenadas.
![image](https://user-images.githubusercontent.com/58042139/131230857-4d1dd408-393f-4f02-9427-8fc4db4cb673.png)
![image](https://user-images.githubusercontent.com/58042139/131230909-16583a99-368f-4661-8376-592b925ed3d5.png)

# Ejercicio 2
## Dentro de couchdb se crea otra base de datos llamada "olimpicgame" en la cual se guardaran los tweets recopilados por el track de "Juegos Olimpicos"
![image](https://user-images.githubusercontent.com/58042139/131231134-c6c316a7-d1de-4128-b4a8-c6f5939db232.png)
![image](https://user-images.githubusercontent.com/58042139/131231201-19c1cdc3-9546-4186-bedd-ae86212e169c.png)

# Ejercicio 3
## Se hace la conexión con mongodb mediante el cliente de pymongo, luego se realiza el web-scraping buscando un patron comun de las etiquetas y esa recopilación es guardada en una colección llamada noticias de una base de datos en mongodb llamada JuegosO
![image](https://user-images.githubusercontent.com/58042139/131232137-b9719cb3-3374-49ad-961d-5b7d340e4494.png)

# Ejercicio 4
## Se crea una base de datos y una coleccion llamada "facebook" en MongoDB, por el momento estas están vacías
![image](https://user-images.githubusercontent.com/66144847/131356930-d82790f5-816f-46e4-b04b-0761f23438af.png)

## Se conecta a la base utilizando PyMongo y se extraen posts de Facebook de la página "Olympics" utilizando la librería facebook-scraper. El script se encarga de separar los elementos del post y guardarlos uno por uno como documentos, si la operación tiene éxito, aparece un mensaje de post guardado, de lo contrario, aparece un mensaje de error y se salta al siguiente post. Este script se ejecuta hasta que se lo interrumpa con el teclado.
![image](https://user-images.githubusercontent.com/66144847/131357543-f98d6f17-a37c-42a5-9ae5-d0cdec900bee.png)

## Se podrá observar que los documentos se encuentran guardados en la base creada
![image](https://user-images.githubusercontent.com/66144847/131357768-c203611d-0a40-4380-8ede-e8010294a8a3.png)

# Ejercicio 5
## Utilizando la libreria de npm llamada tiktok-scraper se realiza la recopilación de información de los videos que tengan el hashtag de Tokio2020.
![image](https://user-images.githubusercontent.com/58042139/131403562-4433ec08-0321-4524-858b-7309a5389cd2.png)
## Una vez realizada la recopilación se cargan los datos en una base de datos local de MySql
![image](https://user-images.githubusercontent.com/58042139/131403933-c44e5b59-1486-4185-99e8-9ecce2933566.png)
![image](https://user-images.githubusercontent.com/58042139/131404071-a0eb9d8d-08d1-4ff9-8df8-e1b05c9fee09.png)
![image](https://user-images.githubusercontent.com/58042139/131404112-e7983741-0e24-40bd-8ef4-ee4d42f58f6e.png)

# Ejercicio 6
## Dentro del administrador de base de datos PHPMyAdmin se realiza la exportación de la base de datos en formato JSON. Unicamente se los exporta a mongodb y se ve reflejada.
![image](https://user-images.githubusercontent.com/58042139/131406561-4f9cae86-ea2c-4ead-a8e1-166724dd0e69.png)
![image](https://user-images.githubusercontent.com/58042139/131406596-da7eda60-f941-4147-b0f2-7b1b8f3a853c.png)
![image](https://user-images.githubusercontent.com/58042139/131406891-14d4eb7f-228a-4afe-8fab-d03c0e930b0b.png)
## Se puede observar los 20 items que forman parte de un arreglo
![image](https://user-images.githubusercontent.com/58042139/131408015-f7093c9f-0c18-49a1-910f-aa42a895a16b.png)

# Ejercicio 7
## Se realiza la conexión entre couchdb y mongodb a travez de pymongo, y mediante un for se va iterando en la base de datos de couch mientras se inserta en la base de mongodb.
![image](https://user-images.githubusercontent.com/58042139/131410850-04edd7b6-18b3-498a-a219-2c1f2001c8d7.png)

# Ejercicio 8
## Para subir todos los resultados a MongoDB Atlas primero se procede a crear una base de datos en un cluster. Atlas permite solo un cluster gratuito a la vez, por lo tanto se creará una nueva base en un cluster previamente creado
![image](https://user-images.githubusercontent.com/66144847/131426182-76cf2bba-c33a-4691-805e-44a3fe650eb5.png)

## Se exporta la colección de datos de facebook en formato JSON
![image](https://user-images.githubusercontent.com/66144847/131426707-3ab3637b-bf3d-46da-a050-2ce8afb2a23d.png)

## Se pueden insertar los datos en atlas de forma manual haciendo click en "insert document" y pegando el contenido del json generado anteriormente
![image](https://user-images.githubusercontent.com/66144847/131427398-d12e7358-1c38-44c0-9118-919ceabd087f.png)
![image](https://user-images.githubusercontent.com/66144847/131427484-070b1022-7707-4b1a-b184-e023b3d4ad17.png)
![image](https://user-images.githubusercontent.com/66144847/131428436-f0e90a77-cb24-432c-bac3-d1e770018ce3.png)

## Un cluster al estar ubicado en la nube, se pueden invitar colaboradores para que puedan añadir datos
![image](https://user-images.githubusercontent.com/66144847/131429864-03db669b-d847-4470-8626-d5642965511f.png)

## Los colaboradores aparecerán en la lista de acceso y se podrá eliminarlos o modificar sus permisos si se requiere
![image](https://user-images.githubusercontent.com/66144847/131430588-14dd73a9-d3f0-45f2-a240-3ca849cb25e2.png)

## Se procede a crear mas colecciones para el resto de datos
![image](https://user-images.githubusercontent.com/66144847/131431124-36496ee6-f45f-4b2e-b731-a403905f664c.png)

## Alternativamente se puede crear un script para subir directamente a Atlas, esto se hizo con los datos de Twitter, el script utiliza la cadena de conexión generada en Atlas para conectarse e insertar los datos en el cluster, este script se puede observar en el archivo 8.py
![image](https://user-images.githubusercontent.com/66144847/131435370-dfa86e00-d7e3-44ec-9677-00c6973ffa48.png)

## Luego de importar todos los datos a Atlas las bases de datos del cluster se verán así
![image](https://user-images.githubusercontent.com/66144847/131435473-85319313-78f1-4593-8427-dfb4673a9574.png)

# Ejercicio 9
## 
