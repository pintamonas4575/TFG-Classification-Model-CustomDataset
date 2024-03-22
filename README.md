# TFG-Classification-Model-CustomDataset

Creación en Tensorflow de un modelo de clasificación sobre un Dataset propio. 

Se ha creado tanto un modelo propio desde cero, como hecho _fine-tuning_ al modelo EfficientNetB2 proporcionado por Keras.

🙋‍♂️ Los archivos de este repositorio pertenecen al TFG de Alejandro Mendoza Medina.

----------------------

Para usar la GPU en Windows nativo se necesita:

- Python -> versión 3.10
- Tensorflow -> versión 2.9 (en la 2.10 hay un error irreparable que no deja guardar el modelo creado, no se puede hacer *'model.save'*)
- Drivers de CUDA -> versión 11.x
- cuDNN -> versión 8.x

**NOTA1:** Previamente se debe tener un dataset local que conste de imágenes repartidas en las clases que se deseen clasificar. Para saber sobre la estructura del dataset, consultar el _readme.md_ de la carpeta _'utils'_.

**NOTA2:** Se debe tener en cuenta que se deberán de ajustar todos los paths para el correcto funcionamiento de los notebooks.

# 📓 Notebook *modelo_propio*

Notebook de creación, entrenamiento y pruebas de un modelo propio que obtiene un **60%** de **accuracy** en **test**.

Las imágenes que se quieran predecir manualmente deben ser redimensionadas a 224x224.

# 📓 Notebook *modelo_EficientNet*

Notebook de creación, entrenamiento y pruebas de un modelo al que se le ha hecho _fine-tuning_ del modelo *EfficientNetB2* que obtiene un **88%** de **accuracy** en **test**.

Las imágenes que se quieran predecir manualmente deben ser redimensionadas a 224x224.

# 📂 Carpeta *"utils"*
En esta carpeta se encuentra un archivo para **"reciclar"** el dataset con descripción detallada.

# 📂 Carpeta *"modelos"*

En esta carpeta se encuentran los modelos creados, tanto el propio como el "fine-tuneado" con EfficientNetB2.

☣️☣️

Si se quisiera reentrenar/probar alguno de los modelos, sepa el lector que se han entrenado sobre un dataset de imágenes de 31 clases de razas de gatos 😸, las cuales son las siguientes: 

Abyssinian, American Curl, American Shorthair, Bengal, Birman, Bobtail, Bombay, British Shorthair, Burmilla, Calico, Egyptian Mau, Exotic Shorthair, Ginger, Khao Manee, Maine Coon, Manx, Munchkin, Nebelung, Norwegian Forest, Persian, Ragdoll, Rex, Russian Blue, Scottish Fold, Siamese, Snowshoe, Sphynx, Tabby, Tortoishell, Turkish Angora y Tuxedo.

Con otro tipo de clases (flores, coches...) no predecirá correctamente.

☣️☣️

# 📂 Carpeta *"fotos"*

Se propircionan imágenes para probar predicciones manualmente.

# ⚖️ Licencia 
Ya podría ser la burocracia de España igual de rápida que obtener la licencia de Github. 

# 👤 Contacto

Cualquier duda o sugerencia contactar con el autor:

Alejandro Mendoza: alejandro.embi@gmail.com
