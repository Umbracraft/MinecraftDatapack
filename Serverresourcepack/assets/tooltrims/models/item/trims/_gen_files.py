import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

toolt = ["sword","pickaxe","axe","shovel","hoe"]
toolm = ["netherite","diamond","golden","iron","stone","wooden"]
trim = ["linear","tracks","charge","frost"]
material = ["amethyst","copper","diamond","emerald","gold","iron","lapis","netherite","quartz","redstone"]

print("Are you sure you want run it? (y/n)")
answer = input()

# Create multiple files
if answer == "y":
    for h in range(len(toolt)):
        for i in range(len(toolm)):
            for j in range(len(trim)):
                for k in range(len(material)):
                    filename = f"{toolm[i]}_{toolt[h]}_{trim[j]}_{material[k]}.json"
                    text = f"{{\n   \"parent\": \"minecraft:item/handheld\",\n   \"textures\": {{\n       \"layer0\": \"tooltrims:item/trims/{toolm[i]}_{toolt[h]}_{trim[j]}_{material[k]}\"\n   }}\n}}"

                    # Write the text to the file
                    with open(filename, "w") as file:
                        file.write(text)