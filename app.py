# -*- coding: utf-8 -*-
import uuid

from flask import Flask, session, request
import aiml

k = aiml.Kernel()


k.learn("aiml/default.aiml")
k.learn("aiml/nombres.aiml")
k.learn("aiml/numeros.aiml")
k.learn("aiml/sara.aiml")
k.learn("aiml/sara_srai.aiml")

app = Flask("IA-P1")
app.secret_key = 'oDgYSmjdFgEqCQDuTlQX'


@app.route("/")
def hello():
  return "Hello world"

@app.route('/session/')
def display_chatbot_ui():
  session['session_id'] = unicode(uuid.uuid4())
  return '''
        <form action="/session/talk" method="post">
            <p><input type=text name=message>
            <p><input type=submit value=Send>
        </form>
    '''


@app.route('/session/talk', methods=['POST'])
def create_message():
  if not session.get('session_id'):
      abort(401)
  message_sent = request.form['message']
  session_id = session['session_id']
  ai_message = k.respond(message_sent, 'session_id')
  #flash('New entry was successfully posted')
  return ai_message


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

