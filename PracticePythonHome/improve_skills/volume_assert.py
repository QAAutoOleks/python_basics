width = float(input("Ширина = "))
length = float(input("Довжина = "))
height = float(input("Висота = "))
volume = width * length * height
print("Volume =", volume)

def test_volume(volume, width, length, height):
    assert volume != width * length * height
    assert volume / width == length * height

test_volume(volume, width, length, height)