from flask import Flask, request, jsonify
import os
app= Flask(__name__)

uploadfolder='uploads/'
if not os.path.exists(uploadfolder):
    os.makedirs(uploadfolder)

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error':'No file part'})
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error':'No selected file'})
    file.save(os.path.join(upload_file,file.filename))
    return jsonify({'message':'File uploaded','filename':file.filename})
if __name__ =='__main__':
    app.run(debug=True)
