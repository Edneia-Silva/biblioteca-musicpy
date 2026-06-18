## 🎵 MusicPy – Criando Música com Python

## Sobre o Projeto
Este projeto foi desenvolvido como atividade acadêmica para estudo da biblioteca MusicPy, uma ferramenta Python voltada para criação, manipulação e automação de elementos musicais.

O objetivo foi explorar uma aplicação criativa da programação, demonstrando como notas musicais podem ser transformadas em código e posteriormente em arquivos MIDI reproduzíveis.

O projeto apresenta um gerador automático de melodias, capaz de criar sequências musicais utilizando conceitos básicos de teoria musical e programação.

---

## O que é a MusicPy?
A MusicPy é uma biblioteca Python desenvolvida para representar conceitos musicais diretamente no código.

Com ela é possível trabalhar com:
* Notas musicais
* Acordes
* Escalas
* Melodias
* Arquivos MIDI
* Composição algorítmica

A biblioteca oferece uma forma intuitiva de unir programação e música, permitindo que estruturas musicais sejam criadas e manipuladas através de Python.

---

## Tecnologias Utilizadas
* Python 3
* MusicPy
* Random (biblioteca padrão do Python)
* OS (biblioteca padrão do Python)

---

## Objetivo do Projeto
Demonstrar como a MusicPy pode ser utilizada para:
1.	Representar elementos musicais em código.
2.	Gerar melodias automaticamente.
3.	Exportar composições para o formato MIDI.
4.	Explorar a relação entre lógica computacional e criação musical.

---

## Miniprojeto: Gerador de Melodias
O projeto gera uma sequência de notas aleatórias utilizando a escala de Dó Maior.

A sequência é transformada em uma melodia pela MusicPy e exportada para um arquivo MIDI que pode ser reproduzido em qualquer software compatível.

# Exemplo Utilizado (Código)
from musicpy import *
import random
import os

notas = ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']

sequencia = ','.join(
    random.choice(notas)
    for _ in range(20)
)

melodia = chord(sequencia)

melodia.interval = [0.25] * 20

write(melodia, name='musica.mid')

os.startfile('musica.mid')

---

## Como Funciona
1. Definição da Escala
notas = ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
As notas pertencem à escala de Dó Maior, escolhida por sua simplicidade e sonoridade agradável.

2. Geração Aleatória
random.choice(notas)
Seleciona notas aleatórias para compor a melodia.

3. Criação da Estrutura Musical
melodia = chord(sequencia)
Transforma a sequência de notas em um objeto musical da MusicPy.

4. Exportação para MIDI
write(melodia, name='musica.mid')
Gera um arquivo MIDI contendo a melodia criada.

5. Reprodução
os.startfile('musica.mid')
Abre automaticamente o arquivo gerado.

---

## Aplicações da MusicPy
A MusicPy pode ser utilizada em diversas áreas:
* Educação musical
* Ferramentas de composição
* Automação de processos musicais
* Jogos digitais
* Computação musical
* Inteligência Artificial aplicada à música
* Sistemas de geração procedural de conteúdo

---

## Estrutura do Projeto
biblioteca-musicpy/
│
├── melodia.py
├── musica.mid
├── README.md
└── requirements.txt

---

## Instalação
Clone o repositório:
git clone https://github.com/Edneia-Silva/biblioteca-musicpy

Acesse a pasta:
cd biblioteca-musicpy

Instale a biblioteca:
pip install musicpy

Execute o projeto:
python melodia.py

---

## Considerações Finais
A MusicPy demonstra que a programação também pode ser utilizada como ferramenta de expressão artística. Através dela, conceitos musicais podem ser representados, manipulados e automatizados de forma simples, aproximando duas áreas aparentemente distintas: música e computação.

---

## Autora
Edneia Silva

Projeto acadêmico desenvolvido para apresentação da 
biblioteca MusicPy na disciplina de Linguagem de Programação II do curso de Integligência Artifical (IA) da Fatec Rio Claro.
