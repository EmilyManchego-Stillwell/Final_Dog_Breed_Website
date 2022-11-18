import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import re

from flask import Flask, request, render_template

loaded_model = tf.keras.models.load_model('./ml_model/final_export/trained_model.h5',
    custom_objects={'KerasLayer': hub.KerasLayer(
    "https://tfhub.dev/tensorflow/resnet_50/classification/1",
    input_shape=(224, 224, 3),
    trainable=False)})

class_names = ['n02085620-Chihuahua',
 'n02085936-Maltese_dog',
 'n02086079-Pekinese',
 'n02086240-Shih-Tzu',
 'n02086910-papillon',
 'n02087046-toy_terrier',
 'n02087394-Rhodesian_ridgeback',
 'n02088094-Afghan_hound',
 'n02088238-basset',
 'n02088364-beagle',
 'n02088466-bloodhound',
 'n02088632-bluetick',
 'n02089078-black-and-tan_coonhound',
 'n02089867-Walker_hound',
 'n02089973-English_foxhound',
 'n02090379-redbone',
 'n02090622-borzoi',
 'n02090721-Irish_wolfhound',
 'n02091032-Italian_greyhound',
 'n02091134-whippet',
 'n02091244-Ibizan_hound',
 'n02091467-Norwegian_elkhound',
 'n02091635-otterhound',
 'n02091831-Saluki',
 'n02092002-Scottish_deerhound',
 'n02092339-Weimaraner',
 'n02093256-Staffordshire_bullterrier',
 'n02093428-American_Staffordshire_terrier',
 'n02093647-Bedlington_terrier',
 'n02093754-Border_terrier',
 'n02093859-Kerry_blue_terrier',
 'n02093991-Irish_terrier',
 'n02094114-Norfolk_terrier',
 'n02094258-Norwich_terrier',
 'n02094433-Yorkshire_terrier',
 'n02095314-wire-haired_fox_terrier',
 'n02095570-Lakeland_terrier',
 'n02095889-Sealyham_terrier',
 'n02096051-Airedale',
 'n02096177-cairn',
 'n02096294-Australian_terrier',
 'n02096437-Dandie_Dinmont',
 'n02096585-Boston_bull',
 'n02097047-miniature_schnauzer',
 'n02097130-giant_schnauzer',
 'n02097209-standard_schnauzer',
 'n02097298-Scotch_terrier',
 'n02097474-Tibetan_terrier',
 'n02097658-silky_terrier',
 'n02098105-soft-coated_wheaten_terrier',
 'n02098286-West_Highland_white_terrier',
 'n02098413-Lhasa',
 'n02099267-flat-coated_retriever',
 'n02099429-curly-coated_retriever',
 'n02099601-golden_retriever',
 'n02099712-Labrador_retriever',
 'n02099849-Chesapeake_Bay_retriever',
 'n02100236-German_short-haired_pointer',
 'n02100583-vizsla',
 'n02100735-English_setter',
 'n02100877-Irish_setter',
 'n02101006-Gordon_setter',
 'n02101388-Brittany_spaniel',
 'n02101556-clumber',
 'n02102040-English_springer',
 'n02102177-Welsh_springer_spaniel',
 'n02102318-cocker_spaniel',
 'n02102480-Sussex_spaniel',
 'n02102973-Irish_water_spaniel',
 'n02104029-kuvasz',
 'n02104365-schipperke',
 'n02105162-malinois',
 'n02105251-briard',
 'n02105412-kelpie',
 'n02105505-komondor',
 'n02105641-Old_English_sheepdog',
 'n02105855-Shetland_sheepdog',
 'n02106030-collie',
 'n02106166-Border_collie',
 'n02106382-Bouvier_des_Flandres',
 'n02106550-Rottweiler',
 'n02106662-German_shepherd',
 'n02107142-Doberman',
 'n02107312-miniature_pinscher',
 'n02107574-Greater_Swiss_Mountain_dog',
 'n02107683-Bernese_mountain_dog',
 'n02107908-Appenzeller',
 'n02108000-EntleBucher',
 'n02108089-boxer',
 'n02108422-bull_mastiff',
 'n02108551-Tibetan_mastiff',
 'n02108915-French_bulldog',
 'n02109047-Great_Dane',
 'n02109525-Saint_Bernard',
 'n02109961-Eskimo_dog',
 'n02110063-malamute',
 'n02110185-Siberian_husky',
 'n02110627-affenpinscher',
 'n02110806-basenji',
 'n02110958-pug',
 'n02111129-Leonberg',
 'n02111277-Newfoundland',
 'n02111500-Great_Pyrenees',
 'n02111889-Samoyed',
 'n02112018-Pomeranian',
 'n02112137-chow',
 'n02112350-keeshond',
 'n02113023-Pembroke',
 'n02113186-Cardigan',
 'n02113624-toy_poodle',
 'n02113712-miniature_poodle',
 'n02113799-standard_poodle',
 'n02113978-Mexican_hairless']

app = Flask(__name__, template_folder='')
app.config['UPLOAD_FOLDER']= '/tmp'

@app.route('/')
@app.route('/index.html')
def index():
    return(render_template('index.html'))

@app.route('/BreedInfo.html', methods=['GET', 'POST'])
def BreedInfo():
    prediction_name = ''
    prediction_percentage = ''
    prediction_result = ''
    if request.method == 'POST':
        file = request.files['img']
        img_path=f'/tmp/{file.filename}'
        file.save(img_path)
        
        img_input = image_input(img_path)

        prediction = loaded_model.predict(img_input)
        prediction_name = label_clean(class_names[np.argmax(prediction)])
        prediction_percentage = f'{np.max(prediction)*100:0.2f}' 
        prediction_result = f'The predicted breed is { prediction_name }, with a probability of { prediction_percentage }.'
        
    return(render_template('BreedInfo.html', prediction_result = prediction_result))

@app.route('/about.html')
def about():
    return(render_template('about.html'))

img_height = 224
img_width = 224

def label_clean(label):
    search = re.search('.{9}-(.*)', label)
    
    label_clean = search.group(1).replace("_", " ")\
        .replace("-", " ")\
        .title()\
        .strip()
    return label_clean

def image_input(img):
    img = tf.io.read_file(img)

    # parse the image as a uint8 tensor, 3 channels for RGB color
    img = tf.image.decode_jpeg(img, channels=3)

    # convert color channels from [0-255] to [0-1]. done here as opposed to in a model layer for increased efficiency
    img = tf.image.convert_image_dtype(img, tf.float32)

    # resize the image to  standardized size
    img = tf.image.resize(img, [img_height, img_width])

    # expand size so that image matches the shape of binned images used to train the model
    img = np.expand_dims(img, axis=0)

    return img