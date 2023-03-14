
# OPENAI API (Prueba Ideaware)

  

Esta es una API basada en Django que utiliza los modelos GPT-3 de OpenAI para generar respuestas a preguntas. Puedes seleccionar uno de dos modelos: `text-davinci-003` y `gpt-3.5-turbo`.

  

## Endpoint

  

Para utilizar la API, envía una solicitud `POST` a la siguiente dirección: `http://127.0.0.1:8000/chat-free/`.

  

## Parámetros de solicitud

  

Los siguientes parámetros se pueden incluir en el cuerpo de tu solicitud codificado en JSON:

  

-  `prompt`: La pregunta para la que quieres generar una respuesta (requerido).

-  `model`: El nombre del modelo que deseas utilizar (`text-davinci-003` o `gpt-3.5-turbo`). Por defecto es `text-davinci-003`.

-  `temperature`: Controla la "creatividad" del texto generado. Valores más altos resultan en respuestas más variadas. Por defecto es `0.7`.

-  `max_tokens`: El número máximo de tokens en la respuesta generada. Por defecto es `1024`.

-  `top_p`: Controla la diversidad del texto generado. Valores más bajos resultan en respuestas más predecibles. Por defecto es `1.0`.

-  `frequency_penalty`: Controla la repetición del texto generado. Valores más altos resultan en menos repetición. Por defecto es `0.0`.

-  `presence_penalty`: Controla la presencia de ciertas palabras o frases en el texto generado. Valores más altos resultan en menos ocurrencias. Por defecto es `0.0`.

-  `systemPrompt`: (Solo para `gpt-3.5-turbo`) El prompt del sistema a utilizar al generar respuestas. Por defecto, utiliza un prompt que hace que el modelo genere respuestas en el estilo de un hablante de Barranquilla.

  

## Ejemplo de uso

  


Para generar una respuesta a la pregunta "¿Cuál es tu color favorito?" utilizando el modelo `gpt-3.5-turbo` con una temperatura de `1.0`, un máximo de `256` tokens y un penalty de frecuencia de `1.5`, y un prompt de sistema "Dime un chiste", envía una solicitud POST a `http://127.0.0.1:8000/chat-free/` con el siguiente cuerpo:

  

```json

{

"prompt": "¿Cuál es tu color favorito?",

"model": "gpt-3.5-turbo",

"temperature": 1.0,

"max_tokens": 256,

"top_p": 0.9,

"frequency_penalty": 1.5,

"systemPrompt": "Dime un chiste"

}
