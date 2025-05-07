import numpy as np
import locale

locale.setlocale(category=locale.LC_ALL, locale="pt_BR.Utf8")

arr = np.array([],dtype=float)
arr2 = np.array([], dtype=float)

def media():
    global arr, arr2
    valores = [9.25,9.51,9.48]
    valores2 = [111,10,100]
    
    arr = np.append(arr, [float(x) for x in valores])
    arr2 = np.append(arr2, [float(x) for x in valores2])
    total = np.multiply(arr,arr2)
    preco_medio = np.divide(total,np.sum(arr2))

    print("="*80)
    print(f"Quantidade: {np.sum(arr2, dtype=int)}")
    print(f"Valor Total: {locale.currency(np.sum(total),grouping=True, symbol=True)}")
    print(f"Preço Médio: {locale.currency(np.sum(preco_medio), grouping=True, symbol=True)}")

media()