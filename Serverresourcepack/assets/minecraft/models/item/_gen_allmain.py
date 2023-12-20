import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

tool_material = ["netherite","diamond","golden","iron","stone","wooden"]
tool = ["sword","pickaxe","axe","shovel","hoe"]
trim = ["linear","tracks","charge","frost"]
material = ["amethyst","copper","diamond","emerald","gold","iron","lapis","netherite","quartz","redstone"]

print("Are you sure you want run it? (y/n)")
answer = input()

if answer == "y":
    for m in range(len(tool_material)):
        for t in range(len(tool)):
            # ---------
            # variables
            # ---------
            main_tm = tool_material[m]
            main_tl = tool[t]

            # ---
            # gen
            # ---
            line1 = "{"
            line2 = "    \"parent\": \"minecraft:item/handheld\","
            line3 = "    \"textures\": {"
            line4 = f"        \"layer0\": \"minecraft:item/{main_tm}_{main_tl}\""
            line5 = "    },"
            line6 = "    \"overrides\": ["

            lineO = ""

            model_data = 311000

            for i in range(len(trim)):
                for j in range(len(material)):

                    model_data = int(model_data) + 1
                    #model_data = round(model_data,3)

                    #if len(str(model_data)) == 4:
                        #model_data = str(model_data) + "0"
                    #if len(str(model_data)) == 3:
                        #model_data = str(model_data) + "00"

                    if i == len(trim) - 1 and j == len(material) - 1 :
                        lineO = lineO + "\n" + f"        {{\"predicate\": {{ \"custom_model_data\": {model_data}}}, \"model\": \"tooltrims:item/trims/{main_tm}_{main_tl}_{trim[i]}_{material[j]}\"}}"
                    
                    else:
                        lineO = lineO + "\n" + f"        {{\"predicate\": {{ \"custom_model_data\": {model_data}}}, \"model\": \"tooltrims:item/trims/{main_tm}_{main_tl}_{trim[i]}_{material[j]}\"}},"

            line8 = "    ]"
            line9 = "}"

            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + lineO + "\n" + line8 + "\n" + line9


            filename = f"{tool_material[m]}_{tool[t]}.json"
            text = lines
                
            # Write the text to the file
            with open(filename, "w") as file:
                        file.write(text)