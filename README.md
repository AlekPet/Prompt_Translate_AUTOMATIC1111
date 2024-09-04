# Prompt translate -> AUTOMATIC1111 and stable-diffusion-webui-Forge (version 2024.09.04)

'Prompt translate' script for AUTOMATIC1111/stable-diffusion-webui (and https://github.com/lllyasviel/stable-diffusion-webui-forge) translate prompt.
This script allows you to write a query in promt query in your native language,
and then translate it into English for better results and not resort to translators.

![Prompt translate AUTOMATIC1111](https://raw.githubusercontent.com/AlekPet/Prompt_Translate_AUTOMATIC1111/main/image_prompt_translate.jpg)

### Description:

The extension for translating promts into English (possibly into other languages) supports the following services (not all is free):

- DeeplTranslator
- QcriTranslator
- LingueeTranslator
- PonsTranslator
- PapagoTranslator
- BaiduTranslator
- MyMemoryTranslator
- GoogleTranslator
- YandexTranslator
- ChatGptTranslator
- LingueeTranslator
- MicrosoftTranslator

### Use

```
1. Cick 'Enable tranlsate'
2. Select languages from and to (or auto, detect source langauges automatical)
3. Click 'Generate' or 'Translate' (if you want views tranlsated prompts in all prompts) and after 'Generate'
```

### Instalation

1. Go to the extension in the webui tab
2. Click on the "Instrall from URL tab"
3. Past link to github https://github.com/AlekPet/Prompt_Translate_AUTOMATIC1111.git (or https://github.com/AlekPet/prompt_translate.git) from field "URL for extension's git repository"
4. And restart webio in settings tab

### Manual instalation

1. Download the repository from github in a zip archive and unpack the Prompt_Translate_AUTOMATIC1111 folder (or immediately unpack the archive into extensions), where you have automatic1111 installed and move it to the extensions folder.
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

### Attention

AUTOMATIC1111 stores some settings in its **ui-config.json** file, which may affect **proxy** field values ​​and **authorization data**

### Note settings:

By default, in the **config.json** file, the option to show services without api is disabled (option **"show_services_no_check_api = false"**), which have **free_api = false** and do not specify **api_key** and other authorization values ​​(depending on the translation service). If you set the value of **show_services_no_check_api: true**, then all services with the value **show_service: true** will be shown. You can also set values ​​to enable proxies and show hidden fields by default.

### Old version

**The old version of the script that runs with the start of Stable Diffusion is here:**
https://github.com/AlekPet/prompt_translate/tree/Prompt-translate-(from_start_app)
