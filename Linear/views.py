import pickle
from django.shortcuts import render
from Linear.forms import House_Area_Form
# Create your views here.
Model_path = "E:\Python in Sublime\DJango Framework\Projects\Linear_Model\Linear\static\model\linear_regression_model.pkl"

def Home(request):
    form = House_Area_Form()
    result = None

    if request.method == 'POST':
        form = House_Area_Form(request.POST)
        if form.is_valid():
            Area = form.cleaned_data['Area']
            result = load_model(Area)
            
    return render(request,template_name="base.html",
                  context={"house_area":form,"Area":result})




def load_model(Square_Feets):
    with open(Model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    predictions = loaded_model.predict([[Square_Feets]])
    return int(predictions.tolist()[0])