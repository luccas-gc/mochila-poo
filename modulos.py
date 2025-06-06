class Item:
    def __init__(self, nome: str, tipo: str, peso: int):
        self.nome = nome
        self.tipo = tipo
        self.peso = peso

    def __str__(self):
        return (f"{self.nome} - ({self.tipo}, {self.peso})")
    
class Mochila:
    def __init__(self):
        self.peso_mochila = 0
        self.peso_maximo = 50
        self.lista_items = []

    @property
    def peso(self):
        return (f"\nA mochila está Pesando {self.peso_mochila} KG.")
    
    def __str__ (self):
        return "\nItens na mochila:\n" + "\n".join(str(item) for item in self.lista_items)
    
    def add_items(self, item: Item):
        self.item = item
        if item.peso + self.peso_mochila > 50:
            print("\nVocê ultrapassou o Limite de 50KG.")
        elif item.peso < 0:
            print("\nNão é possível adicionar peso nulo ou negativo.")
            return

        if self.peso_mochila > self.peso_maximo:
            print("\nVocê ultrapassou o Limite de 50KG.")
            return
        else:
            self.lista_items.append(item)
            self.peso_mochila += item.peso

    def remove_items(self, del_item):
        self.del_item = del_item
        for item in self.lista_items:
            if item.nome == del_item:
                self.peso_mochila -= item.peso
                self.lista_items.remove(item)
                print(f"{del_item} Removido da Mochila.")
                return
        print (f"\nNão há itens com o nome {del_item}")

mochila = Mochila()
