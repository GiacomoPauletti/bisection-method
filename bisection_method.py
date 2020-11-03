from math import ceil, floor, e, log
import numpy as np

def bisection(f, intervallo, precisione=0.01, **kwargs):
    """
    funzione di bisezione che serve a trovare il valore approssimato dello zero di una funzione in un dato 
    intervallo.

    PARAMETRI:
        f: funzione che rappresenta una funzione matematica, quindi che abbina ad un input x un output y
        intervallo: l'intervallo in cui cercare l'intersezione. Perchè il metodo funzioni gli estremi devono esser
                    discordi
        precisione: fino a che cifra (decimale o no) deve approssimare     
    """
    precisione = precisione*0.1
    #estremi dell'intervallo
    a = float(intervallo[0])
    b = float(intervallo[1])

    #----------------------------------------------------------------------------------
    #1)controllando la precisione
    a_digits = [*str(a)]  #--> ["-", "0",".","9","9"]
    b_digits = [*str(b)]

    if a_digits[0] == '-':
        a_digits.remove('-')
    if b_digits[0] == '-':
        b_digits.remove('-')



    #controllo cifra per cifra
    #variabili usate per calcolare la precisione attuale (ovvero fino a che cifra i 2 estremi sono uguali)
    #precisione = ints/10^exp
    exp = 0
    ints = 10**(a_digits.index('.')-1)		#questa variabile è 10 elevato per il numero di cifre prima della 
                                            #virgola. Serve dopo per calcolare la precisione

    #i seguenti 2 valori sono l'index a cui il punto . è posizionato e che equivale al numero di cifre prima della
    #virgola
    index_a = a_digits.index('.')
    index_b = b_digits.index('.') 

    #se i due numeri non hanno lo stesso numero di cifre allora non si calcolerà la precisione
    if index_a - index_b!= 0:
        if index_a > index_b:
            ints = 10**(index_b-1)
        else:
            ints = 10**(index_a-1)
        
    else:
        t = len(a_digits) if len(a_digits) <= len(b_digits) else len(b_digits)
        for i in range(t):
            if a_digits[i] == '.':
                continue

                
            elif a_digits[i] == b_digits[i]:
                exp += 1
                continue
            else:
                break

        #calcolo precisione e nel caso sia corrispondente a quella data, ritorna il risultato
        prec = ints / (10**exp)
        if (prec <= precisione):
            a = ceil(a * 1/precisione) * precisione
            b = floor(a * 1/precisione) * precisione
            return (a + b)/2
    #------------------------------------------------------------------------------------

    #2)calcolo dell'insieme giusto
    punto_medio = (a + b)/2
    #print(punto_medio)

    #se sono discordi, ovvero c'è un intersezione in quell'intervallo
    if f(a, **kwargs) * f(punto_medio, **kwargs) < 0.0:

        return bisezione(f=f, precisione=precisione, intervallo=[a, punto_medio], **kwargs)

    elif f(a, **kwargs) * f(punto_medio, **kwargs) == 0.0:
        if f(a, **kwargs) == 0.0:
            return a
        else:
            return punto_medio

    #altrimenti controllo con l'altro caso
    elif f(punto_medio, **kwargs) * f(b, **kwargs) < 0.0:
        return bisezione(f=f, precisione=precisione, intervallo=[punto_medio, b], **kwargs)

    #se fa 0 allora vuol dire che funzione(b) fa 0 (non l'altro se no sarebbe andato nel 2 caso)
    elif f(punto_medio, **kwargs) * f(b, **kwargs) == 0.0:
        return b

    #se nessuno dei due sottointervalli ha le condizioni necessarie per il teorema degli zeri e nemmeno gli estremi
    #e il punto medio sono le soluzioni
    else:
        print("Nell'intervallo passato non ci sono intersezioni oppure l'algoritmo non è in grado di trovarne alcuna")
        a = ceil(a * 1/precisione) * precisione
        b = floor(a * 1/precisione) * precisione
        return None
