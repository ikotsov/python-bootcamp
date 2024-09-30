import colorgram

colors = colorgram.extract('painting.webp', 30)

rgb_colors= []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    rgb_colors.append((red, green, blue))

print(rgb_colors)
