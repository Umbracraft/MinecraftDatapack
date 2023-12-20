from PIL import Image
import os

dname = os.path.dirname(os.path.abspath(__file__))
os.chdir(dname)

# trims color codes // Pain.NET & Luna images don't work
key = [(249,249,249), (212,212,212), (171,171,171), (131,131,131), (97,97,97), (74,74,74), (55,55,55), (40,40,40)]
amethyst = [(254,203,230),(207,160,243),(179,142,243),(141,106,204),(109,74,175),(84,57,138),(54,38,85),(39,27,63)]
copper = [(244,184,171),(238,155,125),(212,125,96),(181,96,67),(145,70,43),(117,56,34),(73,37,23),(53,27,17)]
diamond = [(215,249,245),(148,231,214),(70,211,194),(38,160,159),(32,109,116),(17,81,85),(9,57,57),(3,38,39)]
emerald = [(195,255,218),(130,246,173),(23,221,98),(0,170,44),(0,123,24),(0,83,0),(0,51,0),(0,37,0)]
gold = [(255,253,224),(255,234,149),(250,214,74),(230,149,27),(178,90,18),(137,54,12),(89,30,0),(70,23,0)]
iron = [(228,237,243),(207,217,220),(181,192,196),(136,146,151),(98,109,117),(65,75,81),(44,53,57),(35,41,44)]
lapis = [(120,158,194),(72,121,200),(35,96,171),(30,73,138),(21,53,114),(12,40,90),(9,30,69),(5,22,54)]
netherite = [(142,126,144),(113,103,114),(95,85,95),(80,66,72),(69,52,60),(61,43,44),(39,29,30),(28,21,22)]
quartz = [(242,239,237),(246,234,223),(227,219,196),(182,173,150),(144,142,128),(101,97,86),(65,62,56),(42,40,34)]
redstone = [(255,138,138),(255,89,89),(246,42,42),(199,27,11),(148,13,13),(109,21,13),(79,18,13),(57,17,13)]

dark_netherite = [(108,98,109), (95,85,95), (80,66,72), (69,52,60), (61,43,44), (39,29,30), (28,21,22), (18,11,12)]
dark_diamond = [(141,231,212), (59,222,202), (13,158,156), (7,104,112), (10,80,84), (8,61,61), (3,41,43), (1,21,23)]
dark_gold = [(255,234,149), (250,214,74), (227,157,20), (178,100,17), (152,67,10), (89,30,0), (70,23,0), (50,16,0)]
dark_iron = [(197,211,216), (153,169,176), (128,146,154), (94,114,122), (76,93,100), (52,63,65), (42,48,52), (28,33,35), (10,18,20)]

palettes_content = [amethyst, copper, diamond, emerald, gold, iron, lapis, netherite, quartz, redstone]
palettes_name = ["amethyst", "copper", "diamond", "emerald", "gold", "iron", "lapis", "netherite", "quartz", "redstone"]
dark_palettes_content = [amethyst, copper, dark_diamond, emerald, dark_gold, dark_iron, lapis, dark_netherite, quartz, redstone]

# combinations
type_verify = ["netherite","diamond","iron","gold","stone","wood"]
type = ["netherite","diamond","iron","golden","stone","wooden"]
tool = ["sword","pickaxe","axe","shovel","hoe","sword","pickaxe","axe","shovel","hoe","sword","pickaxe","axe","shovel","hoe","sword","pickaxe","axe","shovel","hoe","sword","pickaxe","axe","shovel","hoe","sword","pickaxe","axe","shovel","hoe"]
trims = ["linear","tracks","charge","frost"]

print("Are you sure you want run it? (y/n)")
answer = input()

if answer == "y":
    for fpalettes in range(len(palettes_name)):

        input_image = Image.open("_tooltrims_types_key.png")
        pixel_map = input_image.load()
        width, height = input_image.size

        grid_size = 16
        order = 0

        for fwidht in range(width):
            for fheight in range(height):
                order += 1/(grid_size*grid_size)
                h = int(order/((len(trims)*5)+0.1))

                for fkey in range(len(key)):
                    r, g, b, p = input_image.getpixel((fwidht, fheight))
                    
                    if (r, g, b) == key[fkey]:
                            pixel_map[fwidht, fheight] = palettes_content[fpalettes][fkey]
        
        width, height = input_image.size
        order = 0

        for j in range(0, int((height)/grid_size)):
                for i in range(0, int(width/grid_size)):
                    order += 1
                    h = int(order/((len(trims)*5)+0.1))
                    box = (i*grid_size, j*grid_size, (i+1)*grid_size, (j+1)*grid_size)
                    splited = input_image.crop(box)
                    splited.save(f"{type[h]}_{tool[j]}_{trims[i]}_{palettes_name[fpalettes]}.png", format="png")