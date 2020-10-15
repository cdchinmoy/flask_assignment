from flask import Flask, render_template, jsonify, request
import os
import json
import os.path

app = Flask(__name__)

@app.route("/")
def index():
    path_to_json = 'files/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    path_to_json = 'files/NZX_AFT_2020-03.json'

    with open(path_to_json, 'r', encoding='utf-8') as infile:
        data = infile.read()
        final_data = json.loads(data)
        pdf_meta = final_data['pdf-meta']
        #find the filename
        file_name = pdf_meta['name']
        date = pdf_meta['creation_date']
        #dt = json.dumps(final_data['data'], indent=4)
        k = list()
        for gg,hh in final_data['data'].items():  
            pp = {}
            val = list()
            for kk,ll in hh.items():
                for jj in ll:
                    val.append(jj['value']) 
            pp['filename'] = file_name
            pp['metric'] = gg
            pp['date'] = date        
            pp['value'] = val 
            #print(pp) 
            k.append(pp)
           
        return render_template('template.html', my_string="Flask App", my_list=k, files=json_files, filename=file_name)



@app.route("/loaddata", methods=['GET','POST'])
def loaddata():
    
    data = request.get_json()
    filename = data['filename']
    '''
    jdic = jsonify( {'filename' : filename} )
    return jdic
    '''
    path_to_json = 'files/'+str(filename)

    with open(path_to_json, 'r', encoding='utf-8') as infile:
        data = infile.read()
        final_data = json.loads(data)
        pdf_meta = final_data['pdf-meta']
        #find the filename
        file_name = pdf_meta['name']
        date = pdf_meta['creation_date']
        #dt = json.dumps(final_data['data'], indent=4)
        k = list()
        for gg,hh in final_data['data'].items():  
            pp = {}
            val = list()
            for kk,ll in hh.items():
                for jj in ll:
                    val.append(jj['value']) 
            pp['filename'] = file_name
            pp['metric'] = gg
            pp['date'] = date        
            pp['value'] = val 
            #print(pp) 
            k.append(pp)

    return render_template('content.html',  my_list=k)


@app.route("/updatejson", methods=['POST'])    
def updatejson():   
    data = request.form

    if 'filename' in data:
        filename = data['filename']

    filled_data = {}
    for key, f_data in data.items():
        if f_data != "":
            filled_data[key] = f_data

    path_to_json = "files/"+str(filename)
    if(os.path.isfile(path_to_json)):
        for filled_data_key, filled_data_value in filled_data.items():
            filled_data_value = filled_data_value.split(".", 1)
            index = 
        


    else:
        status = 'not found'    


    return jsonify( {'gg':status} )

    
if __name__ == '__main__':
    app.run(debug=True)