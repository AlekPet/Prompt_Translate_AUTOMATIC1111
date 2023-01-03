# Title: Prompt translate script for AUTOMATIC1111/stable-diffusion-webui
# Description: Promt translator into other languages
# GitHub: https://github.com/AlekPet/prompt_translate

import modules.scripts as scripts
import gradio as gr

from modules.processing import Processed
from modules.shared import opts, cmd_opts, state
from googletrans import Translator, LANGUAGES

translator = Translator()

class Script(scripts.Script):
    
    def title(self):
        return "Prompt tranlsate"

    def getprompt(self, value):
        return value
        
    def translate(self, gtext, srcTrans,toTrans):
        if not gtext:
            return ''

        if not srcTrans:
            srcTrans = 'auto'
            
        if not toTrans:
            toTrans = 'en'
            
        tranlate_text = translator.translate(gtext, src=srcTrans, dest=toTrans)

        return [tranlate_text.text, tranlate_text.src]

    def change_lang(self, src, dest):
            if src != 'auto':
                return [src, dest]
          
    def after_component(self, component, **kwargs):
        try:

            if isinstance(component, (gr.components.Textbox,)):
                if kwargs.get('elem_id') == 'txt2img_prompt' or kwargs.get('elem_id') == 'img2img_prompt':
                    with gr.Blocks():
                        with gr.Row():
                            with gr.Column():
                                gtext = gr.Textbox(label="Text translate", lines=2, value="", placeholder="Google translate text", show_label=False, interactive=True)
                                gGet =  gr.Button(value="Get prompt")
                                gtrans = gr.Button(value="Translate")

                            with gr.Row():
                                with gr.Column():
                                    srcTrans = gr.Dropdown(['auto']+list(LANGUAGES.keys()), value='auto', label='From', interactive=True)
                                    toTrans = gr.Dropdown(list(LANGUAGES.keys()), value='en', label='To', interactive=True)
                                with gr.Column():
                                    change_src_to = gr.Button(value="🔃")

                        gGet.click(self.getprompt, inputs=[component], outputs=[gtext])
                        gtrans.click(self.translate, inputs=[gtext,srcTrans,toTrans], outputs=[component, srcTrans])
                        change_src_to.click(self.change_lang, inputs=[srcTrans,toTrans], outputs=[toTrans,srcTrans])

        except Exception as e:
            print(e)
