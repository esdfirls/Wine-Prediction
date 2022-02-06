from flask import Flask

import pickle
from flask import request, jsonify

app = Flask(__name__)

def predict_wine(tipo, fixed, volatile, citric, residual, chlorides, freesulfur, totalsulfur, density, ph, sulphates, alcohol):
    """
        This function imports an machine learning model and runs a prediction.

        Args:
            tipo (int): 0 or 1 value, label encoded for white wine and red wine.
            all others (float): values from lab test of a wine.
        Returns:
            string: output a string that tells if the wine is good or bad.
    
    """
    mapper = {0:"Bad Wine", 1:"Good Wine"}
    
    pickle_file = open('model_wine.pkl', 'rb')     
    model = pickle.load(pickle_file)
    y_predict = model.predict([[tipo, fixed, volatile, citric, residual, chlorides, freesulfur, totalsulfur, density, ph, sulphates, alcohol]])[0]
    return mapper[y_predict]

@app.route("/")
def hello():
    return "A test web service for accessing a machine learning model to see if a wine is good or bad."

@app.route('/wine', methods=['GET'])
def api_all():
    """
        Building API.

        Args:
            Predict Wine Inputs (tipo, fixed, volatile, citric, residual, chlorides, freesulfur, totalsulfur, density, ph, sulphates, alcohol)
        Returns:
            Json : Wine Type, Good or Bad.
        
    """

    tipo = int(request.args['tipo'])
    fixed = float(request.args['fixed'])
    volatile = float(request.args['volatile'])
    citric = float(request.args['citric'])
    residual = float(request.args['residual'])
    chlorides = float(request.args['chlorides'])
    freesulfur = float(request.args['freesulfur'])
    totalsulfur = float(request.args['totalsulfur'])
    density = float(request.args['density'])
    ph = float(request.args['ph'])
    sulphates = float(request.args['sulphates'])
    alcohol = float(request.args['alcohol'])


    wine = predict_wine(tipo, fixed, volatile, citric, residual, chlorides, freesulfur, totalsulfur, density, ph, sulphates, alcohol)

    return(jsonify(Wine_Type = wine))

