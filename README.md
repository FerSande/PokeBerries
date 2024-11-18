
# Proyecto FastAPI - Poke-berries Statistics API

Este proyecto es una aplicación web construida con **FastAPI**, diseñada para proporcionar estadísticas sobre las bayas de Pokémon. Utiliza **Docker Compose** para la configuración y despliegue del entorno.

## Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Instalar Docker y Docker Compose](#instalar-docker-y-docker-compose)
3. [Construir y Ejecutar la Aplicación con Docker Compose](#construir-y-ejecutar-la-aplicación-con-docker-compose)
4. [Uso](#uso)
5. [Esquema de la API](#esquema-de-la-api)

## Requisitos Previos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Tener acceso a una terminal o símbolo del sistema en tu sistema operativo.
- Tener **Docker** y **Docker Compose** instalados en tu máquina.

## Instalar Docker y Docker Compose

1. **Descargar Docker:**
   - Visita la página oficial de [Docker](https://www.docker.com/get-started) y sigue las instrucciones para descargar e instalar **Docker Desktop** según tu sistema operativo.

2. **Verificar la Instalación de Docker:**
   - Abre una terminal y ejecuta el siguiente comando para verificar que Docker esté instalado correctamente:

     ```bash
     docker --version
     ```

3. **Instalar Docker Compose:**
   - Docker Compose suele venir incluido con Docker Desktop, pero si necesitas instalarlo por separado, consulta la documentación oficial de [Docker Compose](https://docs.docker.com/compose/install/).

   - Verifica que Docker Compose esté instalado correctamente con:

     ```bash
     docker-compose --version
     ```

## Construir y Ejecutar la Aplicación con Docker Compose

1. **Clonar el Proyecto (si no lo tienes aún):**

   Si aún no tienes el repositorio en tu máquina, clónalo usando el siguiente comando:

   ```bash
   git clone git@github.com:FerSande/PokeBerries.git
   ```

2. **Construir y Ejecutar la Aplicación:**
   - En el directorio raíz del proyecto, ejecuta el siguiente comando para construir y ejecutar los contenedores:

     ```bash
     docker-compose up --build
     ```

   - Este comando construirá las imágenes necesarias para la aplicación y las levantará:
     - **FastAPI** en el puerto `8000`

3. **Acceder a la Aplicación:**
   - Una vez que los contenedores estén en ejecución, puedes acceder a los siguientes endpoints:
     - API de FastAPI: `http://localhost:8000/`

4. **Detener los Contenedores:**
   - Para detener los contenedores, puedes ejecutar el siguiente comando:

     ```bash
     docker-compose down
     ```

## Uso

- **FastAPI**:
  - La API de FastAPI proporciona un conjunto de endpoints que permiten acceder a las estadísticas sobre las bayas de Pokémon. Puedes consultar estos endpoints directamente desde `http://localhost:8000/docs` y obtener la información en formato JSON.

- **test**:
  - Para ejecutar los tests hay que ejecutar el sig comando: pytest ./tests/test_endpoints.py

- **Render**
 - La API se encuentra subida en render, se puede probar usando https://pokeberries-1.onrender.com, o sus respectivos endpoints https://pokeberries-1.onrender.com/allBerryStats y https://pokeberries-1.onrender.com/berryHistogram

- **Streamlit**
 - Tambien se utilizo streamlit para que quede una aplicacion web mas amigable al usuario y se subio al cloud para poder usarlo remoto, la url es: https://pokeberries-mwyeygnnpqwl2tljfsgrsz.streamlit.app/

## Esquema de la API

La aplicación tiene los siguientes endpoints que puedes usar para obtener estadísticas sobre las bayas de Pokémon:

- **GET `/`**:  
  - **Descripción**: Endpoint de prueba que retorna un mensaje de bienvenida.
  - **Respuesta**:

    ```json
    {
        "message": "Welcome to the Poke-berries Statistics API"
    }
    ```

- **GET `/allBerryStats`**:
  - **Descripción**: Obtiene las estadísticas de todas las bayas de Pokémon, incluyendo tiempos de crecimiento, tipos y otras métricas.
  - **Respuesta**:

    ```json
    {
      "min_growth_time": 30,
      "max_growth_time": 120,
      "mean_growth_time": 75,
      "berry_types": ["Cheri", "Chesto", "Pecha"]
    }
    ```

- **GET `/berryHistogram`**:
  - **Descripción**: Obtiene el histograma de las bayas

