import psycopg2

try:
    conn = psycopg2.connect(host = 'localhost', port = 5435, database = 'postgres', user = 'moredev', password = '123456')
    print('Conexão realizada com sucesso.........')
except:
    print('Conexão nao realizada.........')

if conn is not None:
    print("Sua conexao esta estavel")

    cursor = conn.cursor()

    cursor.execute("CREATE table teste (id serial PRIMARY KEY, nome VARCHAR(15), sobrenome VARCHAR(15));")

    print("Tabela criada")
    conn.commit()
    cursor.close()
    conn.close()




