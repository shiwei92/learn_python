#导入整个模块
'''import pizza
pizza.make_pizza(16,"pepper")'''
#导入某个模块的某个方法
'''from pizza import make_pizza
make_pizza(16,"pepper","mushroom")'''
#使用as给模块执行别名
'''import pizza as pz
pz.make_pizza(20,"pepper","mushroom")'''

#使用as给函数指定别名
'''from pizza import make_pizza as mp
mp(18,"pepper","mushroom")'''
#导入模块中所有函数 (与import pizza 区别，不必再使用module_name.function_name,直接写function_name)
from pizza import *
make_pizza(21,"red pepper","apple")
