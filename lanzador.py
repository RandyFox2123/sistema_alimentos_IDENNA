import os
import sys
import subprocess
import socket
import time
import webbrowser

def check_server_running(host='127.0.0.1', port=8090):
    """Chequea si el servidor Django está activo en host:port"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            return True
        except:
            return False

def create_venv_if_not_exists(venv_path):
    """Crea entorno virtual si no existe"""
    if not os.path.exists(venv_path):
        print("No se encontró entorno virtual. Creando venv...")
        subprocess.check_call([sys.executable, '-m', 'venv', venv_path])
        return True  # Indica que se creó
    return False

def install_requirements(python_exec, requirements_path):
    """Instala dependencias si requirements.txt existe"""
    if os.path.exists(requirements_path):
        print("Instalando dependencias desde requirements.txt...")
        subprocess.check_call([python_exec, '-m', 'pip', 'install', '-r', requirements_path])

def get_python_path(venv_path):
    """Devuelve el path al ejecutable python dentro del venv según sistema"""
    if os.name == 'nt':  # Windows
        return os.path.join(venv_path, 'Scripts', 'python.exe')
    else:  # macOS / Linux
        return os.path.join(venv_path, 'bin', 'python')

def launch_django_server(python_exec, manage_path):
    """Lanza servidor Django en segundo plano sin consola visible"""
    cmd = [python_exec, manage_path, 'runserver']

    if os.name == 'nt':
        # No consola visible en Windows
        subprocess.Popen(cmd,
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         shell=False,
                         creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        # En Unix/Mac, ejecuta en segundo plano
        subprocess.Popen(cmd,
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         shell=False,
                         preexec_fn=os.setsid)

def main():
    # Directorio donde está el script (se asume raíz del proyecto)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    venv_path = os.path.join(base_dir, 'venv')
    requirements_path = os.path.join(base_dir, 'requirements.txt')
    manage_py = os.path.join(base_dir, 'manage.py')

    # Comprobar o crear entorno virtual
    venv_created = create_venv_if_not_exists(venv_path)

    python_exec = get_python_path(venv_path)

    # Si recién creó el entorno virtual, instala dependencias
    if venv_created:
        install_requirements(python_exec, requirements_path)

    # Chequear si servidor está corriendo
    if check_server_running():
        print("Servidor Django ya está corriendo. Abriendo navegador...")
        webbrowser.open('http://127.0.0.1:8090/')
        return

    # Lanzar servidor
    print("Servidor Django no está activo. Lanzando servidor...")
    launch_django_server(python_exec, manage_py)

    # Espera un poco para que el servidor se inicie
    time.sleep(3)

    # Abrir navegador en la vista index
    webbrowser.open('http://127.0.0.1:8090/')

if __name__ == '__main__':
    main()
