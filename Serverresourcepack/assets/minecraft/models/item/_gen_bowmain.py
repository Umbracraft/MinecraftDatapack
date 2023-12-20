import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

type = ["bow", "bow_pulling_0", "bow_pulling_1", "bow_pulling_2"]
trim = ["linear","tracks","charge","frost"]
material = ["amethyst","copper","diamond","emerald","gold","iron","lapis","netherite","quartz","redstone"]

print("Are you sure you want run it? (y/n)")
answer = input()

if answer == "y":
    # ---
    # gen
    # ---
    line1 = '''
{
    "parent": "item/generated",
    "textures": {
        "layer0": "item/bow"
    },
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
    },
    "overrides": [
'''

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
                lineO = lineO + "\n" + f"        {{ \"predicate\": {{ \"custom_model_data\": {model_data} }}, \"model\": \"tooltrims:item/trims/bow_{trim[i]}_{material[j]}\" }}, {{ \"predicate\": {{ \"custom_model_data\": {model_data}, \"pulling\": 1 }}, \"model\": \"tooltrims:item/trims/bow_pulling_0_{trim[i]}_{material[j]}\" }}, {{ \"predicate\": {{ \"custom_model_data\": {model_data}, \"pulling\": 1, \"pull\": 0.65 }}, \"model\": \"tooltrims:item/trims/bow_pulling_1_{trim[i]}_{material[j]}\" }}, {{ \"predicate\": {{ \"custom_model_data\": {model_data}, \"pulling\": 1, \"pull\": 0.9 }}, \"model\": \"tooltrims:item/trims/bow_pulling_2_{trim[i]}_{material[j]}\" }}"
            
            else:
                lineO = lineO + "\n" + f"        {{ \"predicate\": {{ \"custom_model_data\": {model_data} }}, \"model\": \"tooltrims:item/trims/bow_{trim[i]}_{material[j]}\" }}, {{ \"predicate\": {{ \"custom_model_data\": {model_data}, \"pulling\": 1 }}, \"model\": \"tooltrims:item/trims/bow_pulling_0_{trim[i]}_{material[j]}\" }}, {{ \"predicate\": {{ \"custom_model_data\": {model_data}, \"pulling\": 1, \"pull\": 0.65 }}, \"model\": \"tooltrims:item/trims/bow_pulling_1_{trim[i]}_{material[j]}\" }}, {{ \"predicate\": {{ \"custom_model_data\": {model_data}, \"pulling\": 1, \"pull\": 0.9 }}, \"model\": \"tooltrims:item/trims/bow_pulling_2_{trim[i]}_{material[j]}\" }},"

    line8 = "    ]"
    line9 = "}"

    lines = line1 + lineO + "\n" + line8 + "\n" + line9


    filename = f"bow.json"
    text = lines
        
    # Write the text to the file
    with open(filename, "w") as file:
                file.write(text)