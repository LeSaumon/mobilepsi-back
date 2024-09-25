
# Mobilepsi

**Mobilepsi** est un outil pour les étudiants leurs permettant de faciliter leurs trajet entre le domicile et l'école, mais également de réduire son impact écologique en leurs proposant une application pour organiser leurs trajets.

L'application permet : 
- De se connecter en utilisant les identifiants de l'école **EPSI**
- De créer une annonce de covoiturage
- De créer une annonce de location de véhicules (voiture, vélo, trotinettes ...)
- De s'inscrire à un covoiturage où une annonce de location de véhicule
- De consulter les réservations disponibles
- De modifier ses reservations créées ou celles ou l'on est inscrit
- 




## Launch the backend

To launch the backend, you need:
- [Python](https://www.python.org/) 3.10.12
- [PostgreSQL](https://www.postgresql.org/)

1. Create the virtual environment
```bash
python3 -m venv venv
```

2. Activate the virtual environment

Windows
```bash
./venv/scripts/activate
```
Linux
```bash
source ./venv/bin/activate
```

3. Install the dependencies
```
pip install -r requirements.txt
```

4. Setting up the postgres database

*You can follow any tutorial that teach you how to set up a postgresql database*

1. Modify the `src/config.py` file to adapt your database url

```python
postgres_url = "postgresql://<username>:<password>@<host>/<database_name>"
```

6. You can now start the backend 
```bash
fastapi dev src/main.py
```
## API Reference

### Pony API

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | `id` of pony to fetch |
| `body`      | `json` | The `json` representation of a Pony object |

| Endpoint | Description |
| :--------| :-----------|
| **GET** `/bikes/`| Return all bikes data from database |
| **GET** `/bike/{id}`| Return the specific bike linked to the `id` parameter |
| **PATCH**`/bike/{id}`| Update the specific bike related tothe `id` parameter. The bike data must be sent through the `body` of the request.|
| **DELETE** `/bike/{id}`| Delete and return the deleted bike related to the `id` parameter |

### Random API

| Endpoint | Description |
| :--------| :-----------|
| **GET** `/random/parking/available`| Return a random boolean |
| **GET** `/random/bikes`| Return bikes object which are randomly generated by the backend |
| **GET**`/random/parkings`| Return parkings object which are randomly generated by the backend|
| **GET** `/random/sensors`| Return sensors object which are randomly generated by the backend |