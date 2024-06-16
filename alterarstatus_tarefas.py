class alterarstatus:
    def __init__(self, tarefas):
        self.tarefas= tarefas
        
        
    def EncontrarTarefa(self, titulo):
        for tarefa in self.tarefas :
            if tarefa["Titulo"] == titulo:
                return tarefa
        return None
    
        
    def MudarTarefa(self, titulo, disponibilidade):
        
        tarefa= self.EncontrarTarefa(titulo)
        if tarefa:
            tarefa["Disponibilidade"] = disponibilidade
            print(f"Disponibilidade da tarefa '{titulo}' foi alterada para {disponibilidade}.")
        else:
            print(f"Tarefa com o título '{titulo}' não encontrada.")

@staticmethod
def MudarDisponibilidade(tarefas):
    titulo= input("Digite o nome da tarefa que deseja mudar: ")
    disponibilidade= input("Digite 'true' para disponível ou 'false' para não disponível: ").lower() == 'true'
    modificar= alterarstatus(tarefas)
    modificar.MudarTarefa(titulo, disponibilidade)
