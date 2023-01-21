# Prompt translate
'Prompt translate' script for AUTOMATIC1111/stable-diffusion-webui translate prompt.
This script allows you to write a query in promt query in your native language,
and then translate it into English for better results and not resort to translators.

# NOTE
```
The text is translated in automatic mode, only the script "Prompt translate"
at the bottom is selected (without it, the "run" method does not run),
and so far we have not been able to find a way to update the fields with the translated values from the "run" method :)
```

# Instalation
1. Go to the extension in the webui tab
2. Click on the "Instrall from URL tab"
3. Past link to github https://github.com/AlekPet/prompt_translate.git from field "URL for extension's git repository"
4. And restart webio in settings tab

# Manual instalation
1. Download the file "prompt_translate.py" from the script githib folder and transfer it to the scripts folder where stable-diffusion is installed.
2. Add `googletrans==3.1.0a0` to requirements_versions.txt


# Manual instalation - version 2
1. Download the file "prompt_translate.py" from the script githib folder and transfer it to the scripts folder where stable-diffusion is installed.
2. Run virtual enviroment in stable-diffusion folder, run window console or other bash
3. Enter this code
    
Windows
```
.\venv\scripts\activate  
pip install "googletrans==3.1.0a0"
```
    
Linux
```
source ./venv/bin/activate  
pip install "googletrans==3.1.0a0"
```
