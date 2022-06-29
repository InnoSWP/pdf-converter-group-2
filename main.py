import os.path
import tempfile
import io
import subprocess
from xmlrpc.client import Boolean
import zipfile
from email import message
from urllib import response
from flask import Flask, jsonify, request, send_file, url_for, redirect

app = Flask(__name__)

types = ["docx", "doc"]


@app.route('/convertmultiple/pdf', methods=["POST"])
def convert_mul_pdf():
    if 'file' not in request.files:
        response = jsonify({'message': 'file part is missed'})
        response.status_code = 400  # Bad request
        return response
    archive = tempfile.NamedTemporaryFile(prefix="Muhammadjon", suffix=".zip")
    acrhive_zip = zipfile.ZipFile(archive.name, 'w')
    list_uploaded_file = request.files.getlist('file')
    for i in range(len(list_uploaded_file)):
        uploaded_file = list_uploaded_file[i]
        uploaded_file_name = uploaded_file.filename.rsplit('.', 1)[0]
        extension = uploaded_file.filename.rsplit('.', 1)[-1]
        extension_length = len(extension)
        temp_file = tempfile.NamedTemporaryFile(prefix=uploaded_file_name, suffix="." + extension, delete=True)
        if extension not in types:
            response = jsonify({'message': 'Not a appropriate type'})
            response.status_code = 409  # Conflict
            return response
        if uploaded_file:
            pdf = open(uploaded_file.name[:-extension_length] + "pdf", "w")
            pdf_name = pdf.name
            uploaded_file.save(temp_file)
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf", temp_file.name, "--outdir", os.path.dirname(pdf.name)])
            pdf = open(pdf_name, "rb")
            newFile = io.BytesIO(pdf.read())
            newFile.seek(0)
            acrhive_zip.write(pdf.name, os.path.basename(pdf.name))
            pdf.close()
        temp_file.close()
    return send_file(archive, as_attachment=True, attachment_filename=
    archive.name + "zip")


@app.route('/convert/pdf', methods=["POST"])
def convert_pdf():
    if 'file' not in request.files:
        response = jsonify({'message': 'file part is missed'})
        response.status_code = 400  # Bad request
        return response
    file = request.files['file']
    extension = file.filename.rsplit('.', 1)[-1]
    extension_length = len(extension)
    temp_file = tempfile.NamedTemporaryFile(suffix="." + extension, delete=True)
    if extension not in types:
        response = jsonify({'message': 'Not a appropriate type'})
        response.status_code = 409  # Conflict
        return response
    if file:
        pdf = open(temp_file.name[:-extension_length] + "pdf", "w")
        file.save(temp_file)
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", temp_file.name, "--outdir", os.path.dirname(pdf.name)])
        pdf = open(temp_file.name[:-extension_length] + "pdf", "rb")
        newFile = io.BytesIO(pdf.read())
        newFile.seek(0)
        pdf.close()
        return send_file(newFile, as_attachment=True, attachment_filename=file.filename[:-extension_length] + "pdf")
    temp_file.close()


if __name__ == "__main__":
    app.run(host='77.91.73.240')
