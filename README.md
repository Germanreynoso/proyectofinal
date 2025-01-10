# Juego de Preguntas y Respuestas

## Descripción

Este es un juego de preguntas y respuestas desarrollado en Python utilizando la biblioteca `tkinter` para la interfaz gráfica y `pygame` para los efectos de sonido. El juego presenta preguntas de diferentes niveles de dificultad y permite al usuario responderlas, utilizando ayudas como 50/50 y saltar preguntas.

## Características

- **Interfaz gráfica**: Utiliza `tkinter` para una interfaz amigable y fácil de usar.
- **Efectos de sonido**: Utiliza `pygame` para reproducir sonidos al responder correctamente o incorrectamente.
- **Preguntas de diferentes dificultades**: Las preguntas están clasificadas en fácil, medio y difícil.
- **Ayudas**: El usuario puede usar ayudas como 50/50 y saltar preguntas.
- **Guardado de progreso**: El progreso del juego se guarda automáticamente en un archivo `progress.json`.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `pygame`, `PIL`

## Instalación

1. Clona este repositorio en tu máquina local.
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```
2. Navega al directorio del proyecto.
    ```bash
    cd tu-repositorio
    ```
3. Instala las dependencias necesarias.
    ```bash
    pip install pygame pillow
    ```

## Uso

1. Asegúrate de que los archivos [questions.json](http://_vscodecontentref_/2) y [progress.json](http://_vscodecontentref_/3) estén en el directorio del proyecto.
2. Ejecuta el archivo [main.py](http://_vscodecontentref_/4) para iniciar el juego.
    ```bash
    python main.py
    ```

## Estructura del Proyecto

- [main.py](http://_vscodecontentref_/5): Archivo principal que inicia la aplicación.
- [gui.py](http://_vscodecontentref_/6): Contiene la clase [QuizApp](http://_vscodecontentref_/7) que maneja la interfaz gráfica del juego.
- [quiz.py](http://_vscodecontentref_/8): Contiene la clase [Quiz](http://_vscodecontentref_/9) que maneja la lógica del juego.
- [questions.json](http://_vscodecontentref_/10): Archivo JSON que contiene las preguntas del juego.
- [progress.json](http://_vscodecontentref_/11): Archivo JSON que guarda el progreso del juego.
- `assets/`: Directorio que contiene las imágenes y sonidos utilizados en el juego.

## Formato de [questions.json](http://_vscodecontentref_/12)

El archivo [questions.json](http://_vscodecontentref_/13) debe tener el siguiente formato:

```json
[
    {
        "pregunta": "¿Quién es conocido como el 'Rey del Rock'?",
        "opciones": ["Elvis Presley", "Chuck Berry", "Jimi Hendrix", "Little Richard"],
        "respuesta": "Elvis Presley",
        "dificultad": "fácil"
    },
    {
        "pregunta": "¿En qué año se publicó '1984' de George Orwell?",
        "opciones": ["1945", "1951", "1960", "1949"],
        "respuesta": "1949",
        "dificultad": "fácil"
    },
    {
        "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
        "opciones": ["George Washington", "Thomas Jefferson", "John Adams", "James Madison"],
        "respuesta": "George Washington",
        "dificultad": "medio"
    }
]
```

 # Contribuciones
## Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los siguientes pasos:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza los cambios necesarios y haz commit (git commit -am 'Añadir nueva característica').
Sube los cambios a tu repositorio (git push origin feature/nueva-caracteristica).
Crea un Pull Request.
## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de tu-email@example.com.

