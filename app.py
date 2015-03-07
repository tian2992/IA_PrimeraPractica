# -*- coding: utf-8 -*-

from flask import Flask
import aiml

k = aiml.Kernel()


k.learn("default.aiml")
k.learn("nombres.aiml")
k.learn("numeros.aiml")
k.learn("sara.aiml")
k.learn("sara_srai.aiml")

app = Flask("my-app")

@app.route("/")
def hello():
  return "Hello world"


if __name__ == "__main__":
  app.run()
