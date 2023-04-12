# Prompt translate
'Prompt translate' script for AUTOMATIC1111/stable-diffusion-webui translate prompt.
This script allows you to write a query in promt query in your native language,
and then translate it into English for better results and not resort to translators.

**The old version of the script that runs with the start of Stable Diffusion is here:**
https://github.com/AlekPet/prompt_translate/tree/Prompt-translate-(from_start_app)

# !! Warning !!:
**This old scripts used librarie  ~~googletrans==3.1.0a0~~, crash output generated images in stable-diffusion-webui (not showed result image after generation in window output)**

I am used other library named is __"deep_translator"__

To debug you need to delete the **env** folder in the root of stable-diffusion-webui and then re-run **webui-user.bat** or **webui-user.sh** (Linux) otherwise you will not see the generated images at the output. After go to install instructions. :)


# Use
```
1. Cick Enable tranlsate
2. Select languages from and to (or auto, detect source langauges automatical)
3. Click 'Generate' or 'Translate' (if you want views tranlsated prompts in all prompts) and after 'Generate'
```

# Instalation
1. Go to the extension in the webui tab
2. Click on the "Instrall from URL tab"
3. Past link to github https://github.com/AlekPet/prompt_translate.git from field "URL for extension's git repository"
4. And restart webio in settings tab


# Manual instalation
1. Download the file "prompt_translate.py" from the script githib folder and transfer it to the scripts folder where stable-diffusion is installed.
2. Run virtual enviroment in stable-diffusion folder, run window console or other bash
3. Enter this code
    
Windows
```
.\venv\scripts\activate  
pip install "deep_translator"
```
    
Linux
```
source ./venv/bin/activate  
pip install "deep_translator"
```
