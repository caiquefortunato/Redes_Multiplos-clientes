from Usuario import *

class ProtocoloCloud :
    def __init__ (self) :
        self.listaObj = []
    
    def setMensagem(self, mensagem) : self.msg = mensagem

    def __verificaUsuario__ (self, usuario) :
        ver = False
        for item in self.listaObj :
            if(usuario == item.getUsuario()) : ver = True
        return ver
    
    def __verificaSenha__ (self, usuario, senha) :
        if(self.__verificaUsuario__(usuario)) :
            for item in self.listaObj :
                if(usuario == item.getUsuario()) :
                    if(senha == item.getSenha()) : return True
                    else : return False

    def __interpretaDadosRegistro__ (self) :
        msg = self.msg.split(" ")
        usuario = msg[1]
        senha = msg[2]

        user = Usuario(self.msg[2:])

        flag = self.__verificaUsuario__(usuario)

        if(flag == False) :
            self.listaObj.append(user)
            return True
    
    def __interpretaDadosRecebimento__(self) :
        msg = self.msg.split(" ")
        usuario = msg[1]
        senha = msg[2]
        arquivo = msg[3]

        # Verifico se existe ou nao a senha/user
        verUsuario = self.__verificaUsuario__(usuario)
        if(verUsuario == False) : return 1
        verSenha = self.__verificaSenha__(usuario, senha)
        if(verSenha == False) : return 2

        for user in self.listaObj :
            if(usuario == user.getUsuario()) :
                r = user.consultaMensagem(arquivo)
        return r

    def __interpretaDadosLista__(self) :
        msg = self.msg.split(" ")
        usuario = msg[1]
        senha = msg[2]
        resposta = ""

        # Verifico se existe ou nao a senha/user
        verUsuario = self.__verificaUsuario__(usuario)
        if(verUsuario == False) : return 1
        verSenha = self.__verificaSenha__(usuario, senha)
        if(verSenha == False) : return 2

        for user in self.listaObj :
            if(usuario == user.getUsuario()) :
                r = user.getListaArquivos()

        for carac in r :
            if(carac is not "'" and carac is not ",") :
                resposta += carac
        
        return resposta

    def __interpretaDadosEnvio__ (self) :
        msg = self.msg.split(" ")
        usuario = msg[1]
        senha = msg[2]
        arquivo = msg[3]
        space = 0
        carac = 0

        # Verifico se existe ou nao a senha/user
        verUsuario = self.__verificaUsuario__(usuario)
        if(verUsuario == False) : return 1
        verSenha = self.__verificaSenha__(usuario, senha)
        if(verSenha == False) : return 2

        # Defininando a mensagem enviada
        for n in self.msg :
            carac += 1
            if (n == " ") : space += 1
            if (space == 4) : break
        msg_user = self.msg[carac:]
        
        for user in self.listaObj :
            if(usuario == user.getUsuario()) :
                r = user.setMensagemArq(arquivo, msg_user)
        
        return r

    def retornaResposta (self) :
        if(self.msg[0] == "N") :
            if (self.__interpretaDadosRegistro__()) : return ("N 0")
            else : return ("N -1")

        elif(self.msg[0] == "S") :
            r = self.__interpretaDadosEnvio__()
            if(r == 1) : return ("S -1")
            elif(r == 2) : return ("S -2")
            elif(r == 3) : return ("S 0")
            elif(r == 4) : return ("S 1")
            else : return ("S 0 ")#,self.msg[3])

        elif(self.msg[0] == "R") :
            r = self.__interpretaDadosRecebimento__()
            if(r == 1) : return ("R -1")
            elif(r == 2) : return ("R -2")
            elif(r == 3 or r == 4) : return ("R -3")
            else: 
                r = str(r)
                return ("R 0 "+r)

        else : 
            r = self.__interpretaDadosLista__() 
            if(r == 1) : return ("L -1")
            elif(r == 2) : return ("L -2")
            else : 
                r = str(r)
                return ("L 0 "+r)