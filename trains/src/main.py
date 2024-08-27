# Trains
from ursina import EditorCamera, Ursina, Vec3, Sky, DirectionalLight, PointLight, Text, mouse
from ursina.color import color

from model import Model
# from trainsmap import TrainsMap
from trainsfield import TrainsField

# Initialize Ursina engine
app = Ursina(borderless=False)

# Main directional light
main_light = DirectionalLight(y=3, z=3, shadows=True)
main_light.intensity = 10

# Fill light (softer light from another direction)
fill_light = DirectionalLight(y=-1, x=2, shadows=False)
fill_light.intensity = 8

# sky url: https://github.com/devy52/Sky-Wars/blob/main/sky.png
skybox = Sky(texture='sky_default')

model = Model()
trainsfield = TrainsField()
trainsfield.set_model(model)

text_bottom = Text(
    text='Hold down right mouse and move to rotate the camera',
    scale=2,
    position=(0, 0, 0),
    origin=(0, 0),
    billboard=True
)

editor_camera = EditorCamera()
editor_camera.position = (0, 4, -10)
editor_camera.rotation = (15, 1.5, 0)
# Make the EditorCamera look at the origin
editor_camera.look_at(Vec3(0, 0, 0))
# Variable to store the previous rotation of the camera
previous_rotation = editor_camera.rotation

def update():
    global previous_rotation

    # Check if the rotation of the camera has changed
    if editor_camera.rotation != previous_rotation:
        # Print the new rotation angles
        # print(f"New Camera Rotation: {editor_camera.rotation}")

        # Update the previous rotation to the current one
        previous_rotation = editor_camera.rotation

    if mouse.right:
        text_bottom.visible = False

model.start()   # Start the model
app.run()   # Run the Ursina app
