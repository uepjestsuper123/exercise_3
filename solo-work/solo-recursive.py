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

def sum_of_list(lst):
    sum_of_numbers = lst[0] #jako sumę ustalamy wartość pierwszego elementu
    lst.pop(0) #usuwamy pierwszy element z listy
    if(len(lst)> 0): #sprawdzamy czy lista ma jeszcze jakieś elementy
        return (sum_of_numbers + sum_of_list(lst)) #jeśli tak: dodajemy kolejny element z listy do sumy i wracamy do początku
    else:
        return sum_of_numbers #jeśli nie: zwracamy sumę

list = [5, 4, 4, 4, 1]
list = sum_of_list(list)
print("The sum of the list is:", list)

def factorial(n):
    if n == 0:
        return 1 #dla n równego 0 zwracamy 1 
    else:
        return n * factorial(n - 1) #w przeciwnym wypadku zwracamy n razy silnia z n-1

number = 6
n_factorial = factorial(number)
print(f"The factorial of {number} is: {n_factorial}")