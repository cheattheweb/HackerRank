
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# for x_ in range(x+1):
#    for y_ in range(y+1):
#        for z_ in range(z+1):
#            if (x_+y_+z_) != n:
#                result.append([x_, y_, z_])
#                pass
# print(result)

result = [[X, Y, Z] for X in range(x+1) for Y in range(y+1)
          for Z in range(z+1) if X+Y+Z != n]
print(result)
