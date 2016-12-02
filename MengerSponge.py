"""
MengerSponge.py
"""
from visual import *

scene = display(title="Menger Sponge", height=700, width=700, range=450)
scene.lights = 0
lamp = local_light(pos=(0, 0, 0), color=color.white)
scene.center = (0, 0, 0)

value = input("Enter the level of the fractal:  ")


def recursive(level, p, L):
    if level == 1:
        box(pos=p, length=L, height=L, width=L, color=color.green)
    else:
        # Right slice
        p1 = vector(p.x + L / 3, p.y + L / 3, p.z + L / 3);
        p2 = vector(p.x + L / 3, p.y + L / 3, p.z);
        p3 = vector(p.x + L / 3, p.y + L / 3, p.z - L / 3);
        p4 = vector(p.x + L / 3, p.y, p.z + L / 3);
        p5 = vector(p.x + L / 3, p.y, p.z - L / 3);
        p6 = vector(p.x + L / 3, p.y - L / 3, p.z + L / 3);
        p7 = vector(p.x + L / 3, p.y - L / 3, p.z);
        p8 = vector(p.x + L / 3, p.y - L / 3, p.z - L / 3);

        # Middle slice
        p9 = vector(p.x, p.y + L / 3, p.z + L / 3);
        p10 = vector(p.x, p.y + L / 3, p.z - L / 3);
        p11 = vector(p.x, p.y - L / 3, p.z + L / 3);
        p12 = vector(p.x, p.y - L / 3, p.z - L / 3);

        # Left slice
        p13 = vector(p.x - L / 3, p.y + L / 3, p.z + L / 3);
        p14 = vector(p.x - L / 3, p.y + L / 3, p.z);
        p15 = vector(p.x - L / 3, p.y + L / 3, p.z - L / 3);
        p16 = vector(p.x - L / 3, p.y, p.z + L / 3);
        p17 = vector(p.x - L / 3, p.y, p.z - L / 3);
        p18 = vector(p.x - L / 3, p.y - L / 3, p.z + L / 3);
        p19 = vector(p.x - L / 3, p.y - L / 3, p.z);
        p20 = vector(p.x - L / 3, p.y - L / 3, p.z - L / 3);

        # Cube lengths have a little extra so as to overlap
        recursive(level - 1, p1, L / 3 + 0.1);
        recursive(level - 1, p2, L / 3 + 0.1);
        recursive(level - 1, p3, L / 3 + 0.1);
        recursive(level - 1, p4, L / 3 + 0.1);
        recursive(level - 1, p5, L / 3 + 0.1);
        recursive(level - 1, p6, L / 3 + 0.1);
        recursive(level - 1, p7, L / 3 + 0.1);
        recursive(level - 1, p8, L / 3 + 0.1);
        recursive(level - 1, p9, L / 3 + 0.1);
        recursive(level - 1, p10, L / 3 + 0.1);
        recursive(level - 1, p11, L / 3 + 0.1);
        recursive(level - 1, p12, L / 3 + 0.1);
        recursive(level - 1, p13, L / 3 + 0.1);
        recursive(level - 1, p14, L / 3 + 0.1);
        recursive(level - 1, p15, L / 3 + 0.1);
        recursive(level - 1, p16, L / 3 + 0.1);
        recursive(level - 1, p17, L / 3 + 0.1);
        recursive(level - 1, p18, L / 3 + 0.1);
        recursive(level - 1, p19, L / 3 + 0.1);
        recursive(level - 1, p20, L / 3 + 0.1)


recursive(level=value, p=vector(0, 0, 0), L=400)
