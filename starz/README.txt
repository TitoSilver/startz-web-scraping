Archivos:
    conected.py:
        archivo encargado de gestionar la cración listas de películas y series y entregar un diccionario final para el archivo json.

        baseURL(): retorna un string base para la cración de links para cada pelicula y series.

        requestURL(): retorna un string base para hacer las peticiones GET.

        listMovies():retorna un Array con un diccionario de cada objeto película de la plataforma starz.

        listSeries(): retorna un Array con un dccionario de cada objeto serie de la plataforma starz.

        createListMoviesAndSeries(): un wrapped que retorna un diccionario separando series y peliculas llamando a las funciones previamente
        definidas.
    
    main.py:
        archivo base se que encarga de buscar un archivo .json en el directorio de trabajo actual, en caso de encontrarlo lo borra
        para evitar posibles conflictos y crea un archivo "data.json" con toda la información previamente definida.

    data.json:
        archivo .json que incluye toda la información de la plataforma separandolo en sus dos llaves "movies" y "series"