# bounce.py
print('Bouncing ball exercise\n')
init_height =100.0
print('Initially ball height is ',init_height)
for bounce_count in range(1,11):
    new_height = 0.6 * init_height
    init_height = new_height
    print(bounce_count, round(new_height, 4))#

# Exercise 1.5
