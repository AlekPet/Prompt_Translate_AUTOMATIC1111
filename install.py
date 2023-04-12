import launch
import os

requirements = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

with open(requirements) as file:
    for l in file:
        l = l.strip()
        if launch.is_installed("googletrans==3.1.0a0"):
            launch.run_pip("ininstall googletrans==3.1.0a0", f"Prompt_translate uninstall -> googletrans==3.1.0a0")
        
        if not launch.is_installed(l):
            launch.run_pip(f"install {l}", f"Prompt_translate requirement -> {l}")
