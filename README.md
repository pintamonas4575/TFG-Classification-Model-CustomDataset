# TFG-Classification-Model-CustomDataset

Creación en Tensorflow de un modelo de clasificación sobre un Dataset propio. 

Se ha creado tanto un modelo propio desde cero, como hecho _fine tuning_ al modelo de EfficientNetB2 proporcionado por Keras.

Se irá actualizando un ***readme.md*** en cada notebook para explicar el mismo

----------------------

Para usar la GPU en Windows nativo se necesita:

- Python -> versión 3.10
- Tensorflow -> versión 2.9 (en la 2.10 hay un error irreparable que no deja guardar el modelo creado, no se puede hacer *'model.save'*)
- Drivers de CUDA -> versión 11.x
- cuDNN -> versión 8.x

**NOTA:** Previamente se debe tener un dataset local que conste de imágenes repartidas en las clases que se deseen clasificar. 

Cualquier duda o sugerencia contactar con el autor:

Alejandro Mendoza: alejandro.embi@gmail.com

Markdown
<span style="color:red">Este texto está en rojo</span>

<!--HTML-->
<p style="color:red">Este texto está en rojo</p>

```bash
function test() {
  console.log("notice the blank line before this function?");
}
```

ddd