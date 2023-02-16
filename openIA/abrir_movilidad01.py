from pywinauto import Application

# Conectar con la aplicación Chrome
app = Application().connect(title_re=".*Chrome.*")

# Obtener el control de la ventana principal del navegador
window = app.top_window()

# Ingresar la URL del sitio web
address_bar = window.child_window(auto_id="address and search bar", control_type="Edit")
address_bar.set_text("https://movilidad.bioalimentar.com")

# Enviar Enter para cargar la página web
address_bar.type_keys("{ENTER}")

# Esperar a que la página web cargue
window.wait("ready")

# Obtener el control de los campos de usuario y contraseña
username_box = window.child_window(title="usuario", control_type="Edit")
password_box = window.child_window(title="password", control_type="Edit")

# Ingresar el nombre de usuario y la contraseña
username_box.set_text("GABRIELS")
password_box.set_text("Gab$1984")

# Enviar clic en el botón de inicio de sesión
login_button = window.child_window(title="Login", control_type="Button")
login_button.click()
