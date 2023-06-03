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

def fibonacci(n):
    if n <= 0:
        return [0] #dla n=0 zwracamy jednoelementową listę: [0]
    elif n == 1:
        return [0, 1] # dla n=1 zwracamy dwuelementową listę: [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence #w innych wypadku ustalamy sekwencję dla n-1, a następnie dodajemy do listy sumę dwóch poprzednich elementów

number2 = 5
fibo = fibonacci(number2)
print(f"The Fibonacci sequence for {number2} is: {fibo}")

def solve_sudoku(grid):
    for i in range(2): 
        for j in range(2): #iterowanie przez kolumny i wiersze
            if grid[i][j] == 0: #sprawdzanie czy komórki sa puste
                for num in range(1, 3): #jeśli tak, to próbujemy je wypełnić liczbami od 1 do 2
                    if is_valid_move(grid, i, j, num): #sprawdzamy czy możemy wstawić daną liczbę
                        grid[i][j] = num #jeśli tak to wstawiamy
                        if solve_sudoku(grid): #wracając wypełniamy resztę komórek
                            return True
                        grid[i][j] = 0
                return False #jeśli nie ma możliwości dodania liczby to niepowodzenie
    return True #w przeciwnym razie jest super!!! :)

def is_valid_move(grid, row, col, num): #sprawdzamy czy w kolumnach lub wierszach liczby się nie powtarzają
    for i in range(2):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

sudoku_grid = [[2, 0], [1, 0]]

if solve_sudoku(sudoku_grid):
    print("Sudoku solved:")
    for row in sudoku_grid:
        print(*row)
else:
    print("No solution exists for the Sudoku.")

sudoku_grid2 = [[2, 0], [0, 1]]

if solve_sudoku(sudoku_grid2):
    print("Sudoku solved:")
    for row in sudoku_grid2:
        print(*row)
else:
    print("No solution exists for the Sudoku.")