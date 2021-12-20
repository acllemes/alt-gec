#! / usr / bin / python3
# _ * _ codificação: utf-8 _ * _

importar
telnetlib, re, json
do
pool
de
importação
de
multiprocessamento
tempo
de
importação
classe
principal():


def __init__(self):
    equipamentos = [{'ip': '10 .95.1.1 ', ' usuario ': ' usuario1 ', ' senha ': ' senha1 ', ' hostname ': "R1"}, \
                    {'ip': '10 .95.1.3 ', ' usuario ': ' usuario2 ', ' senha ': ' senha2 ', ' hostname ': "R2"}]
    instancias = []
    dado_saida = []
    com
    Pool(2)
    como
    p:
    instancias.anexar(p.map(conexao_equipamento, equipamentos))


para
i
em
instancias:
para
k
em
i:
dado_saida.anexar(k.dado_host)
eu.saida = dado_saida


def get_dado(self):
    retornar
    a
    si
    mesmo.saida


classe
conexao_equipamento():


def __init__(self, dado):
    eu.ip = dado['ip']
    eu.usuario = dado['usuario']
    eu.senha = dado['senha']
    eu.hostname = dado['hostname']
    eu.start_conn()
    saida = self.get_ip()
    lista_interface = texto.extract_ip(saida)
    eu.dado_host = {self.nome
    do
    host: lista_interface}

    def send_command(self, command, new_line=True):
        if (new_line):
            eu.tn.write((command + ' \ n ').encode())
        mais:
        eu.tn.escrever((comando).encode())


def read_command(self, pattern, return_exit=False):
    saida = self.tn.read_until(pattern.encode()).decodificar()
    if (return_exit):
        retorno
        saida


def start_conn(self):
    eu.tn = telnetlib.Telnet()
    eu.tn.aberto(auto.ip, '23', 100)
    eu.read_command(':')
    eu.send_command(self.usuario)
    eu.read_command(':')
    eu.send_command(self.senha)
    eu.read_command('#')


def get_ip(self):
    eu.send_command("show ip int brief")
    saida = self.read_command("#", Verdadeiro)
    retorno
    saida


classe
texto():


def extract_ip(dado):
    dado = dado.dividir(" \ n ")
    dado = dado[2: len(dado) - 1]
    lista_interface = []
    para
    i
    em
    dado:
    i = re.sub(r
    '\ s +', '', i )
    interface = i.dividir('')
    lista_interface.append({'interface': interface[0], 'ip': interface[1], \
                            'status': interface[4]})


retornar
lista_interface
if __name__ == "__main__":
    principal()