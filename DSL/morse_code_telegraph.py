# just a quick demo of the morse code telegraph        #
# this does not relate to my project in any way        #
# it is just a first try handeling DSL language models #


from textx import metamodel_from_file
import pandas as pd
import string


morse_meta = metamodel_from_file("morse.tx", debug=True)

morse_code_text = morse_meta.model_from_file("telegraph.morse")

latin_alphabet = list(string.ascii_lowercase)

morse_code=['.-', '-...', '-.-.', '-..' , '.' , \
            '..-.' , '--.' , '....' , '..' , '.---' ,\
            '-.-' , '.-..' , '--' , '-.' , '---' , '.--.' ,\
            '--.-' , '.-.' , '...' , '-' , '..-' , '...-' , \
            '.--' , '-..-' , '-.--' , '--..']

translation_df = pd.DataFrame(list(zip(latin_alphabet, morse_code)),
               columns =['Latin', 'Morse'])

translation=[]
def translate(morse_code_text):
    for sents in morse_code_text.translate_instructions:
        for words in sents.sentence.word:
            letter_list=str(*words.morse).split('+')
            for a_letter in letter_list:
                df_row_idx=translation_df.index[translation_df['Morse']==a_letter]
                idx=df_row_idx.tolist()[0]
                translation.append(translation_df.at[idx, 'Latin'])
            translation.append(' ')

translate(morse_code_text)

print("translation: ", translation)