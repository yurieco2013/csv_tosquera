
import csv
import random as rd


def input_file(new_file=False):
    if not new_file:
        file_ = input('nome do arquivo (com extensão.csv): ')
    else:
        file_ = input('nome do novo arquivo (com extensão.csv): ')
    return file_


def input_clmn():
    colunmx = input('nome da nova coluna: ')
    return colunmx

#---------------------------------------------------------
# aqui esta o segredo: talvez role ate um read_file()
# dentro dessa func pra pegar valores de outro arquivo


def new_clmn_input(x):
    try:
        out = x ** 2
        return out
    except:
        return x


#----------------------------------------------------------


def read_file(seu_arquivo_csv, HEADER=True):
    """ Argumentos -> str nome do arquivo; HEADER= True(default).
    Retorna uma tupla: x[0] = lista com as linhas do doc csv; x[1] =
    HEADER(bool); x[2] = numero de linhas do doc csv; x[3] = numero
    de colunas """

    lst = []
    counter = 0

    with open(seu_arquivo_csv, newline='\n') as read_file:
        reader = csv.reader(read_file, delimiter=',')

        for row in reader:
            counter += 1
            lst.append(row)
        clmns = len(row)
    print (lst[0][1])

    return (lst, HEADER, counter, clmns)


def write_file(lst):
    final_name = input_file(new_file=True)
    print(type(lst))
    with open(final_name, mode='w', newline='\n') as read_file:
        writer = csv.writer(read_file, delimiter='\t')
        for x in lst:
            writer.writerow(x)


def add_column():
    lst, HEADER, lines, columns = read_file(input_file(), HEADER=True)
    if HEADER:
        counter = 0
        lst1 = []
        name = input_clmn()
        for list_line in lst:
            if counter == 0:
                list_line.append(name)    
            else:
                list_line.append(new_clmn_input(counter)) # lembra da func magica
            counter += 1
            lst1.append(list_line)
    return list(lst1)


x = add_column()
print(type(x))
write_file(x)
