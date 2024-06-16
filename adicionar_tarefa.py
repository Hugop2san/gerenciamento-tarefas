class AdicionarTarefa():
    def __init__(self,titulo, descricao ):
        self.titulo= titulo
        self.descricao= descricao
        
    def thisseftarefa(self):
        tarefa= {
            "Titulo": self.titulo,
            "Descricao": self.descricao,
            "disponibilidade":False
        }
        return tarefa
        
        
    # Função para adicionar uma nova tarefa
@staticmethod
def adicionar_nova_tarefa(tarefas):
        titulo = input("Digite o título da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        nova_tarefa = AdicionarTarefa(titulo, descricao)
        task= nova_tarefa.thisseftarefa()
        tarefas.append(task)
        print("Tarefa adicionada com sucesso!")
        
        
        
        

