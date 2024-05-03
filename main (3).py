# game.py
import math_functions

def game():
    score = 0
    operations = {
        '1': math_functions.add,
        '2': math_functions.subtract,
        '3': math_functions.multiply,
        '4': math_functions.divide,
        '5': math_functions.power,
        '6': math_functions.modulus
    }

    while True:
        print('======== Menu ========'
              '\n1. Add'
              '\n2. Subtract'
              '\n3. Multiply'
              '\n4. Divide'
              '\n5. Power'
              '\n6. Modulus'
              '\n0. Exit')
        option = input('\nChoose an option: ')

        if option == '0':
            break

        num_1 = int(input('Enter the first number: '))
        num_2 = int(input('Enter the second number: '))

        if option in operations:
            try:
                result = operations[option](num_1, num_2)
                answer = float(input('Enter your answer: '))
                if abs(result - answer) < 0.0001:  
                    if option in ['1', '2']:
                        score += 1
                    elif option in ['3', '4', '5', '6']:
                        score += 2
                    print('Correct!!')
                else:
                    print('Incorrect')
            except ZeroDivisionError:
                print('Error: Cannot divide by zero!')
            except ValueError:
                print('Error: Invalid input! Please enter a number.')

    print(f'======== Game Over ========'
          f'\nYour score is {score}'
          '\nKeep going!')

if __name__ == '__main__':
    game()

