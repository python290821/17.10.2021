# solution for homework
# page 35-1
_min = int(input('enter number: '))
for i in range(1, 100):
    _next = int(input('enter number: '))
    if _next < _min:
        print('not sorted!')
        break
    _min = _next
if _next >= _min:
    print('sorted')