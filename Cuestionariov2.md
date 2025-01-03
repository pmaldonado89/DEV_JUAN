# Cuestionario Técnico

Este cuestionario está diseñado para evaluar conocimientos y habilidades técnicas en desarrollo de software. Está organizado por categorías y niveles de dificultad.

---

## **Sección 1: Conocimientos Generales**

1. **¿Cuál es la diferencia entre Git y GitHub, y cómo se complementan en el desarrollo de software?**
   _Dificultad: Básico_
   **RESPUESTA:**
Tenemos que git es el sistema de control de versiones y github un servicios saas para uso de git

   ***

3. **¿Qué es TypeScript y cuáles son las ventajas de su uso?**  
   _Dificultad: Básico_
   **RESPUESTA:**  
Es un lenguaje de programación que sirve como una capa extra superior para JS y teniendo ventajas como el manejo de tipado estricto, estructuras de datos y complemento que da otros lenguajes de programacion 

   ***

4. **Explica qué es CORS (Cross-Origin Resource Sharing) y cómo se maneja en una aplicación web.**  
   _Dificultad: Intermedio_
   **RESPUESTA:**  
  
   ***
Es una politica de seguridad que tiene el navegador donde bloquea las peticiones de un dominio externo al origen
   
---

## **Sección 2: Desarrollo Frontend**

4. **¿Qué es el Virtual DOM y cómo mejora el rendimiento de React?**  
   _Dificultad: Intermedio_
   **RESPUESTA:**  
   ***
Es una abstración del DOM real, y react lo tiene en memoria manejado por estado donde el acceso es mucho más facil y ligero 

6. **Escribe un componente en React que renderice una lista de elementos a partir de un array de datos.**  
   _Dificultad: Intermedio_
   **RESPUESTA:**
   ***


8. **¿Cómo manejarías el estado global en una aplicación React?**  
   _Dificultad: Avanzado_
   **RESPUESTA:**  
   ***
``` js
import React from 'react';

const Item = ({ name, descripcion}) => {
   return (
      <div>
         <h3>{name}</h3>
         <p>{descripcion}</h3>
      </div>
   );
}

const ItemList = ({}) => {
   return (
      <div>
         {
            items.map(item => ({
               <Item key={item.id} name={item.name} descripcion={item.descripcion} />
            )});
         }
      </div>
   );

}

export default ItemList;
```
---

## **Sección 3: Desarrollo Backend**

7. **Explica el concepto de middleware en Express.js y proporciona ejemplos de su uso.**  
   _Dificultad: Intermedio_
   **RESPUESTA:**  
   ***

Es una capa extra que se puede ejecutar antes de llegar al endpoint y luego de ejecución

``` js

const middlware = (req, res, next) => {
   console.log("Middleware ejecutado");
   next();
}
```

9. **¿Qué es NestJS y qué lo hace diferente de otros frameworks de backend?**  
   _Dificultad: Básico_
   **RESPUESTA:**  
   ***

Es un framework backend pero progresivo que utiliza typescript como lenguaje principal y su enfoque es modular

11. **Explica el concepto de inyección de dependencias en NestJS.**  
   _Dificultad: Avanzado_
   **RESPUESTA:**  
   ***
Es una estrategia donde hay contenedor de dependencia que a partir de la inyección esta ayuda a resolver todo lo necesario a la hora de crear ejecutar una clase etc.


11. **Diseña una API REST para gestionar tareas (CRUD) utilizando NestJS. Registra las tareas en un archivo de texto.**  
    _Dificultad: Avanzado_
    **RESPUESTA:**
    ***
---

Campos:
title:str
description:str
status:bool

BD: Seria una no relacional

Cloud: Seria uso AWS y desplegado en un EC2

Diseñamos entonces los endpoint repectivos para cada CRUD:
C -> POST /item + payload 
R -> GET /item o item/{id}
U -> PUT /item/{id} + payload 
D -> DELETE /item/{id}

Le agregamos una placa de seguridad de autorizacion e untenticacion con una tecnologia de JWT.

Cuando se ejecute los endpoint validamos los campos requeridos y logica de negocio. Ya luego se hace la creacion de archivo y se alamacena en el sistema de storage que se maneje.

## **Sección 4: Infraestructura y DevOps**

11. **¿Cómo configurarías un pipeline CI/CD para una aplicación usando React y NestJS?**  
    _Dificultad: Avanzado_
    **RESPUESTA:**  
    ***
Supongamos el contexto que se tiene ya toda la aplicacion desarrollada y alojada en github:
Creamos el pipeline en un github action:
- El action se ejecutara cuando se lanze un PR a la rama main
- Colocamos los steps:
- - step de configuracion
- - step de instalar dependencias
- - step ejecutar test
- - step de build apliacion
- - step deploy a la cloud

13. **¿Qué es Docker y cómo lo usarías para empaquetar una aplicación Node.js?**  
    _Dificultad: Intermedio_
    **RESPUESTA:**  
    ***

Es una tecnologia donde manejamos contenedores para empaquetar aplicaciones con la tecnologia y setups necesarios. Entonces creamos una imagen (Dockerfile) para la configuraciones necesarias y luego generar el contenedor.


15. **Diseña una solución tecnológica (a nivel de arquitectura) para captura de datos en campo, garantizando sincronización online/offline.**  
    _Dificultad: Avanzado_
    **RESPUESTA:**  
---

Hacemos una arquitectura basada en dos frentes (Front y Backend)

Front:
Tecnologias: Flutter 
Caracteristicas: Modo offline: almacenamiento local usando AsyncStorage.  Y usar sincronizacion automatica que detecte conectividad y sincronice datos locales con el servidor.

Backend:
Tecnologia: Python
Caracteristicas: Usamos una API Rest con el framework de starlette.
BD: Usariamos una BD no relacional (Mongo DB)
Middleware: Apache Kafka y su funcion seria la reconciliacion de datos (merge entre offline y online)
Infrastructure: Cloud AWS para sincronizacion rapida DynamoDB y S3 para almaceniamiento. AWS lambda para procesos ligeros y API Gatwway para manejar solicitudes
Patron CRDT para colocar colas locales tareas para envio de informacion

## **Sección 5: Bases de Datos**

14. **¿Qué es una migración en bases de datos y por qué es importante?**  
    _Dificultad: Básico_
    **RESPUESTA:**  
    ***
Es la accion de crear un cambio de estado en una BD (Tablas) y es importante para tener un historico. y sea una forma mas rapida de ejecucion y alza de aplicación

16. **Explica la diferencia entre bases de datos relacionales y no relacionales.**  
    _Dificultad: Básico_
    **RESPUESTA:**
    
    Relacional: Almacena datos en tablas  de filas y columnas y se utiliza lenguaje SQL para interactuar con los datos. Datos organizadosen relaciones o tablas (cada tabla tiene un esquema fijo) y su relaciones se hacen a apartir de claves primarias y foraneas 
No relacional: No usan tablas como almacenamiento principal y los modelos de datos pueden ser clave-valor, documentos, columnas o grafos. No requiere esquemas fijos   
    ***
   

18. **Escribe un ejemplo de cómo realizarías una consulta básica a una base de datos con un ORM en NestJS.**  
    _Dificultad: Intermedio_
    **RESPUESTA:**  
    Usando como ORM Eloquen de Laravel:

    - Para consultar por clave primaria:
    - - modelo.find(id)
    - Para consulta por where y campo:
    - - modelo.where(campo, comparacion, valor)->get()
    - Para consultar y traer unas columnas y por where:
    - - modelo.where(campo, valor)->select([columna])->get()
    Etc asi seria una estructura valor mas semantico.
    ***
---

## **Sección 6: Algoritmos y Resolución de Problemas**

17. **Escribe un algoritmo en Python que busque duplicados en un array.**  
    _Dificultad: Intermedio_
    **RESPUESTA:**  
    ***

Recibimos una lista de elementos y lo que hacemos a partir de un contador ir buscando si esta o no en este diccionario que vamos almacenando por el valor
``` python

from collections import Counter

def find_duplicates_with_count(nums):

   counts = Counter(nums)

   duplicates = {key: value for key, value in counts.items() if value > 1}
   return duplicates

```

19. **Tienes un archivo JSON llamado `data.json` que contiene información sobre ventas de una empresa. Diseña un algoritmo en Python que:**  
    _Dificultad: Intermedio_

    - Calcule la suma total de ventas por categoría.
    - Devuelva el resultado en un formato legible como un diccionario Python.
    - Opción adicional: Guarde el resultado en un nuevo archivo JSON llamado `category_sales.json`.

    **RESPUESTA:**  
    
   Leemos el archivo JSON: -> se carga contenido usando json load
   Calcular la suma por categorias: -> se itera sobre la lista de datos y agrupando por categorias
   Guardar resultados: -> se guarda el diccionario en un archivo y de forma legible

   ``` python

   import json
   from itertools import groupby

   with open('data.json', 'r') as file:
      data = json.load(file)

   data.sort(key=lambda x: x['category'])
   category_sale = {
      category: sum(map(lambda x: x['sales'], item))
      for category, items in groupby(data, lambda x: x['category'])
   }

   with open('category_sales.json', 'w') as file:
      json.dump(category_sales, file, indent=4)

   ```
    ***

20. **Diseña una arquitectura básica para una aplicación de e-commerce usando React, NestJS y PostgreSQL.**
    **RESPUESTA:**  
    ***
   
React (Front) -> NestJs (Backend) -> PostgresSQL (Base de datos)
Frontend: 
funcionalidades: Catalogo de productos, Carrito de compras, Autenticacion, Gestion de Pedidos
Backend:
modulos principaleS: Auth, Productos, Carrito, Ordenes y Pagos

Comunicacion: Seria a traves de API Rest con un Auth de JWT

Cloud: AWS con EC2

Contenerizacion: Usariamos Docker 

Escalabilidad: API Gateway, Balanceadores de carga, Cache (Redis) y una aruitectura de microservicios



   
