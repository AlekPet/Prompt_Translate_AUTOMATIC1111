import launch

if not launch.is_installed('googletrans'):
    launch.run_pip("install googletrans==3.1.0a0", "Need to prompt_translate")
