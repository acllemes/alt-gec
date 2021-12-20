#! / usr / bin / python3
# _ * _ codificação: utf-8 _ * _
from  flask  importar  Flask , solicitar
de  flask_restful  importação  de recursos , Api
importar  get_ip_interface  como  gii
classe  principal ():
    def  __init__ ( self ):
        fl . start_flask ()

classe  executa_requisicao ( Recurso ):
    def  get ( self ):
        interface  =  gii . principal ()
        saida  =  interface . saida
        retorno  saida
    def  post ( self ):
        interface  =  gii . principal ()
        saida  =  interface . saida
        retorno  saida


classe  fl ():
    def  start_flask ():
        app  =  Flask ( __name__ )
        api  =  Api ( app )
        api . add_resource ( executa_requisicao , '/' )
        app . executar ( debug = True , host = '192.168.80.130' , porta = 8081 )
if  __name__  ==  "__main__" :
    principal ()
