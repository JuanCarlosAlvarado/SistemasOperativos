import pyodbc

# Conexión a SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=LAPTOP-L5BTHTKJ;'
                      'DATABASE=DB_ahora_si_PC02;'
                      'UID=sa;'
                      'PWD=845623197')

cursor = conn.cursor()

# Inserción de datos
Identificacion = 'Juan'
Titulo="Curso"
Profesor="Juan"
Descricion="El curso de juan"

cursor.execute("INSERT INTO Usuariosssssssssssssss (Identificacion, Titulo, Profesor, Descricion) VALUES (?, ?, ?, ?)", (Identificacion, Titulo, Profesor, Descricion))
conn.commit()

print("Datos insertados correctamente.")
