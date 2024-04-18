# Introdução à Python
## Slide 2
### Legibilidade: Facilidade do programa ser lido e compreendido
- Foco de legibilidade para humanos
  - Python é uma linguagem de alto nível, ou seja, há uma maior facilidade de escrita, manutenção e abstração para o programador
- Sobrecarga de operador é permitida em Python
  - Entretanto é de necessidade e uso completamente controlada pelo programador
- Multiplicidade de recursos é relativamente baixa em Python
  - Devido meu atual foco de estudo essa comparação é feita quando comparada a C, Go e Java
- Considerações de sintaxe
  - Nomenclatura de identificadores é flexível (mais informações em [Forma](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/main/Diario_de_bordo.md#forma))
- Ortogonalidade
  - Em Python não há o uso de ponteiros, de modo que, todo o gerenciamento de memória e mapeamento é feito pelo compilador

### Regibilidade: Facilidade para criar um programa para um domínio de problema conhecido
- A construção primitiva de uma varíavel em python não precisa ser especificada pelo programador
  - Uma mesma variável pode, em diferentes instantes, ser de diferentes tipos
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/1.Demonstracao_Variavel.py) e o [resultado no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/1.Demonstracao_Variavel_saida_terminal.png)
- Suporte à abstração
  - Visto que Python é imperativa e orientada a objetos, ela permite:
    - Criação de classes, e seus construtores, e objetos 
    - Encapsulamento, herança e polimorfismo
    - Uso de módulos e pacotes
 
### Confiabilidade: Se o programa se comporta de acordo com suas especificações em todos os casos
- Erros de tipos
  - Podem ser verificados através de verificações entre type() e o tipo desejado
  - Isso permite evitar erros como tentar multiplicar uma string com uma int
- Tratamento de erros
  - Em Python a interceptação de erros é feita através de "try:" e "except PossivelErro"
- [Exemplo de tratamento de erro de tipo](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/1.Casos_de_erro.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/1.Casos_de_erro_saida_terminal.png) com os teste usados

### Custo e Outros
- Python é interpretada: Mais lenta do que linguagens compiladas
- Há disponibilidade de interpretadores gratuitos de Python
- Python pode ser usada em qualquer plataforma que tenha um interpretador para ela
- É bem definida no [documento oficial](https://docs.python.org/3/genindex-all.html)
- É flexível o bastante para ser usada em diversas aplicações, já que, assim como descrito, é imperativa e orientada a objetos

## Slide 3
### Categoria
- Python é uma linguagem imperativa
  - Também oferece suporte a programação orientada a objetos
    - Permitindo a criação de classes e contrutores para elasa
  - Também sendo uma linguagem de script
    - Permitindo a execução de algoritmos criados pelo programador

### Interpretação pura
- Implementação usual de Python
- Erros são facilmente mostrados
- Como desvantagem, possui maior custo de memória e tempo de execução

### Observação
- Similarmente a Java, códigos em Python passam por uma passo de compilação
- Entretanto, diferente de Java, essa compilação é um passo automático
- Além disso, não há uma forma intermediária, como o bytecode de Java, em Python disponível para uso

### Programação estruturada (pelo programador)
- Permite divisão em funções
- Uso de estruturas de dados simples como tuplas e dicionários (mais informações em [Tipos](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/main/Diario_de_bordo.md#tipos))
- Uso de comentários (Em linhas através de #Comentario e em partes através de ''' código ''')

### Orientada a objetos
- Python é uma linguagem orientada a objetos, permitindo:
  - A criação de classes, construtores e objetos para dada classe
  - Encapsulamento, herança e polimorfismo

### Concorrente
- Threads
  - Através do módulo threading
  - Muito usada para operações de entrada e saída intensivas
- Programação assíncrona
  - Através mo módulo asyncio
  - Muito usada para operações de entrada e saída assíncronas

### Programação paralela
- Módulo multiprocessing
  - Permite o programador a fazer uso de múltiplos núcleos de CPU
 
# Variáveis
## Slide 6
### Forma: 
- [a-zA-Z_][a-zA-z0-9_]*
  - O limite do tamanho da variável é determinado pela quantidade de memória disponível
- Não permite espaço no nome
- Case sensitive
- Não é necessário definir o tipo de variável anteriormente

### Tipos:
- Inteiro (int)
- Ponto flutuante (float)
- String (str)
- Booleano (bool)
- Complexa (complex) 
  - Para números complexos (Parte real e parte imaginária)
- Lista (list) 
  - Vetores
- Tupla (tuple)
  - Um vetor imutável
- Dicionário (dict)
  - Um vetor de chaves e valores
    - Permitindo vetores de diferentes tipos como: 
    - { 'nome': 'Nome 1', ..., 'idade': 21}
- [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/2.Exemplo_tipos_variaveis.py#L6) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/2.Exemplo_tipos_variaveis_saida_terminal.png)

### Palavras especiais
- São todas reservadas em Python
  - [Lista de palavras especiais em Python](https://pythoniluminado.netlify.app/sintaxe)
- Caracteres como '{', '}', '&', '^', etc também tem uso especial em Python
- Possui, no total, menos de 50 palavras reservadas
- Podem ser visualizadas com uso do módulo keyword
  - Nesse caso o comando 'print(keyword.kwlist)' imprimirá todas elas no terminal

### Na implementação da linguagem
- import 'x'
  - Faz a importação do módulo 'x'
- Amarração de tipo dinâmico para variáveis

## Slide 7
### Variável estática
- Variaveis globais em Python são declaradas fora de funções ou com o uso do prefixo 'global' quando dentro de uma função

### Variável de pilha
- Variáveis locais de funções

### Variável explícita de heap
- Não há como declarar variáveis explícita de heap em python

### Variável implícita de heap
- Variáveis do tipo:
  - list
  - tuple
  - dict
  
### Variáveis locais
- Variáveis criadas em funções

### Variáveis não-locais
- Escopo estático
  - Variáveis globais
- Escopo dinâmico
  - Em funções aninhadas:
    - Uso do prefixo nonlocal permitirá alterar o valor da função pai mais próxima

### Ambiente de referenciação
- Estático
  - Variáveis locais e globais
- Dinâmico
  - Variáveis locais e da função pai mais próxima através do prefixo nonlocal

### Constantes
- Não há uma maneira direta (como 'const' ou 'final') de declarar constantes 
- Portanto, a definição de constates é feita através de uma tupla unitária
  - Valor dessa variável pode ser estática ou dinâmica, de acordo com o desejo do programador

# Tipo de dados
## Slide 8
### Tipos primitivos
- Inteiro (int)
- String (str)
- Ponto flutuante (float)
- Booleano (bool)
- Complexo (complex) 

### Tipos estruturados
- Lista (list) 
- Tupla (tuple)
- Dicionário (dict)

### Informações gerais
- Tamanho estático

### Copiando uma string
- Através de str()
- Através de splicing sem condições [:]

### Comparando string
- Através de ==
- Através de 'is' (Compara local da memória)

### Informações gerais
- Referência a arrays através de []
- Índice tem que ser do tipo int
  - Pode ser negativo, fazendo uma leitura em ordem inversa

### Array estático
- Apenas trupla
  - Devido sua natureza estática

### Array Pilha-Dinâmico Fixo
- Não existe em Python

### Array Pilha-Dinâmico
- Não existe em Python

### Array Heap-Dinâmico Fixo
- Não existe em Python

### Array Heap-Dinâmico
- Variáveis do tipo list e dict
- Vetores de objetos de classes

### Inicialização de Arrays
- Ou o array é vazio ou valores e posições são alocados diretamente
- Com excessão do Array vazio, não é possível gerar posições com valores vazios sem módulos

### Array multidimensional
- Através do aninhamento de tipos estruturados
- Armazenado na ordem linha

### Array associativo
- Dicionários (dict)
- Acessado por chave (String)
- Pode ser aninhado
- [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/3.Exemplo_Dicionario_aninhado.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/3.Exemplo_Dicionario_aninhado_saida_terminal.png)

## Slide 9
### Registro
- Python permite a construção de classes ou uso de dicionárioss
- Referenciação
  - Usa-se a notação de ponto, começando com a extrutura mais externa até a atual
- Operações
  - Classes de objetos podem ser comparadas através de type()
  - Métodos e/ou atributos podem ser comparados entre classes
- Implementação
  - Campos são armazanados em localizações adjacentes
  - Nãao é possível usar aritmética de ponteiros
- Array vs registros
  - Enquanto dicionários arrays poderiam funcionar de maneira similar à, por exemplo, struct em C, qualquer outro dicionário, mesmo que de mesmo atributoss, devem ser feitos do 0
  - O uso de classes, programação orientada a objetos, permite o uso de polimorfismo e herança
 
### Union
- Não há algum tipo equivalente a union em python
- Entretanto, union é utilizado para o armazenamento de valores das variáveis do programa

### Ponteiro
- Não permite a manipulação direta de memória alocada
- Atribuição
  - Funciona através do uso de igual (=) entre o ponteiro criado e a variável desejada
    - Esse funcionamento é feito através de referências a objetos
- Operações
  - Uso direto do ponteiro como variável, já que não há possibilidade da manipulação de memória
- Problemas
  - Dangling Reference
    - Não ocorre, pois a liberação de memória é feita pelo interpretador
    - Desse modo, esse erro é apenas possível se o programador alterar a variável para qual o ponteiro aponta e esquecer essa mudança
- Tipo referência
  - Tem o mesmo funcionamento de outros tipos em Python

### Verificação de tipo
- Verificação dinâmica
- Tipagem forte
  - Também permite cast explícito
- Equivalência de tipos
  - Pode ser verificado com uma comparação com type()
  - As estruturas, quando equivalentes, podem ser usadas como estruturas iguais

# Atribuição e estruturas de controle
## Slide 10
### Precedência de operadores
- Ordem de precedência em Python (Ordem decrescente)
  - '++' (Potência)
  - '*' (Multiplicação), '/' (Divisão) e '//' (Divisão inteira, não considera o resto)
  - '+' (Adição) e '-' (Subtração)
  - '<', '==', '!=' , '>', '<=' ou '>=' (Comparação)
  - not
  - and
  - or
  
### Associatividade de operadores
- No geral, associatividade pela esquerda
- Excessão:
  - Potência é pela direita

### Parênteses
- Não é de uso obrigatório
- Permite o aumento de precedência de certas operações em uma fórmula

### Expressões condicionais
- if(): e else:
  - As expressões deverão ter uma indentação maior do que o if(): 
- Não há o uso de then após o if():
- o else: será relacionado ao if(): mais próximo de mesma indentação

### Ordem de avaliação de operandos
- Efeito colateral
  - Em Python, uma função que retorna o valor diretamente na operação não altera o valor da variável em si diretamente
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/4.Ordem_de_operandos.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_1-LPP-2024.1/blob/Codigos_e_exemplos/4.Ordem_de_operandos_saida_terminal.png)
  
### Sobrecarga de operadores
- '+' é usado para soma e concatenação de strings
- '*' é usado para a multiplicação e replicação de strings
- '==' e '!=' pode verificar igualdade entre números e estrutural (tipos, classes, etc)

### Conversões de tipo
- Conversão implícita será feita quando válido
  - Modo misto
    - Permitido em casos específicos:
      - multiplicação entre int e string
      - multiplicação entre int e float
      - etc
- Conversão explícita pode ser usada através do prefixo do nome do tipo desejado entre aspas

### Expressões racionais 

### Atribuição

## Slide 11
### Introdução

### Sentenças de seleção

### Seleção múltipla

### Sentença interativa

### Loops controlados por contadores

### Loops controlados logicamente

### Controle definido por usuário

### Iteração baseada em estrutura de dados
