import dict_starterdictionary
import os


def mprogram():
    prompt = input("Tú: ")


    if prompt in dict_starterdictionary.frases:
        if dict_starterdictionary.frases[prompt]["type"] == "ans":
            backprompt = dict_starterdictionary.frases[prompt]["text"]
        elif dict_starterdictionary.frases[prompt]["type"] == "command":
            backprompt = dict_starterdictionary.frases[prompt]["text"]()
        else:
            print("No lo he entendido. Por favor, repitelo.")
            return True

        print("Xeon:",backprompt,)
        return True

    elif prompt in dict_starterdictionary.exitc:
        backprompt = dict_starterdictionary.exitc[prompt]
        print("Xeon:",backprompt,)
        return False

    else:
        print("Xeon: ","No te he entendido.",)

ex = True
while ex:
    ex = mprogram()
