#Задание Ultra Lite
#1. Написать свой генератор последовательностей, свой тернарный оператор
N=10

# генератор списка
generated_list = [(i**2) for i in range(1,N+1) if (i**2)%2 == 0]
print('generated_list',generated_list)

# генератор словаря
generated_dict = {i:(i**2) for i in range(1,N+1) if (i**2)%2 == 0}
print('generated_dict',generated_dict)

# генератор множества
generated_set = {i**2 for i in range(1,N+1)}
generated_set_d = {(i**2)%10 for i in range(1,N+1)}
print('generated_set',generated_set)
print('generated_set_d',generated_set_d)

# тернарный оператор
check_age = 17
check = 1 if check_age >=18 else 0
check_lambda = lambda x: 1 if x>=18 else 0

print('check check_age=',check_age,check)
print('check_lambda 17',check_lambda(17))
print('check_lambda 18',check_lambda(18))
print('check_lambda 19',check_lambda(19))

#2. Написать свой декоратор
def show_information(f):
  def wrapper(*args, **kwargs):
    print('до function')
    f(*args, **kwargs)
    print('после function')
  return wrapper

@show_information
def function():
  print('function()')

function()

