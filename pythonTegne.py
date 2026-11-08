from browser import document

bredde = 110
høyde = 80

canvas = document["canvas"]
context = canvas.getContext("2d")

def tegn_piksel(x, y, r, g, b):
    context.fillStyle = f"rgb({r}, {g}, {b})"
    context.fillRect(x, y, 1, 1)

def tegn_flagg():
    for y in range(høyde):
        for x in range(bredde):
            if 35 <= x < 45 or 35 <= y < 45:
                tegn_piksel(x, y, 0, 0, 160)
            elif 30 <= x < 50 or 30 <= y < 50:
                tegn_piksel(x, y, 255, 255, 255)
            else:
                tegn_piksel(x, y, 220, 0, 0)

tegn_flagg()
