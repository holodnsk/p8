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

#Задание Lite
#1. Выполнить задание уровня ultra-light
#2. Написать декоратор, замеряющий время выполнение декорируемой функции.
#3. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
import time

def show_time(f):
  def wrapper(*args, **kwargs):
    time_before = time.time()
    f(*args,**kwargs)
    time_after = time.time()
    print(f.__name__,'time',time_after-time_before)
  return wrapper

@show_time
def get_list1():
  return [i for i in range(1,1000001)]

@show_time
def generator1():
  for i in range(1,1000001):
    yield (i)

get_list1()
generator1()

#Задание Pro
#1. Выполнить задание уровня light
#2. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
#3. 4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.
import psutil
psutil.Process().memory_info().rss / (1024 * 1024)

def show_mem(f):
  def wrapper(*args, **kwargs):
    mb_start = psutil.Process().memory_info().rss / (1024 * 1024)
    f(*args,**kwargs)
    mb_end = psutil.Process().memory_info().rss / (1024 * 1024)
    print(f.__name__,'got MB',mb_end-mb_start)
  return wrapper


@show_mem
def get_list2():
  return [i for i in range(1,1000001)]

@show_mem
def generator2():
  for i in range(1,1000001):
    yield (i)

get_list2()
generator2()


