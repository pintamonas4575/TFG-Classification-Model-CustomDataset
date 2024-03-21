# TFG-Classification-Model-CustomDataset

Creación en Tensorflow de un modelo de clasificación sobre un Dataset propio. 

Se ha creado tanto un modelo propio desde cero, como hecho _fine tuning_ al modelo de EfficientNetB2 proporcionado por Keras.

Se irá actualizando un ***readme.md*** en cada notebook para explicar el mismo.

----------------------

Para usar la GPU en Windows nativo se necesita:

- Python -> versión 3.10
- Tensorflow -> versión 2.9 (en la 2.10 hay un error irreparable que no deja guardar el modelo creado, no se puede hacer *'model.save'*)
- Drivers de CUDA -> versión 11.x
- cuDNN -> versión 8.x

**NOTA1:** Previamente se debe tener un dataset local que conste de imágenes repartidas en las clases que se deseen clasificar. 

**NOTA2:** Se debe tener en cuenta que se deberán de ajustar todos los paths para el correcto funcionamiento de los notebooks.

# Notebook *modelo_propio*

Notebook de creación, entrenamineto y pruebas de un modelo propio y el archivo ***.keras*** que obtiene un **60%** de **accuracy** en **test**.

# Carpeta *utils*
En esta carpeta se encuentra un archivo para **"reciclar"** el dataset con descripción detallada. 

# Contacto

Cualquier duda o sugerencia contactar con el autor:

Alejandro Mendoza: alejandro.embi@gmail.com

