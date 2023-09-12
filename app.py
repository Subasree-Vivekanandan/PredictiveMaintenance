# -*- coding: utf-8 -*-

import pandas as pd
from flask import Flask, request,render_template
import pickle as pkl

app = Flask(__name__)
#log_reg_model = pkl.load(open('log_reg.pkl','rb'))
#dec_tree_model = pkl.load(open('dec_tree.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/logreg')
def logreg_page():
    return render_template('lr_upload.html')

@app.route('/lrpredict',methods=['POST'])
def predict_logreg(): 
    return render_template('check_p.html')
    
@app.route('/dectr')
def decisiontree_page():
    return render_template('dt_upload.html')

@app.route('/dtpredict',methods=['POST'])
def predict_decisiontree(): 
    return render_template('check_p.html')

#@app.route('/upload')
#def upload_route_summary():
#    return render_template('upload.html')

#@app.route('/file',methods=['POST'])
#def file_upload():
#       f = request.files.get('fileupload')
#       df = pd.read_csv(f, encoding='latin-1')
#       output = df.to_numpy()
#       output_arr = np.array(output)
       
#       return render_template('display.html', dict_output=output_arr)
    
if __name__ == "__main__":
    app.run(debug=True)    
        
    
    
    