# 1.find_max
# 2.sum_of.list
# 3.n!
# 4.cFibonacci
# 5.dodatkowe sudoku 4 lub 9

def find_max(arr):
    if len(arr) == 1: #jeśli długośc listy to 1...
        return arr[0] #... to zwracamy pierwszy (jedyny) element listy
    else:
        max_value = find_max(arr[1:]) # w przeciwnym razie działamy na podzbiorze
        return arr[0] if arr[0] > max_value else max_value # zwracamy pierwszy element jeśli jest on większy od drugiego, w przeciwnym razie zwracamy drugi
    
array = [4, 9, 2, 6, 1, 8, 54, 7]
max_value = find_max(array)
print("Maximum value:", max_value)

