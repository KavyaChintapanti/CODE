
from django.shortcuts import render
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from .models import Pests
import os 
import numpy as np

# Create your views here.
def index(request):
    return render (request,"index.html")


def about(request):
    return render (request,"about.html")

def upload(request):
    return render(request,"upload.html")

def result(request):
    return render(request,"result.html")




def result(request):
    if request.method == 'POST':
        classes = []
        path = os.listdir(r"../Backend/pest/test")
        for i in path:
            classes.append(i)
        selection = int(request.POST['alg'])
        file = request.FILES['pest']
        a = Pests(image=file)
        a.save()

        path1 = 'app/static/pestssave/' + a.filename()
        path2 = 'static/pestssave/' + a.filename()

        model = load_model(r"../Backend/models/CNNcroppest.h5")
        x = image.load_img(path1, target_size=(64, 64))
        x = image.img_to_array(x)
        x = np.expand_dims(x, axis=0)
        x /= 255

        result = model.predict(x)
        b = np.argmax(result)
        Results = classes[b]
        print(Results)

        '''if Results == 'aphids':
            mssg = 'Merits: Rapid reproduction aids research, Ecologically important as prey.'
            mssg1='Demerits: Crop damage through sap-sucking, Transmit plant diseases, reducing yields.'

        elif Results == 'armyworm':
            mssg = 'Merits:Rapid reproduction,Versatility in host plants,High adaptability to diverse climates.'
            mssg1='Demerits:Crop devastation,Economic losses,Resistance to pesticides.'

        elif Results == 'beetle':
            mssg = 'Merits:Beetles control pests, aiding natural balance and reducing crop damage'
            mssg1='Demerits:Some beetles harm crops, causing economic losses and yield reduction.'

        elif Results == 'bollworm':
            mssg = 'Merits:Resistant crops reduce pesticide use, promoting sustainable agriculture and minimizing environmental impact'
            mssg1='Demerits:Develops resistance, necessitating constant innovation in pest management, leading to increased costs and potential ecological imbalances.'

        elif Results == 'grasshopper':
            mssg = 'Merits:Grasshoppers control weeds, contribute to nutrient cycling, and serve as a food source for predators in ecosystems'
            mssg1='Demerits:Grasshopper swarms can devastate crops, causing significant agricultural losses and impacting food security for communities relying on agriculture.'

        elif Results == 'mites':
            mssg = 'Merits:Natural predators, biocontrol agents, aid in pest population control, reduce need for chemical pesticides'
            mssg1='Demerits: Potential to become pests, damage crops, disrupt ecological balance, require monitoring and management.'
        elif Results == 'mosquito':
            mssg = 'Merits:Mosquitoes pollinate plants and serve as a food source for various animals, contributing to ecosystem balance.'
            mssg1='Demerits:Mosquitoes transmit diseases, causing widespread illness and posing a threat to human and animal health.'

        elif Results == 'sawfly':
            mssg = 'Merits:Natural pollinators,Serve as prey for beneficial insects.'
            mssg1='Demerits:Larvae damage crops,Resistant to certain pesticides.'

        elif Results == 'stem_borer':
            mssg = 'Merits:Enhances natural selection, drives plant resistance, and promotes ecosystem balance by controlling weaker plants, fostering resilience.'
            mssg1='Demerits:Causes yield loss, reduces crop quality, demands increased pesticide use, jeopardizes food security, and escalates economic burdens on farmers.' '''


        return render(request, "result.html", {"result": Results, "path": path2})
    return render(request, "result.html", {"result": Results, "path": path2})



    return render(request,"result.html")