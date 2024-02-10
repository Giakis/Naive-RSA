def Fast_Exponentiation(b , e , m):
    B = b #Base
    result = 1
    M = m #Μodulo
    E = e #exponent
    while (E > 0):
        if ((E % 2) == 1):
            result =(result * B) % M
        E = (E // 2) #Η πράξη // εκτελεί και επιστρέφει ακέραιο αποτέλεσμα ενώ η / δεκαδικό.
        B = (B ** 2) % M
    return result


N = 899
e = 839
s = 301
m = 3

#Αφού είναι naive RSA δεν θα χρησιμοποιήσω Hash
result = Fast_Exponentiation(s,e,N)
print(result)
if (result == m):
    print('Ειναι σωστη η ψηφιακη υπογραφη')
else:
    print('Δεν ειναι σωστη η ψηφιακη υπογραφη για το m:',m)
