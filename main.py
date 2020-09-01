from flask import Flask, render_template, request, flash
import pickle
import os
app = Flask('__name__')
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('tranform.pkl', 'rb'))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    text = request.form['text']
    prediction = model.predict(vectorizer.transform([text]))
    if prediction[0]==0:
      flash(f'This is not a spam email.', 'success')
    else:
      flash('This is a spam email.', 'danger')
    return render_template('index.html')



if __name__== '__main__':
  app.run(host='0.0.0.0', port=8080)