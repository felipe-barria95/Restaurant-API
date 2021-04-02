# T02 - API REST
The data used in the database was taken from the [Uncle Fletch](https://delivery.uncle-fletch.com) website. Next, the methods that can be used will be detailed, together with the corresponding restrictions for each case. Link to website: [Restaurant API](https://barria-t02.herokuapp.com)
- **GET** /hamburger - Get the 11 hamburgers with the information of each one.
- **POST** /hamburger - The hamburger is created with the information provided. It is not necessary to add an ID attribute to it, since the database will instantiate it automatically. If it is instantiated correctly, it will return HTTP201. Otherwise it will return HTTP400 error. It must include name, price, description and image. Ingredients should not be referenced.
- **GET** /hamburger/{id} - Gets the hamburger with the specified ID. If an invalid ID is entered, HTTP400 error will be returned. If a hamburger with the indicated ID is not found, it will raise HTTP404 error. If a valid ID is entered, it will return HTTP200 with the corresponding JSON.
- **DELETE** /hamburger/{id} - Delete the hamburger with the specified ID with all the information inside. This includes instantiations with ingredients. If an invalid ID is entered, HTTP400 error will be returned. If a hamburger with the indicated ID is not found, it will return HTTP404 error.
- **PATCH** /hamburger/{id} , updates one of the following properties:
  - name
  - price
  - description
  - image

Side note: You can update more than one property at the same time. If you try to update the ingredients or the ID with PATCH, it will return HTTP400 error. If the hamburger ID is not found, it will raise HTTP404 error. If an invalid ID is entered, HTTP400 error will be returned.
- **DELETE** /hamburger/{id_ham}/ingredient/{id_ing} - Removes the delivered ingredient from the burger. Valid ID's must be provided and that the hamburger as the ingredient is effectively instantiated, otherwise it will return HTTP404 error response.
- **PUT** /hamburger/{id_ham}/ingredient/{id_ing} - add the delivered ingredient to the burger. You must comply with the above. Also, you cannot add an ingredient to a hamburger that already has that same ingredient, or it will return HTTP400 error.
- **GET** /ingredient - Get all the ingredients that exist.
- **POST** /ingredient - Create a new ingredient. In the same way as the hamburger, it will not be necessary to specify an ID for the ingredient created.
- **GET** /ingredient/{id} - Get the ingredient with the given ID.
- **DELETE** /ingredient/{id} - Delete an ingredient with the given ID, only if it is not in any hamburger. If the ingredient is present in a hamburger it will raise HTTP409 error.
