def volume_cylinder(radius, height):
    v = 3.14 * radius * radius * height  # or radius**2
    return v


print(volume_cylinder(7, 10))
print(volume_cylinder(7.4, 12.30))
print(round(volume_cylinder(7, 10), 2))

# key-value pairs arguments (args)
v1 = volume_cylinder(height=12, radius=5)

3
#TODO hello, put something here
def volume_cone(radius, height, decimals=2):
    v = 1 / 3 * 22 / 7 * radius ** 2 * height
    return round(v, decimals)
    return v


print(volume_cone(7, 10, decimals=1))
