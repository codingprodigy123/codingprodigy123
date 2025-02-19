import tkinter as tk
from langchain_ollama import OllamaLLM

model = OllamaLLM(model='mistral')
window = tk.Tk()
window.geometry('500x500')
window.title('pi ai') 

def make_responce():
    x = input_field.get()
    y = model.invoke(x)
    output_field.insert(tk.END, f'ai: {y}\n')

input_field = tk.Entry(window, width=30)
input_field.pack(pady=20)

generate_button = tk.Button(window, text='Generate', command=make_responce)
generate_button.pack(pady=10)

output_field = tk.Text(window, height=10, width=50)
output_field.pack(pady=20)

window.mainloop()
while True:
    pass
    x = input('me:')
    y = model.invoke(x)
    print(f'ai:{y}')
