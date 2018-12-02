import textwrap

def wrap_lines(text, number, justify):
    try:
        number = int(number)
        if number <= 0: # Testa se o input number não é menor que zero
            raise ValueError 
        if text == " " or not isinstance(text, str): # Testa se o input text está vazio ou não é possível ser convertido para string
            raise ValueError
    except ValueError:
        return "Value error!"

    final_text = ""

    lines = textwrap.fill(text, number) # Gera uma lista de strings quebradas com limite de caracteres
    if justify == True:
        list_of_lines = lines.split('\n')
        for line_index, line in enumerate(list_of_lines):
            new_line = []        # Foi utilizada uma lista para armazenar a string pois variáveis do tipo string em python são imutáveis e o valor era resetado depois de cada iteração, porém, listas não são imutáveis
            new_line.append(line)

            if len(line) < number:
                count_of_chars = len(line) # Total de caracteres na linha
                count = 0 # Contador de caracteres
                blank_spaces = [c for c in line if c == " "]
                number_of_blank_spaces = len(blank_spaces) # Contador de caracteres em branco

                if number_of_blank_spaces == 0: # Se a linha tiver o tamanho exato do input number o processo é interrompido e o próximo loop é iniciado
                    while len(new_line[0]) < number:
                        temp_line = new_line[0]
                        new_line[0] = temp_line + " "

                last_blank_space = 0 # Último espaço em branco
                blank_space_count = 0 # Contador de espaços em branco
                    
                while len(new_line[0]) < number:
                    for index, c in enumerate(new_line[0]):
                        if new_line[0][index] == " " and new_line[0][index + 1] is not " ": # Esta linha é para garantir que uma sequência de espaços em branco seja considerado apenas um espaço
                            blank_space_count += 1
                            if blank_space_count > last_blank_space:

                                new_line[0] = new_line[0][:index] + " " + new_line[0][index:] # É adicionado um espaço em branco
                                    
                                last_blank_space = blank_space_count
                                blank_space_count = 0

                                if last_blank_space == number_of_blank_spaces: # Se o último espaço executado for o último da string o registro é zerado e o loop é reiniciado
                                    last_blank_space = 0
                                break
            else:
                new_line[0] = line
                
            final_text += new_line[0] + "\n"

    else:
        final_text = lines    
                                                 
    return final_text