from ursina import *

app = Ursina()

EditorCamera()

modelo = Entity(
    model='scene.gltf',
    scale=0.01
)

print(modelo)

app.run()