
from menu import Menu
from adicionar_tarefa import adicionar_nova_tarefa
from alterarstatus_tarefas import MudarDisponibilidade
from localizar_tarefas import localizar_tarefas
from remover_tarefas import MudarDisponibilidade

 
def main():
    
    tarefas=[]
    
    while True:
        print("\nBem-vindo à gestão da biblioteca!")
        escolha= Menu()
        
        if escolha == "1":
            adicionar_nova_tarefa(tarefas)
                
        elif escolha == "2":
            print(tarefas)
        
        elif escolha == "3":
            localizar_tarefas(tarefas)
    
        elif escolha == "4":
            MudarDisponibilidade(tarefas)
    
        elif escolha == "5":
            MudarDisponibilidade(tarefas)
        
        elif escolha.lower() == "sair" :
            print("Saindo do programa...") 
            break
        
        else: 
            print("Escolher opçao correta.") 
            break


if __name__== "__main__":
    main()