from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

banco = mysql.connector.connect(
    host= 'localhost',
    user=  'root',
    passwd= '',
    database= 'projeto_publica'
)
def chama_tela1():
    tela1.show()

def chama_segunda_tela():
    cadastro.show()    

def chama_consulta():
    consulta.show()

    cursor = banco.cursor()
    comando_SQL = 'select num_cad_jogo,placar_cad_jogo,min_temporada,max_temporada,quebra_recorde_min,quebra_recorde_max from cadastro_jogo'
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    consulta.tableWidget.setRowCount(len(dados_lidos))
    consulta.tableWidget.setColumnCount(6)
    
    for i in range(0, len(dados_lidos)):
       for j in range(0,6):
            consulta.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
def funcao_principal():
    cursor = banco.cursor()
    SQL = 'select min(min_temporada) from cadastro_jogo' 
    cursor.execute(SQL,)
    dados_min = cursor.fetchall()

    cursor = banco.cursor()
    SQL_ = 'select max(max_temporada) from cadastro_jogo' 
    cursor.execute(SQL_)
    dados_max = cursor.fetchall()

    cursor = banco.cursor()
    SQL_ = 'select max(quebra_recorde_min) from cadastro_jogo' 
    cursor.execute(SQL_)
    dados_quebra_rcd_min = cursor.fetchall()

    cursor = banco.cursor()
    SQL_ = 'select max(quebra_recorde_max) from cadastro_jogo' 
    cursor.execute(SQL_)
    dados_quebra_rcd_max = cursor.fetchall()
    
    min_temp = dados_min[0][0]
    max_temp = dados_max[0][0]
    qbr_rcd_min = 0
    qbr_rcd_max = 0

    dado_lido = cadastro.lineEdit.text()
    dado_lido_2 = cadastro.lineEdit_2.text()
    if(dado_lido == '') or (dado_lido_2 == ''):
        QMessageBox.about(cadastro,'Atenção','Dados incorretos')
    else:
        campo1 = cadastro.lineEdit.text()
        campo2 = int(cadastro.lineEdit_2.text())
        cadastro.lineEdit.setText('')
        cadastro.lineEdit_2.setText('')
        if (max_temp == None) and (min_temp == None):
            max_temp = campo2
            min_temp = campo2
            qbr_rcd_max = 0
            qbr_rcd_min= 0
        elif campo2 >= max_temp:
            max_temp = campo2
            min_temp = dados_min[0][0]
            qbr_rcd_max = 1
            qbr_rcd_min= dados_quebra_rcd_min[0][0]
        else:
            min_temp = campo2
            max_temp = dados_max[0][0]
            qbr_rcd_min = 1
            qbr_rcd_max = dados_quebra_rcd_max[0][0]

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
cadastro.pushButton_2.clicked.connect(chama_tela1)
tela1.show()
app.exec()
