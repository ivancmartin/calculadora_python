class Calculadora():
	def __init__(self):
		self.operacion=""
		self.__valorTotal=0


	def __sumar(self,num1,num2):
		try:
			return num1+num2
		except ValueError:
			return False
		except TypeError:
			return False

	def __restar(self,num1,num2):
		return num1 - num2

	def __multiplicar(self,num1,num2):
		return num1 * num2

	def __dividir(self,num1,num2):
		return num1 / num2

	def __comprobar_num(self,num):
		pass 

	def introducir_valor(self,valor):
		print(valor)
		return valor
		pass

	def operar(self,valor):
		self.__valorTotal

		if self.operacion == 0:
			try:
				self.__valorTotal+=int(valor)
			except:
				print("no realiza la operacion")
		elif self.operacion == 1:
			try:
				self.__valorTotal-=int(valor)
			except:
				print("no realiza la operacion")
		elif self.operacion == 2:
			try:
				self.__valorTotal**=int(valor)
			except:
				print("no realiza la operacion")
		else:
			self.__valorTotal=0

		print(self.__valorTotal)

	def obtenerResultado(self):
		return self.__valorTotal
		
		#3+2-5*2/2

