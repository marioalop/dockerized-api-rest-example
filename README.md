# dockerized-api-rest-example  
## Efemerides Rest API
Proyecto API Rest demo  realizado con django rest framework y dockerizado

Se utilizo como fuente de datos para las efemerides:  http://www.igualdadycalidadcba.gov.ar/SIPEC-CBA/AnuariosEscolares/2019/Efemerides-Anuario2019.pdf

## Despliegue

instalar docker y docker compose, en Ubuntu:

    wget -qO- https://get.docker.com/ | sh
    sudo usermod -aG docker $(whoami)
    sudo apt-get -y install python-pip
    sudo pip install docker-compose

Editar variables de entorno del archivo .env


Ejectuar  docker-compose:

    sudo docker-compose up -d

La API Rest se encuentra expuesta en el puerto 80

## Uso
### Autenticación
Obtener token JWT via POST en /token/
Payload de autenticacion:

    {"username": "<username>", "password": "<password>"}

Ejemplo

    curl -X POST "http://127.0.0.1/token/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"username\":\"<USERNAME>\",\"password\":\"<PASSWORD>\"}"

Resultado:

    {"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1...", "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0hw.."}

En los headers de las consultas externas a la API colocar el "access" 

    Authorization: JWT <JWT ACCESS>

## Consulta de efemérides
Realizar un GET a /efemerides?day=YYYY-MM-DD
Ejemplo

 `GET http://127.0.0.1/efemerides?day=2019-05-01`
Resultado:

    {
	    "dia": [
		    "Día de los Trabajadores",
		    "Día de la Constitución Nacional"
	    ],
	    "mes": {
	    "01": "Día de los Trabajadores // Día de la Constitución Nacional",
	    "02": "Día Nacional del Crucero ARA ",
	    "03": "Día Mundial de la Libertad de Prensa",
	    "07": "Día de la Promoción de la Palabra y la No Violencia en el espacio público // Día de la Minería Argentina",
	    "08": "Día Internacional de la Cruz Roja",
	    "11": "Día del Himno Nacional Argentino",
	    "15": "Día Provincial de la Familia",
	    "17": "Día Provincial por la Igualdad y la No Discriminación por Orientación Sexual",
	    "18": "Día de la Escarapela Nacional",
	    "23": "Día del Cine Nacional",
	    "25": "Aniversario de la Revolución de Mayo",
	    "28": "Día de los Jardines de Infantes y Día de la Maestra Jardinera",
	    "29": "Día del Cordobazo y de las Luchas Populares",
	    "30": "Día Nacional de la Donación de "
	    }
    }
*Si no se especifica una fecha devuelve el dia actual

## Documentación
En /docs/ se encuentra la documentacion de los esquemas con swagger

## CRUD
En /admin/ se encuentra habilitado el admin de django para la gestion de las efemerides y usuarios.
