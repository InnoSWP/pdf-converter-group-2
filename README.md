![GitHub Super-Linter](https://github.com/InnoSWP/pdf-converter-group-2/workflows/Lint%20Code%20Base/badge.svg)
![https://badgen.net/badge/:subject/:status/:color?icon=github](https://badgen.net/badge/icon/terminal?icon=terminal&label)
![https://badgen.net/badge/:subject/:status/:color?icon=github](https://badgen.net/badge/license/MIT/red)
# MF-PDF
A Doc to PDF converter that uses API implementation. The program can convert multiple fils in a relatively fast speed. The program can also convert XLSX files to PDF.

## How to use
* Open any terminal
* Enter the directory of the files in the terminal
* use the command: `curl -F`
* Put in the name of the file with quotations, eg: `"file=@filename.docx"`
* If the file is an excel make sure to change the type to `xlsx`
* Put in the program on the server address: `http://77.91.73.240:5000/convert/pdf`
* For zip of multiple files conversion use: `http://77.91.73.240:5000/convertFolder/pdf`
* Put in the name of the resulted PDF after `-o`, eg:  `-o Result.pdf`
* Full command line example: `curl -F "file=@filename.docx" http://77.91.73.240:5000/convert/pdf -o Result.pdf`

## Demo Screenshots
### Single File:
Docx and Xlsx files before conversion:

<img src="images/singlesbefore.png" width="550" >

Conversion process:

<img src="images/cmd.png" width="800" >

New PDF files in the directory:

<img src="images/singlesresults.png" width="550" >

### Multiple Files:

Zip file with the files that should be converted:

<img src="images/multiplebefore.png" width="550" >

Conversion process:

<img src="images/cmd2.png" width="800" >

New Zip folder that contains converted PDF files in the same directory:

<img src="images/multipleafter.png" width="550" >


## Features
* Simple conversion process
* No external programs needed
* Secure operation
* Fast conversion speed
* Works on all Operating Systems

## Technology and License
The program currently uses LibreOffice library
The progeam uses the MIT License
