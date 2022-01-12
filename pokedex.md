# Projet Pokédex
Ce tp consiste à créer un site qui permet à l'utilisateur d'ajouter dans son pokédex, pour cela vous aurez besoin d'effectuer un système de connexion et d'utiliser une database (sqlite comme la dernière fois) pour stocker les diverses informations


```sql 
CREATE TABLE pokedex(
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    poke_id INTEGER NOT NULL
    );

CREATE TABLE pokemon(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ptype VARCHAR(255) NOT NULL,
    img VARCHAR(255) NOT NULL
    );

CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    );



```


Dans ce tp vous aurez 3 pages minimum à réaliser : 


- La page Register, elle sert à créer le compte d'un utilisateur, grace à cette page vous devez récupérer le nom d'utilisateur et le mot de passe renseigné dans le formulaire, puis les insérer dans la base de données. Puis elle redirige l'utilisateur vers la page Login

- La page Login, qui sert à connecter l'utilisateur, il faut donc comme sur le page register récupérer les données du formulaire puis récuperer les informations de l'utilisateur dans la base de données grâce au nom d'utilisateur fourni dans le formulaire, ensuite si le mot de passe du formulaire correspond au mot de passe présent dans la base de données on instancie la session de l'utilisateur et elle redirige l'utilisateur vers la page Home

- La page home qui récupère la liste des pokémons depuis la base de données et permet d'ajouter ou de retirer un pokémon de son pokédex. Tous les pokémons sont contenus dans un seul formulaire, seul la valeur que renvoit le bouton change
   ```html
  <button type="submit" value="" name="">Add</button>
   ```
  On récupère ensuite en méthode POST la valeur du bouton pour définir si on doit retirer ou ajouter le pokémon ´ ainsi que l'id du pokemon, puis on ajoute l'id de l'user contenu dans la session ainsi que l'id du pokémon dans la base de données 

  ![](https://i.imgur.com/QGVaMEh.png)
