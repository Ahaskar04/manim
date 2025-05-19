from manim import tempconfig
from main import SIZoo2  # adjust import if your file name is different

# Define your custom parameters
params = {
    "units": [
        ("Length", "m", "#a2d2ff"),
        ("Mass", "kg", "#ffc9de"),
        ("Time", "s", "#caffbf"),
        ("Energy", "J", "#ffaaaa")
    ],
    "highlight_script": ["Energy"],
    "highlight_style": "red_flash",
    "show_previous_units": True
}

# Use Manim’s tempconfig to set quality & preview
with tempconfig({"quality": "low_quality", "preview": True}):  # change to "medium_quality" or "high_quality" if needed
    scene = SIZoo2()

    # Inject parameters into the scene
    for key, value in params.items():
        setattr(scene, key, value)

    # Render the scene
    scene.render()
