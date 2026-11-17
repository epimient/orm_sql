# Sistema de Inventario de Zapatos — SQLAlchemy ORM

## 1. Información del proyecto

| Información | Descripción |
|---|---|
| Estudiante | [Nombre completo] |
| Asignatura | [Nombre de la asignatura] |
| Docente | [Nombre del docente] |
| Fecha | [Fecha de entrega] |
| Lenguaje de programación | Python |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

## 2. Descripción del proyecto

**¿En qué consiste el programa?**

[Escribe un párrafo explicando qué hace la aplicación, qué información administra y cuál es su propósito.]

**¿Qué funcionalidades tiene?**

Describe brevemente las operaciones que permite realizar el sistema:

- Registrar zapatos.
- Consultar el inventario.
- Buscar zapatos por ID.
- Actualizar precios.
- Eliminar zapatos.

## 3. Estructura del proyecto

Presenta la estructura de archivos de tu aplicación.

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
└── evidencias/
```

**Explicación de los archivos:**

| Archivo | ¿Cuál es su responsabilidad? |
|---|---|
| `main.py` | [Explicar] |
| `datos.py` | [Explicar] |
| `requirements.txt` | [Explicar] |
| `zapateria.db` | [Explicar cómo y cuándo se genera] |

## 4. Instalación y ejecución

Explica los pasos para ejecutar el proyecto en otro computador.

**Paso 1. Requisitos**

[Indica los programas y herramientas necesarios.]

**Paso 2. Instalación de dependencias**

```bash
python -m pip install -r requirements.txt
```

**Paso 3. Ejecución**

```bash
python main.py
```

**Paso 4. Resultado esperado**

[Describe qué aparece cuando se ejecuta correctamente la aplicación.]

---

# 5. Documentación técnica — Preguntas obligatorias

Responde las siguientes preguntas utilizando tu implementación. Cuando sea necesario, incluye fragmentos de tu código para explicar el funcionamiento.

### Pregunta 1. Modelo y tabla

¿Qué clase de Python representa la tabla de la base de datos? Explica cómo SQLAlchemy identifica el nombre de la tabla y sus columnas.

**Respuesta:**

[Escribe tu respuesta aquí.]

**Fragmento de código relacionado:**

[Agrega el fragmento de código de tu modelo y explícalo.]

### Pregunta 2. Creación de la base de datos

¿Qué ocurre cuando ejecutas el programa por primera vez? Explica cómo se crea la base de datos `zapateria.db` y la tabla `zapatos`.

**Respuesta:**

[Escribe tu respuesta aquí.]

**Fragmento de código relacionado:**

[Indica qué instrucciones intervienen en la creación de la base de datos y la tabla.]

### Pregunta 3. Registro de zapatos

Cuando seleccionas la opción de registrar un zapato, ¿qué recorrido siguen los datos desde el menú hasta quedar almacenados en SQLite? Identifica las funciones utilizadas.

**Respuesta:**

[Explica paso a paso lo que sucede desde que el usuario escribe los datos hasta que se almacenan.]

**Fragmento de código relacionado:**

[Agrega el código correspondiente y explícalo.]

### Pregunta 4. Sesiones y transacciones

¿Para qué se utiliza una sesión de SQLAlchemy? ¿Qué ocurriría si agregas o modificas un objeto, pero no confirmas la transacción con `commit()`?

**Respuesta:**

[Escribe tu respuesta aquí y relaciona el concepto con el código del programa.]

### Pregunta 5. Búsqueda por ID

¿Cómo funciona la búsqueda de zapatos por ID? Explica qué devuelve tu función cuando encuentra el registro y qué devuelve cuando no existe.

**Respuesta:**

[Escribe tu respuesta aquí.]

**Fragmento de código relacionado:**

[Agrega el código de búsqueda y explícalo.]

### Pregunta 6. Actualización de precios

¿Cómo se actualiza el precio de un zapato mediante el ORM? Explica cómo se obtiene el objeto, cómo se modifica su atributo y cómo se guarda el cambio.

**Respuesta:**

[Escribe tu respuesta aquí.]

**Fragmento de código relacionado:**

[Agrega el código de actualización y explícalo.]

### Pregunta 7. Eliminación de registros

¿Qué ocurre cuando eliminas un zapato? Explica cómo compruebas que el registro ya no existe en la base de datos.

**Respuesta:**

[Escribe tu respuesta aquí.]

**Fragmento de código relacionado:**

[Agrega el código de eliminación y explica su funcionamiento.]

### Pregunta 8. Persistencia de datos

¿Qué sucede con los zapatos registrados cuando cierras y vuelves a ejecutar el programa? Explica por qué permanecen almacenados.

**Respuesta:**

[Escribe tu respuesta aquí e indica cómo comprobaste que los registros se conservaron.]

---

## 6. Pruebas de funcionamiento y evidencias

Debes ejecutar el programa y demostrar el funcionamiento de cada una de las operaciones.

### Prueba 1. Registrar zapatos

- **Acción realizada:** registrar dos zapatos.
- **Datos utilizados:** [Indicar modelo, talla y precio].
- **Resultado obtenido:** [Explicar qué ocurrió].

**Evidencia:**

![Registro de zapatos](evidencias/registro.png)

### Prueba 2. Listar inventario

- **Acción realizada:** consultar todos los zapatos.
- **Resultado obtenido:** [Explicar qué mostró el programa].

**Evidencia:**

![Listado de zapatos](evidencias/listado.png)

### Prueba 3. Buscar por ID

- **ID utilizado:** [Indicar ID].
- **Resultado obtenido:** [Explicar qué ocurrió].

**Evidencia:**

![Búsqueda de zapatos](evidencias/busqueda.png)

### Prueba 4. Actualizar precio

- **Zapato seleccionado:** [Indicar].
- **Precio anterior:** [Indicar].
- **Precio nuevo:** [Indicar].
- **Resultado obtenido:** [Explicar qué ocurrió].

**Evidencia:**

![Actualización de precio](evidencias/actualizacion.png)

### Prueba 5. Eliminar zapato

- **ID eliminado:** [Indicar ID].
- **Resultado obtenido:** [Explicar cómo verificaste la eliminación].

**Evidencia:**

![Eliminación de zapato](evidencias/eliminacion.png)

### Prueba 6. Comprobar persistencia

- **Acción realizada:** cerrar y ejecutar nuevamente el programa.
- **Resultado obtenido:** [Explicar cuáles registros permanecieron guardados].

**Evidencia:**

![Persistencia de datos](evidencias/persistencia.png)

### Pruebas con registros inexistentes

Ejecuta las operaciones de buscar, actualizar y eliminar utilizando un ID que no exista.

| Operación | ¿Qué sucedió? |
|---|---|
| Buscar ID inexistente | [Respuesta] |
| Actualizar ID inexistente | [Respuesta] |
| Eliminar ID inexistente | [Respuesta] |

## 7. Conclusiones

Responde brevemente:

1. ¿Qué aprendiste al implementar las operaciones CRUD utilizando SQLAlchemy?
2. ¿Qué diferencia identificaste entre trabajar con objetos Python y escribir sentencias SQL directamente?
3. ¿Cuál fue la principal dificultad durante el desarrollo y cómo la solucionaste?


## Indicaciones de documentación

- Responde las ocho preguntas con tus propias palabras.
- Relaciona tus explicaciones con el código que implementaste.
- Incluye fragmentos de código únicamente cuando ayuden a explicar tu respuesta.
- Todas las evidencias deben corresponder a ejecuciones reales del programa.
- Guarda las capturas dentro de la carpeta `evidencias/` utilizando los nombres indicados o actualiza las rutas del README.
- Verifica que las imágenes se visualicen correctamente en GitHub.
- Elimina los textos entre corchetes y reemplázalos con tus respuestas antes de entregar.
- La documentación debe permitir que otra persona comprenda cómo instalar, ejecutar y utilizar tu aplicación.