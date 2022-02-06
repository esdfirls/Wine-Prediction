# App Widget for jupyter notebooks.


def model_api():

    import requests
    from ipywidgets import Label, BoundedFloatText, Dropdown, Button, Output, VBox, Layout

    prescribe_label = Label('Wine Quality prediction')
    tipo = Dropdown(options=[0, 1], description='Tipo:', disabled=False)
    fixed = BoundedFloatText(min=3, max=16, value=7, description="fixed acidity:", disabled=False)
    volatile = BoundedFloatText(min=0, max=2, value=1, description="volatile acidity:", disabled=False)
    citric = BoundedFloatText(min=0, max=2, value=1, description="citric acid:", disabled=False)
    residual = BoundedFloatText(min=0, max=70, value=45, description="residual sugar:", disabled=False)
    chlorides = BoundedFloatText(min=0, max=0.7, value=0.5, description="chlorides:", disabled=False)
    freesulfur = BoundedFloatText(min=1, max=300, value=150, description="free SO2:", disabled=False)
    totalsulfur = BoundedFloatText(min=6, max=450, value=200, description="total SO2:", disabled=False)
    density = BoundedFloatText(min=0.98, max=1.04, value=1, description="density:", disabled=False)
    ph = BoundedFloatText(min=2.7, max=4.1, value=3, description="ph:", disabled=False)
    sulphates = BoundedFloatText(min=0.2, max=2, value=1, description="sulphates:", disabled=False)
    alcohol = BoundedFloatText(min=8, max=15, value=10, description="alcohol:", disabled=False)



    prescribe_button = Button(description="Is a good wine?")
    prescribe_output = Output()

    # Button click event handlers ...
    def prescribe_button_on_click(b):
        
        request_url = f"https://winepredict.azurewebsites.net/wine?tipo={tipo.value}&fixed={fixed.value}&volatile={volatile.value}&citric={citric.value}&residual={residual.value}&chlorides={chlorides.value}&freesulfur={freesulfur.value}&totalsulfur={totalsulfur.value}&density={density.value}&ph={ph.value}&sulphates={sulphates.value}&alcohol={alcohol.value}"
        response = requests.get(request_url)
        Wine_Type = response.json()["Wine_Type"]    

        prescribe_output.clear_output()
        with prescribe_output:

            print(f"This Wine is a {Wine_Type}")
            
    prescribe_button.on_click(prescribe_button_on_click)

    vbox_prescribe = VBox([prescribe_label, tipo, fixed, volatile, citric, residual, chlorides, freesulfur, totalsulfur, density, ph, sulphates, alcohol, prescribe_button, prescribe_output], layout=Layout(width='100%', height='100%'))

    return vbox_prescribe
