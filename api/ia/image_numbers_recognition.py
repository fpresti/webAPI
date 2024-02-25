import tensorflow as tf

class ArtificialNeuronalNetwork :

    def generate_random_image() :
        #Cargamos los datasets default de Keras
        from tensorflow.keras import datasets

        #Utilizamos el dataset mnist, que son 60.000 imágenes de 28x28 pixeles de números del 0 al 9 escritas a mano. Y además hay 10.000 casos de test.
        mnist = datasets.mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()

        #Visualizando conjunto de datos

        import random
        numero_aleatorio = random.randint(0, 9999)
        X_new = X_test[numero_aleatorio]
        import numpy as np   
        from PIL import Image as image

        data = image.fromarray(X_new)
        name_file = "random_image_pic.png"        
        data.save(name_file)

        return ({'image_file_name':name_file, 'X': X_new})

    def predict(X) :
        import numpy as np   
        # Preprocesamos la nueva imagen que queremos predecir
        X_new_prep = X.reshape((1, 28*28)) #hay que pre procesar esta imágen, la dejamos en forma de vector
        X_new_prep = X_new_prep.astype('float32') / 255
        # Importamos las librerias necesarias
        from tensorflow.keras.models import load_model
        # Cargamos el nuestra RNA entrenada de disco
        mnist_model = load_model("static/trained_ia/model_mnist.h5") 
        # Realizamos una nueva prediccion
        y_pred = np.argmax(mnist_model.predict(X_new_prep), axis=-1)

        return y_pred
