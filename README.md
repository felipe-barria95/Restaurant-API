# Tarea 2 Taller de Integración - API REST
Los datos utilizados en la base de datos fueron extraidos de la página de Uncle Fletch. A continuación, se detallarán los metodos que se pueden utilizar, en conjunto con las restricciones correspondientes para cada caso.
- **GET** /hamburguesa , Obtiene las 11 hamburguesas con la informacion de cada una.
- **POST** /hamburguesa , se crea la hamburguesa con la información entregada. No es necesario agregarle un atributo ID, ya que la base de datos la va a instansiar de forma automática. Si se instancia de forma correcta retornara HTTP201. De lo contrario retornara HTTP400. Debe incluir nombre, precio, descripcion e imagen. Ingredientes no debe ser referenciado.
- **GET** /hamburguesa/id , obtiene la hamburguesa con el ID especificado. Si se ingresa un ID invalido retornara HTTP400. Si no se encuentra una hamburguesa con el ID indicado retornara HTTP404. Si se ingresa un ID valido retornara HTTP200 con el json correspondiente.
- **DELETE** /hamburguesa/id , elimina la hamburguesa con el ID especificado con toda la informacion en su interior. Esto incluye las instanciaciones con los ingredientes. Si se ingresa un ID invalido retornara HTTP400. Si no se encuentra una hamburguesa con el ID indicado retornara HTTP404.
- **PATCH** /hamburguesa/id , actualiza la una de las siguientes propiedades:
  - nombre
  - precio
  - descripcion
  - imagen

Nota: Se puede actualizar mas de una propiedad a la vez. Si se intenta actualizar los ingredientes o el ID con PATCH, retornara HTTP400 response. Si no se encuentra el ID de la hamburguesa retornara HTTP404. Si se ingresa un ID no valido retornara HTTP400.
- **DELETE** /hamburguesa/id_ham/ingrediente/id_ing , elimina el ingrediente entregado de la hamburguesa. Se deberan entregar ID's validos y que la hamburguesa como el ingrediente efectivamente esten instanciados, sino retornara HTTP404 response.
- **PUT** /hamburguesa/id_ham/ingrediente/id_ing , agrega el ingrediente entregado a la hamburguesa. Debe cumplir con lo anterior. Además, no se podra agregar un ingrediente a una hamburguesa que ya tenga ese mismo ingrediente. Si se hacer retornara HTTP400.
- **GET** /ingrediente , obtiene todos los ingredientes que existen.
- **POST** /ingrediente , crea un nuevo ingrediente. De la misma forma que la hamburguesa, no sera necesario explicitar un ID para el ingrediente creado.
- **GET** /ingrediente/id , obtiene el ingrediente con el ID entregado.
- **DELETE** /ingrediente/id , borra un ingrediente con el ID entregado, solo si no esta en ninguna hamburguesa.
