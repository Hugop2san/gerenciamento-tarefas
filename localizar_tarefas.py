class localizarTarefas():
    
    def __init__(self, localizar):
        self.localizar= localizar
        
        
    def EncontrarTarefa(self, titulo):
        for tarefa in self.localizar :
            if tarefa["Titulo"] == titulo:
                return tarefa
        return None
    
@staticmethod
def localizar_tarefas(tarefas):
    titulo= input("Digite o nome da tarefa que deseja pesquisar: ")
    mostrar= localizarTarefas(tarefas)
    print(mostrar.EncontrarTarefa(titulo))
