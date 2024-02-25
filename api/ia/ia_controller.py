from flask import Blueprint, make_response, jsonify
from PIL import Image
from api.ia.image_numbers_recognition import ArtificialNeuronalNetwork

ia_bp = Blueprint('ia', __name__, url_prefix='/ia')

@ia_bp.get('/getrandomnumber')
def get_random_number():    
    
    try : 
        random_image = ArtificialNeuronalNetwork.generate_random_image()

        import io
        image = Image.open(random_image['image_file_name'])
        image_buffer = io.BytesIO()
        image.save(image_buffer, format='PNG')
        image_bytes = image_buffer.getvalue()
        response = make_response(image_bytes)
        response.headers['Content-Type'] = 'image/png'

        #print prediction in the console.
        print(f"Prediction: {ArtificialNeuronalNetwork.predict(random_image['X'])} !")

        return response
    
    except Exception as ex :
        return f"Error: {ex}"
    