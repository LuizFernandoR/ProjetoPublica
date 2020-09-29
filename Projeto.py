from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host= 'localhost',
    user=  'root',
    passwd= '',
    database= 'projeto_publica'
)

def chama_segunda_tela():
    cadastro.show()
def chama_consulta():
    consulta.show()

    cursor = banco.cursor()
    comando_SQL = 'select num_cad_jogo,placar_cad_jogo,min_temporada,max_temporada,quebra_recorde_min,quebra_recorde_max from cadastro_jogo'
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    

    consulta.tableWidget.setRowCount(len(dados_lidos))
    consulta.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0,6):
            consulta.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    

def funcao_principal():
    
    qbr_rcd_min = 0
    qbr_rcd_max = 0
    min_temp =  'select max(min_temporada) from cadastro_jogo'
    max_temp =  'select max(max_temporada) from cadastro_jogo'
    
    campo1 = cadastro.lineEdit.text()
    campo2 = int(cadastro.lineEdit_2.text())
    cadastro.lineEdit.setText('')
    cadastro.lineEdit_2.setText('')
    

    if campo2 > max_temp:
        max_temp = campo2
        min_temp = min_temp
        qbr_rcd_max = 1
        qbr_rcd_min= 0
    else:
        min_temp = campo2
        max_temp = max_temp
        qbr_rcd_min = 1
        qbr_rcd_max = 0


    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO cadastro_jogo (num_cad_jogo,placar_cad_jogo,min_temporada,max_temporada,quebra_recorde_min,quebra_recorde_max) values (%s,%s,%s,%s,%s,%s)'
    dados = int(campo1),int(campo2),int(min_temp),int(max_temp),int(qbr_rcd_min),int(qbr_rcd_max)
    cursor.execute(comando_SQL,dados)
    banco.commit()



app=QtWidgets.QApplication([])
tela1=uic.loadUi('tela1.ui')
cadastro=uic.loadUi('cadastro.ui')
consulta=uic.loadUi('consulta.ui')
tela1.pushButton.clicked.connect(chama_segunda_tela)
tela1.pushButton_2.clicked.connect(chama_consulta)
cadastro.pushButton_2.clicked.connect(funcao_principal)

tela1.show()
app.exec()