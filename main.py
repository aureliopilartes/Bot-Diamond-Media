# relevant packages & modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as gui

# VERSAO DE TESTES

class Main():

	def __init__(self):
		pass

	def Conect(self):
		
		self.driver = webdriver.Firefox()

		self.driver.get("https://diamondvideomedia.com/login")

	def Login(self):
		
		gui.alert("      BOT - DIAMOND MEDIA \nLinkedin: Aurélio Pilartes Lander\n")

		gui.alert("Em caso de erros ou duvidas entre em contacto!")

		gui.alert("PROGRAMA GRATUITO, NÃO PAGUE NEM COBRE POR ELE!")

		self.user = gui.prompt("USUARIO: ")

		self.password = gui.password("SENHA: ")

		gui.alert("   Fazendo sua renda extra {0} vá descansar...!" .format(self.user))

		if self.user == "" or self.password == "":
			
			gui.alert("            LOGIN ERRADO! ")

		else:

			self.Conect()

			# LOCALIZANDO OS ELEMENTOS NA PAGINA E CLICANDO

			try:
				user = self.driver.find_element_by_id('van-field-1-input')

				passwd = self.driver.find_element_by_id('van-field-2-input')

				login_button = self.driver.find_element_by_class_name('van-button')
			
				user.send_keys(self.user)

				passwd.send_keys(self.password)

				time.sleep(2)

				login_button.click()

				time.sleep(2)

				self.getTasks() # Chamando o metodo que faz as tarefas

			except Exception as e:

				print("LOGIN FALHOU: ", e)

			else:
				pass
			finally:
				pass


	def getTasks(self):

		try:

			self.driver.get("https://diamondvideomedia.com/mytask")
			

			while True:

			
				task_list = self.driver.find_elements(By.XPATH, '//div[@class="list-item"]')

				for task in task_list:

					task.click()

					time.sleep(2)

					self.driver.get("https://diamondvideomedia.com/mytask")

					time.sleep(4)


															# Tentando pegar o elemento da modal

					task_finished = self.driver.find_element(By.XPATH,'//*[contains(text(), "Concluído")]') # Nao funciona

					# task_finished = self.driver.find_element(By.XPATH,'//button[@type="button'])[2]") Nao funciona

					# task_finished = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[6]/div[3]/button[2]') Nao funciona

					# task_finished = self.driver.find_element(By.XPATH,'//html[1]/body[1]/div[6]/div[3]/button[2]') Nao funciona

					# task_finished = self.driver.find_element(By.XPATH,'//html[1]//body[1]//div[6]//div[3]//button[2]') Nao funciona




		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

main = Main()

main.Login()