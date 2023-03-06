import os
import xml.etree.ElementTree as ET

def generar_tabla(largo, ancho, organismos):
    imprimirPag = '''
    graph main {
    '''
    if largo <= 10000 and ancho <= 10000:
        try:
            s = '''nodo1 [shape=plaintext, label=<
                        <table border="2" cellborder="1" cellspacing="7">
                '''

            n = 0
            for i in range(0, largo + 1):
                m = 0
                s2 = '''
                <tr>
                '''
                s += s2
                for j in range(0, ancho + 1):
                    if i == 0 and j == 0:
                        s3 = f'''
                        <td></td>
                        '''
                    elif i == 0:
                        s3 = f'''
                        <td>{j}</td>
                        '''
                    elif j == 0:
                        s3 = f'''
                        <td>{i}</td>
                        '''
                    else:
                        org = organismos.get((i, j), {"organismo": "", "estado": " "})
                        s3 = f'''
                        <td>{org["organismo"]}({org["estado"]})</td>
                        '''
                    s += s3
                    m += 1
                s4 = '''
                </tr>
                '''
                s += s4
                n += 1

            s5 = '''
                </table>>]
            '''
            s6 = '}'

            with open('Bacterias.dot', 'w') as f:
                f.write(imprimirPag)
                f.write(s)
                f.write(s5)
                f.write(s6)

            os.system('dot -Tpdf Bacterias.dot -o Bacterias.pdf')

        except:
            print("Ocurrio un Error")
    else:
        print("Ha ingresado un numero invalido de columnas o Filas")
