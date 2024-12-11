#####################################################
# Probably not gonna use json, compare to finance app
#####################################################

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'nicoPau2',
    'database': 'wardrobio'
}

#clothes = []
#outfits = []

@app.route('/outfits')
def outfits():
    return render_template('outfits.html')

@app.route('/wardrobe')
def wardrobe():
    return render_template('wardrobe.html')

@app.route('/clothes/<int:clothing_id>', methods=['DELETE'])
def delete_clothes(clothing_id):
    global clothes
    clothes = [clothing for clothing in clothes if clothing['id'] != clothing_id]
    return '', 204

@app.route('/outfitsjhb', methods=['POST'])
def add_outfit():
    new_outfit = request.json
    outfits.append(new_outfit)
    return

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
            return
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)