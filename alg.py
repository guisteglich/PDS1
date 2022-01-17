from datetime import datetime
class Produto:

    def __init__(self, codigo, data_inicial, data_final, hora, nome, preco, quantidade):
        self.codigo = codigo
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.hora = hora
        self.nome = nome 
        self.preco = preco
        self.quantidade = quantidade

    def info_detalhes(self):
        print("---------------Informações--------------------------")
        print ("Item : "+str(self.nome))
        print ("Preco : " + str (self.preco) + ' R$')
        print ("Codigo : "+str(self.codigo))
        print ("Quantidade : " + str (self.quantidade) +' unidades')
        print ("Data início preço: "+str(self.data_inicial))
        print ("Data fim preço: "+str(self.data_final))
        print ("Hora : "+str(self.hora))

class Estoque(Produto):

    def __init__(self , Nome_Estoque , id):
        self.Lista_de_Produtos = []
        self.Lista_de_Quantidade = []
        self.Lista_de_Venda = []
        self.Nome_Estoque = Nome_Estoque
        self.id = id

    def imprime_Nome_Estoque(self):
        print("----------------Nome do Estoque : " + str(self.Nome_Estoque))


    def imprime_Lista_de_Produtos_Estoque(self):
        print("----------------imprimindo Lista de Produtos-------------")
        tam = self.Lista_de_Produtos.__len__()
        for i in range (tam):
            Produto = self.Lista_de_Produtos[i]
            print(Produto.codigo)


    def imprime_Lista_de_Vendas(self):
        print("----------------imprimindo Lista de vendas-------------")
        print(self.Lista_de_Venda)


    def imprime_numero(self):
        print ('Numero de Identificação do Estoque : '+ str(self.id))

    def imprime_detalhadamente_Lista_de_Produtos(self):
        print("--------------------Lista detalhada de Produtos ----------------------")
        aux = 0
        tam = self.Lista_de_Produtos.__len__()
        for i in range (tam):
            Produto = self.Lista_de_Produtos[i]
            Produto.info_detalhes()

    def Adicionar_Produto_Estoque(self ,Produto):
        print("-------------------- Adicionando Produto ao Estoque ----------------------")
        self.Lista_de_Produtos.append(Produto)
        self.Lista_de_Quantidade.append(Produto.quantidade)
        print('Produto : '+ str(Produto.nome))
        print('Qtd : ' + str(Produto.quantidade))
        print(str(Produto.preco)+str('R$'))
        print("-------------------- ------------------------------ ----------------------")


    def Adicionar_Venda_Estoque(self, venda):
        self.Lista_de_Venda.append(venda)
        #print (self.Lista_de_Venda)
        print ("Venda adicionado com sucesso : "+str(venda))


class Vendas(Estoque) :

    def __init__(self , data):
        self.Lista_de_Vendas_carrinho = []
        self.data_venda = data
        self.status = False
        self.total = 0.0

    def concluir_venda(self):
        print('Concluindo Compra !!!')
        self.status = True


    def adiciona_item(self , Produto):
      if(self.status == False):
        print("++++++++++++++ Carrinho de compras ++++++++++++++")
        self.Lista_de_Vendas_carrinho.append(Produto)
        print("Produto adicionado a lista item:"+str(Produto.codigo))
        print("--------------------------------------------------")
      else:
        print('----Impossivel add produto Compra Concluida !!!')

    def imprime_Lista_de_Vendas_no_carrinho(self):
        print("---------------- Produtos no carrinho--------------------")

        tam = self.Lista_de_Vendas_carrinho.__len__()
        for i in range(tam):
            Produto = self.Lista_de_Vendas_carrinho[i]
          
            data_inicial = datetime.strptime(Produto.data_inicial, "%d/%m/%Y")
            data_final = datetime.strptime(Produto.data_final,  "%d/%m/%Y")
           
            if data_inicial <= self.data_venda <= data_final:
                self.total += float(Produto.preco)
                print(Produto.nome + str('               ') + str(Produto.preco) + str('R$'))
        print('Valor Total : '+ str(self.total) + ' R$')
        print("----------------------------------------------------")

    def info_detalhes(self):

        print("---------------Informações--------------------------")
        print ("Item : "+str(self.item))
        print ("Codigo : "+str(self.codigo))
        print ("Data : "+str(self.data))
        print ("Hora : "+str(self.hora))
        print("----------------------------------------------------")

    def get_tam_Lista_Vendas(self):
        tam = self.Lista_de_Vendas_carrinho.__len__ ()
        return (tam)

    def remove_item(self , Produto):
       try:

           flag =  self.Lista_de_Vendas_carrinho.index(Produto)
           print("Codigo encontrado :" + str(Produto.codigo))
           self.Lista_de_Vendas_carrinho.pop(flag)

       except ValueError:

           print('Erro codigo não encontrado :'+str(Produto.codigo))


class Preco(Produto):

    def __init__(self , Produto):
        data_inicial = datetime.strptime(Produto.data_inicial, "%d/%m/%y")
        data_final = datetime.strptime(Produto.data_final, "%d/%m/%y")

        self.preco = Produto.preco
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.hora = Preco.hora
        self.item = Preco.nome

    def aloca_item(self , Produto , Estoque):
        print('---------Decrementando Produto no Estoque--------------------')
        Produto.quantidade = Produto.quantidade - 1
        pos = Estoque.Lista_de_Produtos.index(Produto)
        aux = Estoque.Lista_de_Quantidade[pos]
        aux = aux - 1
        Estoque.Lista_de_Quantidade[pos] = aux
        print('-'+str(pos))
        print(Estoque.Lista_de_Quantidade)
        print ('-------------------------------------------------------------')

class Items_Venda(Produto):

    def __init__(self , data , qtd ,status):
        self.data = data
        self.quantidade = qtd
        self.status = status


    def imprime_quantidade_de_Items_Venda(self):
        print('\n\n\n\n\n------------------ITEM VENDIDO---------------------------')
        print("Data da compra : " +str(self.data))
        print ("Quantidade de Itens : " + str (self.quantidade))
        if(self.status == True):
            print('Status : Compra concluida ')
        print ('--------------------------------------------------')

Estoque = Estoque('Estoque1' , '20121200')
produto_a = Produto('001' , '14/01/2022' , '16/04/2022', '02h' , 'camiseta do Grêmio 2021' , '100.00' , 20)
produto_b = Produto('002' , '01/02/2022' , '16/02/2022', '22h' , 'calça jeans' , '200.00' , 30)
produto_c = Produto('0032' , '16/01/2022' , '16/02/2022', '12h' , 'moletom preto' , '300.00' , 2)
produto_a2 = Produto(produto_a.codigo, '17/01/2022', '25/02/2022', '10h', produto_a.nome, '250', 10)


Estoque.Adicionar_Produto_Estoque(produto_a)
Estoque.Adicionar_Produto_Estoque(produto_b)
Estoque.Adicionar_Produto_Estoque(produto_c)
Estoque.Adicionar_Produto_Estoque(produto_a2)
Estoque.imprime_detalhadamente_Lista_de_Produtos()


sacola = Vendas(datetime.now())
sacola.adiciona_item(produto_a)
sacola.adiciona_item(produto_b)
sacola.adiciona_item(produto_c)
sacola.imprime_Lista_de_Vendas_no_carrinho()
sacola.concluir_venda()
