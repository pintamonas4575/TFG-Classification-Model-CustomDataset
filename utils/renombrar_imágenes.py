
import os

directory = "../cats20_probarV2/TRAINING"
razas = os.listdir(directory)

for raza in razas:
    i=0
    nombres_fotos = os.listdir(f'{directory}/{raza}')
    for foto in nombres_fotos:
        nombre, extension = os.path.splitext(f'{directory}/{raza}/{foto}')
        os.rename(src=f'{directory}/{raza}/{foto}', dst=f'{directory}/{raza}/{raza}_{i}{extension}')
        i+=1