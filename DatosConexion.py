class DatosConexion ():
      
      def __init__(self):
        global DB_HOST  
        global DB_USER  
        global DB_PASS
        global DB_NAME 
        self.DB_HOST = "localhost"
        self.DB_USER = "homestead"
        self.DB_PASS = "secret"
        self.DB_NAME = "bancasoft"
