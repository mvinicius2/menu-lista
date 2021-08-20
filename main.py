import modulo as mod
import menu as m
#m.menu()

opcao = m.menu()
while opcao != 0:
    if opcao == 1:
     mod.primeiraquest()
    if opcao == 2:
        mod.segundaquest()
    if opcao == 3:
        mod.terceiraquest()
    if opcao == 4:
        mod.quartaquest()
    if opcao == 5:
        mod.quintaquest()
    if opcao == 6:
        mod.sextaquest()
    if opcao == 7:
        mod.setimaquest()
    if opcao == 8:
        mod.oitavaquest()
    opcao = m.menu()