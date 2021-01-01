from flask import Flask, flash, render_template, request
from werkzeug.utils import secure_filename

import librosa.display
import scipy.io.wavfile as wavfile
import numpy
import os.path
from os import walk
from scipy import stats
import numpy as np
import librosa 
import numpy as np
from scipy.stats import norm
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
UPLOAD_FOLDER = 'C:/Users/Nada Mekki/Desktop/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
           

	
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
         file = request.files['file']
         if file.filename == '':
              flash('No selected file')
              return 'No file selected'
         if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          
          signal, rate = librosa.load(filename)  
           #The Mel Spectrogram
          S = librosa.feature.melspectrogram(signal, sr=rate, n_fft=2048,    hop_length=512, n_mels=128)
          S_DB = librosa.power_to_db(S, ref=np.max)
          S_DB = S_DB.flatten()[:1200]
          clf = pickle.load(open('../SVM.pkl' , 'rb'))
          ans = clf.predict([S_DB])[0]
          music_class = str(ans)
          # print(music_class)
          if(music_class == 'blues'):
                return "blues"
          elif(music_class == 'classical'):
                return "classical"
          elif(music_class == 'country'):
                return "country"
          elif(music_class == 'disco'):
                return "disco"
          elif(music_class == 'hiphop'):
                return "hiphop"
            
          elif(music_class == 'metal'):
                return "metal"
          elif(music_class == 'pop'):
                return "pop"
          else:
                return "error in predicting music"
      
		
if __name__ == '__main__':
   app.run(debug = True)