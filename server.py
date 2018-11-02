from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'emilys super-secret key'

@app.route('/')
def counter():
    if 'visits' in session:
        session['visits'] = session['visits'] + 1
    else:
        session['visits']=1
    return render_template('index.html')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    print("I'm destroying the session")
    session.clear()		# clears all keys
    # session.pop('key_name')		# clears a specific key 
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)