
# 布尔类型和布尔对象
print(bool(1))
print(bool(True))
print(bool('0'))
print(bool([]))
print(bool((1,)))

# 使用bool数
foo = 42
bar = foo < 42

print(bar)
print(bar + 10)
print('%s' % bar)
print('%d' % bar)

# 类型转换  complex负数
print(int(5.01212))
print(float(8))
print(complex(8))

# 进制转换
print('+++++++进制转换+++++++')
# 8进制
print(hex(255))
# 10进制
print(oct(255))
# 16进制
print(oct(0x111))

# ASII 转换
# chr函数和ord函数分别用来将数字转换为字符，和字符转换为数字
print('+++++++ASII 转换+++++++')
print(chr(76))
print(ord('L'))
