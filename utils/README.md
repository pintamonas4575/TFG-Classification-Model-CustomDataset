Este archivo consta de 2 partes:

- Sección superior: Traslada todas las fotos que haya en los subsets de 'Testing' y 'Validation' a 'Training'.
- Sección inferior: Traslada, seleccionando de forma aleatoria, el **10%** de las fotos del dataset a **'Testing'** y el **20%** a **Validation'**.

Este método cuenta con flexibilidad, de modo que solo es necesario cambiar el nombre del dataset a manipular y la ruta de sus 3 particiones (Trainig, Validation y Testing).

Se espera que la estructura del dataset sea la siguiente:

```bash
📂Nombre dataset    
├── 📂Training
│   ├── 📂Clase1 
│   │   ├── 🖼️Foto1
│   │   ├── 🖼️Foto2
│   │   └── ...
│   ├── 📂Clase2   
│   │   ├── 🖼️Foto1
│   │   ├── 🖼️Foto2
│   │   └── ... 
│   └── ...
├── 📂Validation
│   ├── 📂Clase1 
│   │   ├── 🖼️Foto1
│   │   ├── 🖼️Foto2
│   │   └── ...         
│   ├── 📂Clase2         
│   └── ...
└── 📂Testing
    ├── 📂Clase1
    │   ├── 🖼️Foto1
    │   ├── 🖼️Foto2
    │   └── ...           
    ├── 📂Clase2         
    └── ...
```

⚠️ Se recuerda la necesidad de cambiar los paths del dataset en el notebook. ⚠️