import random

def alternate():
    responses = ["It seems I don't understand you, please try re-phrasing in a way I can understand."
    ,"Repeat yourself, but slowly...", "It's all gibberish to me, I only speak English I'm afraid."
    ,"I don't even think you understood what you said. I'm just a chatbot, make it easy for me pleases."
    ,"I'll pretend I'm following you, but I probably won't do what you want me to, so let's do that again."]

    random_num = random.choice(responses)

    print(""+str(random_num))
