#6. Crie o Arquivo remover.py: Este módulo deve conter a função que remove uma tarefa do sistema.
class RemoverTarefa:
    def __init__(self, tarefas):
        self.tarefas= tarefas
            
    def encontrar_tarefa(self, titulo):
        for tarefa in self.tarefas :
            if tarefa["Titulo"] == titulo:
                return tarefa
        return None
    
    def remover_tarefa(self, titulo):
        tarefa_encontrada=self.encontrar_tarefa(titulo)
        
        if tarefa_encontrada:
            self.tarefas.remove(tarefa_encontrada)
            print(f"Tarefa '{titulo}' removida com sucesso.")
        else:
            print(f"Tarefa com o título '{titulo}' não encontrada.")
    
@staticmethod
def MudarDisponibilidade(tarefas):
    titulo= input("Digite o nome da tarefa que deseja excluir: ")
    remover= RemoverTarefa(tarefas)
    remover.remover_tarefa(titulo)
    
    