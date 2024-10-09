import os
import json
import modules.mensajes as msg
import modules.validate as val
"""
MY_DATABASE = None

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)
    
def AddData(*param):
    with open(MY_DATABASE,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            try:
                data_file.get(param[0]).update(param[1])
            except AttributeError:
                pass
        else:
            data_file.update({param[0]})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])

def delData(*param):
    decision = bool(input('Desea borrar la informacion, Presione cualquier tecla para (Si) Enter(No)'))
    if decision:
        data = list(param)
        if val.validateResponse(msg.msgDelete):
            camperBorrar= data[2].get(data[0]).pop(data[1])
            NewFile(data[2])
    else:
        print('No se elimino la informacion')
"""