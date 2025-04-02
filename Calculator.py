import customtkinter as ctk

def calcular_imc(weight, size):
    """Função para calcular o IMC"""
    return weight / (size * size)

def determinar_categoria(imc):
    """Função para determinar a categoria e a cor correspondente ao IMC"""
    if imc < 17:
        return 'Very underweight', '#FFFE01'
    elif 17 <= imc < 18.5:
        return 'Underweight', '#D8FF6D'
    elif 18.5 <= imc < 25:
        return 'Normal weight', '#20FF00'
    elif 25 <= imc < 30:
        return 'Overweight', '#FFAA00'
    elif 30 <= imc < 35:
        return 'Obesity I', '#FF7B02'
    elif 35 <= imc < 40:
        return 'Obesity II(severe)', '#FF4B00'
    else:
        return 'Obesity III (morbid)', '#FF0B00'

def atualizar_campos(imc, categoria, textcolor, campo_resultado, campo_categoria):
    """Função para atualizar os campos de resultado e categoria"""
    campo_resultado.configure(state="normal")  # Permite editar o campo
    campo_resultado.delete(0, ctk.END)  # Limpa o campo de resultado
    campo_resultado.insert(0, f'{imc:.2f}')  # Insere o valor do IMC no campo
    
    campo_categoria.configure(state="normal")  # Permite editar o campo
    campo_categoria.delete(0, ctk.END)  # Limpa o campo de categoria
    campo_categoria.insert(0, categoria)  # Insere a categoria no campo
    
    # Alterando a cor do texto da categoria
    campo_categoria.configure(text_color=textcolor)  # Aplica a cor ao texto da categoria
    
    campo_resultado.configure(state="disabled")  # Desabilita o campo após inserir o valor
    campo_categoria.configure(state="disabled")  # Desabilita o campo após inserir o valor

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400')
        self.root.minsize(350, 350)
        self.root.configure(padx=20, pady=20, bg_color='#6438FF')  # Fundo roxo para a janela
        self.root.title('Calculator BMI')

        # Fontes
        self.fonte_texto_principal = ctk.CTkFont('Arial', 18, 'bold')
        self.fonte_padrao = ctk.CTkFont('Arial', 14, 'bold')

        # Componentes da interface
        self.criar_widgets()

    def criar_widgets(self):
        """Função para criar os widgets"""
        texto_principal = ctk.CTkLabel(self.root, text='Better Health', font=self.fonte_texto_principal, text_color='#FFF91F')
        texto_principal.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        texto_principal_sub = ctk.CTkLabel(self.root, text='Calculate your BMI and Make Better Decisions ', font=self.fonte_padrao)
        texto_principal_sub.grid(row=1, column=0, columnspan=2, pady=(15))

        # Entrada de peso
        self.textinsideblock = self.criar_entrada('Type your weight:', 'WEIGHT', 2)
        
        # Entrada de altura
        self.textinsideblock_two = self.criar_entrada('Type your size:', 'SIZE', 3)
        
        # Botão para calcular o IMC
        botao_calcular = ctk.CTkButton(self.root, text="Get result", command=self.calculatedata, font=self.fonte_padrao, corner_radius=20, text_color='#FFF9BF', fg_color='#6438FF')
        botao_calcular.grid(row=4, column=0, columnspan=2, pady=15)

        # Labels e campos para exibir o resultado
        self.campo_resultado = self.criar_entrada('Result: ', 'IMC', 5, disabled=True)
        self.campo_categoria = self.criar_entrada('Category: ', 'Category', 6, disabled=True)

    def criar_entrada(self, label_text, placeholder_text, row, disabled=False):
        """Função auxiliar para criar campos de entrada"""
        label = ctk.CTkLabel(self.root, text=label_text, font=self.fonte_padrao)
        label.grid(row=row, column=0, pady=5, sticky="w", padx=20)

        entry = ctk.CTkEntry(self.root, placeholder_text=placeholder_text, corner_radius=10)
        entry.grid(row=row, column=1, pady=5, padx=20)
        if disabled:
            entry.configure(state="disabled")  # Deixa o campo desabilitado

        return entry

    def calculatedata(self):
        """Função chamada quando o botão for pressionado"""
        try:
            weight = float(self.textinsideblock.get())
            size = float(self.textinsideblock_two.get())
        except ValueError:
            return  # Se os valores não forem numéricos, não faz nada

        # Calculando o IMC
        imc = calcular_imc(weight, size)
        print(f'Com base nos seus dados o seu IMC é: {imc:.2f}')
        
        # Determinando a categoria e cor correspondente
        categoria, textcolor = determinar_categoria(imc)
        
        # Atualizando os campos de resultado e categoria
        atualizar_campos(imc, categoria, textcolor, self.campo_resultado, self.campo_categoria)

# Iniciando a interface
if __name__ == "__main__":
    ctk.set_default_color_theme('blue')
    ctk.set_appearance_mode('dark')
    
    janela = ctk.CTk()
    app = BMICalculatorApp(janela)
    janela.mainloop()