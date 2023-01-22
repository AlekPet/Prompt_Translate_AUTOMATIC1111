# Title: Prompt translate script for AUTOMATIC1111/stable-diffusion-webui
# Description: Promt translator into other languages
# GitHub: https://github.com/AlekPet/prompt_translate
# Date: 2023-01-22
import re
import modules.scripts as scripts
import gradio as gr

from modules.processing import Processed
from modules.shared import opts, cmd_opts, state
from googletrans import Translator, LANGUAGES

translator = Translator()
empty_str = re.compile('^\s*$', re.I | re.M)

class Script(scripts.Script):
    
    def title(self):
        return "Prompt tranlsate (from start app)"

    def getprompt(self, value):
        return value
        
    def translate(self, gtext, srcTrans=None, toTrans=None):
        if not gtext or empty_str.match(gtext):
            return ['',srcTrans]

        if not srcTrans:
            srcTrans = 'auto'
            
        if not toTrans:
            toTrans = 'en'
            
        tranlate_text = translator.translate(gtext, src=srcTrans, dest=toTrans)
        
        return [tranlate_text.text, tranlate_text.src]

    def change_lang(self, src, dest):
            if src != 'auto' and src != dest:
                return [src, dest]
            return ['en','auto']


    def process(self, p, *args):
        print('process')
        
    def run(self, p, *args):
        if p.prompt:
            p.prompt = self.translate(p.prompt)[0]

        if p.negative_prompt:
            p.negative_prompt = self.translate(p.negative_prompt)[0]
    
    def after_component(self, component, **kwargs):
        try:
            
            if isinstance(component, (gr.components.Textbox,)):

                if kwargs.get('elem_id') == 'txt2img_prompt':
                    self.txt2img_prompt = component
                    
                if kwargs.get('elem_id') == 'txt2img_neg_prompt':
                    self.txt2img_neg_prompt = component

                if kwargs.get('elem_id') == 'img2img_prompt':
                    self.img2img_prompt = component

                if kwargs.get('elem_id') == 'img2img_neg_prompt':                    
                    self.img2img_neg_prompt = component

                    
                if kwargs.get('elem_id') == 'txt2img_neg_prompt' or kwargs.get('elem_id') == 'img2img_neg_prompt':

                    tab = 0
                    if kwargs.get('elem_id') == 'img2img_neg_prompt':
                        tab = 1
                    
                    with gr.Blocks():
                        with gr.Row():
                            with gr.Column():
                                with gr.Row():
                                    gtrans = gr.Button(value="Translate")
                                    gtrans_neg = gr.Button(value="Negative Translate")

                            with gr.Column():
                                with gr.Row():
                                    srcTrans = gr.Dropdown(['auto']+list(LANGUAGES.keys()), value='auto', label='From', interactive=True)
                                    toTrans = gr.Dropdown(list(LANGUAGES.keys()), value='en', label='To', interactive=True)
                                change_src_to = gr.Button(value="🔃")

                                if tab == 0:
                                    gtrans.click(self.translate, inputs=[self.txt2img_prompt, srcTrans, toTrans], outputs=[self.txt2img_prompt, srcTrans])
                                    gtrans_neg.click(self.translate, inputs=[self.txt2img_neg_prompt, srcTrans, toTrans], outputs=[self.txt2img_neg_prompt, srcTrans])
                                else:
                                    gtrans.click(self.translate, inputs=[self.img2img_prompt, srcTrans, toTrans], outputs=[self.img2img_prompt, srcTrans])
                                    gtrans_neg.click(self.translate, inputs=[self.img2img_neg_prompt, srcTrans, toTrans], outputs=[self.img2img_neg_prompt, srcTrans])
                                
                                change_src_to.click(self.change_lang, inputs=[srcTrans,toTrans], outputs=[toTrans,srcTrans])

        except Exception as e:
            print(e)
