This simple application shows that smolagent result is being evaluated by langfuse. We need to create a account in langfuse by selecting US / Europe. Here we need to create a project, to get Secret and public keys. After running our application all calls to tools are appeared here. The results are appeared as a form of screenshots. on click codeagent.run in langfuse as shown in langfuse1 screenshot, the calls used by agent will be displayed which can be seen in langfuse2 screenshot

1. Pre-requisite:
    Python should be installed
    Any editor (I have used Visual Studio Code)
2. Download folder
3. Go to CLI or terminal
4. Make sure you are inside the folder and type below one by one
    1. uv init
    2. uv add -r requirements.txt
5. Add your huggingface key token and prompt in .env file
    1. uv run sample_langfuse.py