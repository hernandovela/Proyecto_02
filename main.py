from flask import Flask, jsonify, request

app = Flask(__name__)
nameApi = '/api/'

@app.route(nameApi)
def usuario():
    return jsonify({"usaurio":"get"})

@app.route(nameApi+'crear',methods=["POST"])
def usuarioCrear():
    data=request.get_json()
    return jsonify(data)

@app.route(nameApi+'actualizar',methods=["PUT"])
def usuarioActaulizar():
   return jsonify({"usaurio":"actualizar 3"})


if __name__ == '__main__':
    app.run(debug=True)
