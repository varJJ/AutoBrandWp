from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configura las opciones de Brave
options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Cambia la ruta si es necesario

# Configura el WebDriver para Brave
service = Service(executable_path='C:/chrome-driver/chromedriver.exe')  # Cambia la ruta al chromedriver
driver = webdriver.Chrome(service=service, options=options)

# Abre la página de login de tu WordPress
driver.get('https://tusitio.com/wp-login.php')

# Espera a que la página cargue
time.sleep(2)

# Encuentra el campo de usuario e ingresa tu nombre de usuario
username_field = driver.find_element(By.ID, 'user_login')
username_field.send_keys('tu_usuario')

# Encuentra el campo de contraseña e ingresa tu contraseña
password_field = driver.find_element(By.ID, 'user_pass')
password_field.send_keys('tu_contraseña')

# Encuentra el botón de login y haz clic en él
login_button = driver.find_element(By.ID, 'wp-submit')
login_button.click()

# Espera un poco para que el login se complete
time.sleep(3)

# Navega a la sección de agregar marca
driver.get('https://tusitio.com/wp-admin/post-new.php?post_type=brand')

# Encuentra el campo para el nombre de la marca y agrega el nombre
brand_name_field = driver.find_element(By.NAME, 'post_title')
brand_name_field.send_keys('Nueva Marca')

# Encuentra el botón para publicar la marca y haz clic
publish_button = driver.find_element(By.ID, 'publish')
publish_button.click()

# Espera un poco para que el proceso se complete
time.sleep(3)

# Cierra el navegador
driver.quit()
