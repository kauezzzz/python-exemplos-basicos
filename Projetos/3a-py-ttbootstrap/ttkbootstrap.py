import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import sys
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Obtém o caminho absoluto para o recurso, funciona para dev e para o PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class FormularioInscricao:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulário de Inscrição")
        self.master.geometry("500x550")
        
        # Configurando o ícone da janela
        self.set_icon()
        
        # Lista de temas disponíveis no ttkbootstrap
        # (https://ttkbootstrap.readthedocs.io/en/latest/themes)
        self.temas = ["darkly", "flatly", "litera", "minty", "lumen", "sandstone", "yeti", "pulse", 
                      "united", "morph", "journal", "darkly", "superhero", "solar", "cyborg", "vapor"]
        
        # Configuração do estilo inicial
        self.style = ttk.Style("darkly")
        
        # Criação do frame principal
        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack(fill=BOTH, expand=YES)
        
        # Título
        ttk.Label(self.frame, text="Formulário de Inscrição", font=("TkDefaultFont", 16, "bold")).pack(pady=10)
        
        # Campo Nome
        ttk.Label(self.frame, text="Nome").pack(anchor=W, pady=(10, 0))
        self.nome_entry = ttk.Entry(self.frame, width=50)
        self.nome_entry.pack(fill=X)
        
       
        
 
        
        # ComboBox para seleção de temas
        self.tema_var = ttk.StringVar()
        self.tema_combo = ttk.Combobox(self.opcoes_frame, textvariable=self.tema_var, values=self.temas, 
        state="readonly", width=15)
        self.tema_combo.set("darkly")  # Tema inicial
        self.tema_combo.pack(side=RIGHT)
        self.tema_combo.bind("<<ComboboxSelected>>", self.mudar_tema)
        
        # Frame para os botões
        self.botoes_frame = ttk.Frame(self.frame)
        self.botoes_frame.pack(pady=20, fill=X)
        
        # Botão Enviar
        self.enviar_btn = ttk.Button(self.botoes_frame, text="Enviar", bootstyle="success", command=self.enviar)
        self.enviar_btn.pack(side=LEFT, expand=True)
        

        
        # Frame para exibir os dados coletados
        self.dados_frame = ttk.Frame(self.frame)
        self.dados_frame.pack(pady=10, fill=X)
        
        # Labels para exibir os dados coletados
        self.nome_label = ttk.Label(self.dados_frame, text="", anchor=CENTER)
        self.nome_label.pack(fill=X)
        


    def set_icon(self):
        icon_ico = resource_path("logo.ico")
        icon_png = resource_path("logo.png")
        
        if os.path.exists(icon_ico):
            self.master.iconbitmap(icon_ico)
        elif os.path.exists(icon_png):
            logo = Image.open(icon_png)
            logo = ImageTk.PhotoImage(logo)
            self.master.iconphoto(True, logo)
        else:
            print("Arquivo de ícone não encontrado.")
    


if __name__ == "__main__":
    root = ttk.Window()
    app = FormularioInscricao(root)
    root.mainloop()