#####################################################
# Probably not gonna use json, compare to finance app
#####################################################

from flask import Flask, request, jsonify

app = Flask(__name__)

clothes = []
outfits = []

@app.route('/clothes', methods=['POST'])
def add_clothes():
    new_clothing = request.json
    clothes.append(new_clothing)
    return jsonify(new_clothing), 201

@app.route('/clothes/<int:clothing_id>', methods=['DELETE'])
def delete_clothes(clothing_id):
    global clothes
    clothes = [clothing for clothing in clothes if clothing['id'] != clothing_id]
    return '', 204

@app.route('/outfits', methods=['POST'])
def add_outfit():
    new_outfit = request.json
    outfits.append(new_outfit)
    return jsonify(new_outfit), 201

@app.route('/outfits/<int:outfit_id>', methods=['DELETE'])
def delete_outfit(outfit_id):
    global outfits
    outfits = [outfit for outfit in outfits if outfit['id'] != outfit_id]
    return '', 204

@app.route('/outfits/<int:outfit_id>', methods=['PUT'])
def modify_outfit(outfit_id):
    updated_outfit = request.json
    for outfit in outfits:
        if outfit['id'] == outfit_id:
            outfit.update(updated_outfit)
            return jsonify(outfit), 200
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)