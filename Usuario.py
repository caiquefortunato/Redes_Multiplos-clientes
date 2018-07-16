from ConteudoMsg import *

class Usuario :
    def __init__ (self, mensagem):
        self.msg = mensagem.split(" ")
        self.usuario = self.msg[0]
        self.senha = self.msg[1]
        self.listaArquivo = []

    def getUsuario(self):
        return self.usuario
         
    def getSenha(self):
        return self.senha

    def __verificaArq__(self, titulo, grava) :
        for item in self.listaArquivo :
            if(item.getTitulo() == titulo) : 
                return True 

        if(grava == "s") :
            l_Arq = ConteudoMsg()
            l_Arq.setTitulo(titulo)
            self.listaArquivo.append(l_Arq)
        return False

    def setMensagemArq(self, titulo, mensagem) :
        # Verifica se existe arquivo
        if(self.__verificaArq__(titulo, 's') == True) :
            for item in self.listaArquivo :
                if(item.getTitulo() == titulo) : 
                    if(item.getConteudo() == "") : 
                        item.setConteudo(mensagem)
                        return 3
                    else : 
                        item.setConteudo(mensagem)
                        return 4
        # Se arquivo nao existe, crio.
        else :
            for item in self.listaArquivo :
                if(item.getTitulo() == titulo) : 
                    item.setConteudo(mensagem)
            return 3     
    
    def consultaMensagem(self, titulo) :
        # Verifica se existe arquivo
        if(self.__verificaArq__(titulo, 'n') == True) :
            for item in self.listaArquivo :
                if(item.getTitulo() == titulo) : 
                    if(item.getConteudo() == "") : 
                        return 3
                    else : return item.getConteudo()
        else :
            return 4
        
    def getListaArquivos(self) :
        listaAux = []
        for item in self.listaArquivo :
            listaAux.append(item.getTitulo())
        #arquivos = ''.join(listaAux)

        return str(listaAux)[1:-1]


