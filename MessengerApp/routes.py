from flask import render_template, url_for, flash, redirect

@app.route('/')
@app.route('/home')
def index():
    return render_template('base.html')
