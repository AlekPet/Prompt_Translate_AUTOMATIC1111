# Title: Prompt translate script for AUTOMATIC1111/stable-diffusion-webui
# Description: Prompt translator into other languages
# GitHub: https://github.com/AlekPet/prompt_translate
# Date: 2023-04-12
import re
import modules.scripts as scripts
import gradio as gr

from modules.processing import Processed, process_images
from modules.shared import opts, cmd_opts, state
from deep_translator import GoogleTranslator

empty_str = re.compile('^\s*$', re.I | re.M)

class Script(scripts.Script):

    def title(self):
        return "Prompt Tranlsate"
    
    def show(self, is_img2img):
        return scripts.AlwaysVisible
    
    def translate(self, prompt, prompt_neg='', srcTrans="auto", toTrans="en"):
        if not srcTrans:
            srcTrans = 'auto'
            
        if not toTrans:
            toTrans = 'en'

        tranlate_text_prompt = ''
        if prompt and not empty_str.match(prompt):
            tranlate_text_prompt = GoogleTranslator(source=srcTrans, target=toTrans).translate(prompt) 

        tranlate_text_prompt_neg = ''
        if prompt_neg and not empty_str.match(prompt_neg):
            tranlate_text_prompt_neg = GoogleTranslator(source=srcTrans, target=toTrans).translate(prompt_neg) 

        
        return [tranlate_text_prompt, tranlate_text_prompt_neg]
       

    def change_lang(self, src, dest):
            if src != 'auto' and src != dest:
                return [src, dest]
            return ['en','auto']
        
    def ui(self, is_img2img):          
        with gr.Accordion('Prompt Translate', open=False):
            with gr.Row():
                enabled = gr.Checkbox(label='Enable translate', value=False)
                automate = gr.Checkbox(label='Auto translate "Prompt and Negative prompt" before Generate', value=True)
                
            with gr.Row():
                gtrans = gr.Button(value="Translate")        

                srcTrans = gr.Dropdown(['auto','ru','en'], value='auto', label='From', interactive=True)
                toTrans = gr.Dropdown(['en','ru'], value='en', label='To', interactive=True)
                change_src_to = gr.Button(value="🔃")
                
            with gr.Row():
                adv_trans = gr.Checkbox(label='See translated prompts after click Generate', value=False)          
                
            with gr.Box(visible=False) as viewstrans:
                gr.Markdown('Tranlsated prompt & negative prompt')
                with gr.Row():
                    p_tr = gr.Textbox(label='Prompt translate', show_label=False, value='', lines=2, placeholder='Translated text prompt')

                with gr.Row():            
                    p_n_tr = gr.Textbox(label='Negative Translate', show_label=False, value='', lines=2, placeholder='Translated negative text prompt')

        def show_viewtrans(checkbox):
            return {viewstrans: gr.update(visible=checkbox)}                
                
        if not is_img2img :
            gtrans.click(self.translate, inputs=[self.txt2img_prompt, self.txt2img_neg_prompt, srcTrans, toTrans], outputs=[self.txt2img_prompt, self.txt2img_neg_prompt])
            gtrans.click(self.translate, inputs=[self.txt2img_prompt, self.txt2img_neg_prompt, srcTrans, toTrans], outputs=[p_tr, p_n_tr])
            self.p_com.click(self.translate, inputs=[self.txt2img_prompt,self.txt2img_neg_prompt, srcTrans, toTrans], outputs=[p_tr,p_n_tr])

        else:
            gtrans.click(self.translate, inputs=[self.img2img_prompt, self.img2img_neg_prompt, srcTrans, toTrans], outputs=[self.img2img_prompt, self.img2img_neg_prompt])
            gtrans.click(self.translate, inputs=[self.img2img_prompt,self.img2img_neg_prompt, srcTrans, toTrans], outputs=[p_tr, p_n_tr])
            self.ip_com.click(self.translate, inputs=[self.img2img_prompt,self.img2img_neg_prompt, srcTrans, toTrans], outputs=[p_tr, p_n_tr])

            
        change_src_to.click(self.change_lang, inputs=[srcTrans,toTrans], outputs=[toTrans,srcTrans])
        adv_trans.change(show_viewtrans, inputs=adv_trans, outputs=[viewstrans])        

        return [automate, enabled]

    def listTransale(self, tlist):
        result = []
        for ap in tlist:
            translate_prompt, translate_neg_prompt = self.translate(ap, '')
            result.append(translate_prompt)      
        return result
        
    def process(self, p, automate, enabled):
        if not enabled:
            return

        if automate:

            if p.prompt:
                prompt, negative_prompt = self.translate(p.prompt,p.negative_prompt)
                setattr(p, 'prompt', prompt)               
                setattr(p, 'negative_prompt', negative_prompt)

                all_prompts = self.listTransale(getattr(p,'all_prompts',[prompt]))
                all_negative_prompts = self.listTransale(getattr(p,'all_negative_prompts',[negative_prompt]))

                if not all_prompts:
                    all_prompts = [prompt]

                if not all_negative_prompts:
                    all_negative_prompts = [negative_prompt]
                    
                setattr(p, 'all_prompts', all_prompts)
                setattr(p, 'all_negative_prompts', all_negative_prompts)

    
    def after_component(self, component, **kwargs):           
        if isinstance(component, (gr.components.Textbox,)):

            if kwargs.get('elem_id') == 'txt2img_prompt':
                self.txt2img_prompt = component
                
            if kwargs.get('elem_id') == 'txt2img_neg_prompt':
                self.txt2img_neg_prompt = component

            if kwargs.get('elem_id') == 'img2img_prompt':
                self.img2img_prompt = component

            if kwargs.get('elem_id') == 'img2img_neg_prompt':                    
                self.img2img_neg_prompt = component

        if isinstance(component, (gr.components.Button,)):
            if kwargs.get('elem_id') == 'txt2img_generate':
                self.p_kw = kwargs
                self.p_com = component
                
            if kwargs.get('elem_id') == 'img2img_generate':
                self.ip_kw = kwargs
                self.ip_com = component
