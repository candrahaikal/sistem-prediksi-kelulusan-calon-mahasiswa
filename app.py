from flask import Flask, request, render_template
import pickle
import numpy as np
import math

app = Flask(__name__)

model_file = open('svm_model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', output='')

@app.route('/predict', methods=['POST'])
def predict():

    nama = request.form['nama']
    tahun = request.form['tahun']
    jeniskelamin = request.form['jeniskelamin']
    Q1 = int(request.form['Q1'])
    Q2 = int(request.form['Q2'])
    Q3 = int(request.form['Q3'])

    Q1_olah = ''
    Q2_olah = ''
    Q3_olah = ''

    if Q1 >= 200 and Q1 <= 400:
        Q1_olah = 1
    elif Q1 >= 401 and Q1 <= 580:
        Q1_olah = 2
    elif Q1 >= 581 and Q1 <= 800:
        Q1_olah = 3

    if Q2 >= 310 and Q2 <= 450:
        Q2_olah = 1
    elif Q2 >= 451 and Q2 <= 500:
        Q2_olah = 2
    elif Q2 >= 501 and Q2 <= 677:
        Q2_olah = 3

    if Q3 >= 0 and Q3 <= 3:
        Q3_olah = 1
    elif Q3 >= 4 and Q3 <= 6:
        Q3_olah = 2
    elif Q3 >= 7 and Q3 <= 10:
        Q3_olah = 3
    

    prediction = model.predict([[Q1_olah, Q2_olah, Q3_olah]])
    output = ''

    if prediction == 1:
        output = 'Rendah'
    elif prediction == 2:
        output = 'Menengah'
    elif prediction == 3:
        output = 'Tinggi'

    return render_template('index.html', output=output, nama=nama, tahun=tahun, jeniskelamin=jeniskelamin, Q1=Q1,Q2=Q2,Q3=Q3)


if __name__ == '__main__':
    app.run(debug=False)