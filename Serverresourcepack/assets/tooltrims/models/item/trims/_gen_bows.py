import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

type = ["bow", "bow_pulling_0", "bow_pulling_1", "bow_pulling_2"]
trim = ["linear","tracks","charge","frost"]
material = ["amethyst","copper","diamond","emerald","gold","iron","lapis","netherite","quartz","redstone"]

print("Are you sure you want run it? (y/n)")
answer = input()

# Create multiple files
if answer == "y":
    for h in range(len(type)):
        for j in range(len(trim)):
            for k in range(len(material)):
                filename = f"{type[h]}_{trim[j]}_{material[k]}.json"
                text0 = "{"
                text1 = f"\n   \"parent\": \"minecraft:item/handheld\",\n   \"textures\": {{\n       \"layer0\": \"tooltrims:item/trims/{type[h]}_{trim[j]}_{material[k]}\"\n   }},"
                text2 = '''
      "display": {
        "thirdperson_righthand": {
            "rotation": [ -80, 260, -40 ],
            "translation": [ -1, -2, 2.5 ],
            "scale": [ 0.9, 0.9, 0.9 ]
        },
        "thirdperson_lefthand": {
            "rotation": [ -80, -280, 40 ],
            "translation": [ -1, -2, 2.5 ],
            "scale": [ 0.9, 0.9, 0.9 ]
        },
        "firstperson_righthand": {
            "rotation": [ 0, -90, 25 ],
            "translation": [ 1.13, 3.2, 1.13],
            "scale": [ 0.68, 0.68, 0.68 ]
        },
        "firstperson_lefthand": {
            "rotation": [ 0, 90, -25 ],
            "translation": [ 1.13, 3.2, 1.13],
            "scale": [ 0.68, 0.68, 0.68 ]
        }
    }
                '''
                text3 = "\n}"

                # Write the text to the file
                with open(filename, "w") as file:
                    file.write(text0 + text1 + text2 + text3)