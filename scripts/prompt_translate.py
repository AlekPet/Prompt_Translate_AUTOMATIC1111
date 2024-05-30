# Title: Prompt translate script for AUTOMATIC1111/stable-diffusion-webui
# Description: Prompt translator into other languages
# GitHub: https://github.com/AlekPet/Prompt_Translate_AUTOMATIC1111
# Date: 2024.05.30
import re
import modules.scripts as scripts
import gradio as gr

from modules.processing import Processed, process_images
from modules.shared import opts, cmd_opts, state
# from deep_translator import GoogleTranslator
from scripts.module_translate import PromptTranslate

promptTranslate = PromptTranslate()

class Script(scripts.Script):

    def title(self):
        return "Prompt Tranlsate"
    

    def show(self, is_img2img):
        return scripts.AlwaysVisible

       
    def ui(self, is_img2img):
        dom, translate_enabled, translate_service, gtrans, srcTrans, toTrans, change_src_to, adv_trans, p_tr, p_n_tr, translate_proxy_enabled, translate_proxy, translate_auth_data, viewstrans, proxy_settings = promptTranslate.createElements()

        translate_service.change(promptTranslate.setComboBoxesSrcTo, inputs=translate_service, outputs=[srcTrans, toTrans, translate_proxy, translate_auth_data])
                
        if not is_img2img :
            gtrans.click(promptTranslate.translateByClick, inputs=[srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data, translate_service, self.txt2img_prompt, self.txt2img_neg_prompt], outputs=[self.txt2img_prompt, self.txt2img_neg_prompt, p_tr, p_n_tr])
            self.p_com.click(promptTranslate.translateByClick, inputs=[srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data, translate_service, self.txt2img_prompt, self.txt2img_neg_prompt], outputs=[p_tr,p_n_tr])

        else:
            gtrans.click(promptTranslate.translateByClick, inputs=[srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data, translate_service, self.img2img_prompt, self.img2img_neg_prompt], outputs=[self.img2img_prompt, self.img2img_neg_prompt, p_tr, p_n_tr])
            self.ip_com.click(promptTranslate.translateByClick, inputs=[self.img2img_prompt,self.img2img_neg_prompt, srcTrans, toTrans], outputs=[p_tr, p_n_tr])

            
        change_src_to.click(promptTranslate.change_lang, inputs=[srcTrans,toTrans], outputs=[srcTrans, toTrans])
        adv_trans.change(lambda x: gr.update(visible=x), inputs=adv_trans, outputs=viewstrans)

        translate_proxy_enabled.change(lambda x: gr.update(visible=x), inputs=translate_proxy_enabled, outputs=proxy_settings, queue=False, show_progress=False)      

        return [translate_enabled, translate_service, srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data]
    

    def listTransale(self, tlist, translate_service, srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data):
        result = []
        for ap in tlist:
            translate_prompt, _ = promptTranslate.deep_translate_text(srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data, translate_service, ap, "")
            result.append(translate_prompt)      
        return result

   
    def process(self, p, translate_enabled, translate_service, srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data):
        if not translate_enabled:
            return

        if p.prompt:
            prompt, negative_prompt = promptTranslate.deep_translate_text(srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data, translate_service, p.prompt, p.negative_prompt)
            setattr(p, 'prompt', prompt)               
            setattr(p, 'negative_prompt', negative_prompt)

            all_prompts = self.listTransale(getattr(p,'all_prompts',[prompt]), translate_service, srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data)
            all_negative_prompts = self.listTransale(getattr(p,'all_negative_prompts',[negative_prompt]), translate_service, srcTrans, toTrans, translate_proxy_enabled, translate_proxy, translate_auth_data)

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
