#!/usr/bin/env python

from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

@app.route('/7601cb2b', methods=['GET','POST'])
def intro():
    if request.method == 'POST':
        lastname = request.form.get('lastname','')
        if lastname.lower() == 'smisko':
            return redirect(url_for('challenge1'))
    return render_template('intro.html')

@app.route('/a7e2d5e1', methods=['GET','POST'])
def challenge1():
    START = [ [0, 1, 0, 0, 4, 6, 0, 0, 0],
              [6, 0, 0, 3, 0, 0, 0, 0, 0],
              [3, 4, 8, 7, 2, 0, 0, 6, 9],
              [0, 0, 1, 0, 0, 0, 0, 8, 0],
              [4, 0, 7, 0, 0, 0, 3, 0, 5],
              [0, 6, 0, 0, 0, 0, 7, 0, 0],
              [7, 3, 0, 0, 8, 2, 9, 1, 4],
              [0, 0, 0, 0, 0, 7, 0, 0, 8],
              [0, 0, 0, 4, 1, 0, 0, 7, 0] ] 

    SOLUTION = [ [2, 1, 9, 8, 4, 6, 5, 3, 7],
                 [6, 7, 5, 3, 9, 1, 8, 4, 2],
                 [3, 4, 8, 7, 2, 5, 1, 6, 9],
                 [9, 5, 1, 2, 7, 3, 4, 8, 6],
                 [4, 2, 7, 1, 6, 8, 3, 9, 5],
                 [8, 6, 3, 9, 5, 4, 7, 2, 1],
                 [7, 3, 6, 5, 8, 2, 9, 1, 4],
                 [1, 9, 4, 6, 3, 7, 2, 5, 8],
                 [5, 8, 2, 4, 1, 9, 6, 7, 3] ] 

    passed = True

    if request.method == 'POST':
        for i in xrange(9*9):
            try:
                if SOLUTION[i/9][i%9] != int(request.form.get('%d' % i,
                                                          START[i/9][i%9])):
                    passed = False
                    break
            except ValueError:
                passed = False
                break
        if passed:
            return redirect(url_for('challenge2')) 
    return render_template('challenge1.html', START=START) 
    
@app.route('/b937b618', methods=['GET','POST'])
def challenge2():
    if request.method == 'POST':
        answer = request.form.get('answer', '')
        if answer.lower() == 'pi':
            return redirect(url_for('challenge3'))
    return render_template('challenge2.html') 

@app.route('/cb330558', methods=['GET','POST'])
def challenge3():
    if request.method == 'POST':
        answer = request.form.get('answer','')
        if answer.lower() == 'gg':
            return redirect(url_for('finish'))
    return render_template('challenge3.html') 

@app.route('/4a58e873', methods=['GET'])
def finish():
    return render_template('finish.html') 

@app.route('/')
def root():
    return redirect(url_for('intro')) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
