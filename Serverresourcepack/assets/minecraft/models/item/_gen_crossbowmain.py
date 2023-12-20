import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

type = ["crosscrossbow", "crosscrossbow_pulling_0", "crosscrossbow_pulling_1", "crosscrossbow_pulling_2","crosscrossbow_arrow","crosscrossbow_firework"]
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
        "layer0": "item/crossbow"
    },
    "display": {
        "thirdperson_righthand": {
            "rotation": [ -90, 0, -60 ],
            "translation": [ 2, 0.1, -3 ],
            "scale": [ 0.9, 0.9, 0.9 ]
        },
        "thirdperson_lefthand": {
            "rotation": [ -90, 0, 30 ],
            "translation": [ 2, 0.1, -3 ],
            "scale": [ 0.9, 0.9, 0.9 ]
        },
        "firstperson_righthand": {
            "rotation": [ -90, 0, -55 ],
            "translation": [ 1.13, 3.2, 1.13],
            "scale": [ 0.68, 0.68, 0.68 ]
        },
        "firstperson_lefthand": {
            "rotation": [ -90, 0, 35 ],
            "translation": [ 1.13, 3.2, 1.13],
            "scale": [ 0.68, 0.68, 0.68 ]
        }
    },
    "overrides": [
'''

    vanillaline = '''        { "predicate": { "pulling": 1 }, "model": "item/crossbow_pulling_0" },
        { "predicate": { "pulling": 1, "pull": 0.58 }, "model": "item/crossbow_pulling_1" },
        { "predicate": { "pulling": 1, "pull": 1.0 }, "model": "item/crossbow_pulling_2" },
        { "predicate": { "charged": 1 }, "model": "item/crossbow_arrow" },
        { "predicate": { "charged": 1, "firework": 1 }, "model": "item/crossbow_firework" },'''

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
                lineO = lineO + "\n" + f'''
        {{ "predicate": {{ "custom_model_data": {model_data} }}, "model": "tooltrims:item/trims/crossbow_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "pulling": 1 }}, "model": "tooltrims:item/trims/crossbow_pulling_0_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "pulling": 1, "pull": 0.58 }}, "model": "tooltrims:item/trims/crossbow_pulling_1_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "pulling": 1, "pull": 1.0 }}, "model": "tooltrims:item/trims/crossbow_pulling_2_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "charged": 1 }}, "model": "tooltrims:item/trims/crossbow_arrow_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "charged": 1, "firework": 1 }}, "model": "tooltrims:item/trims/crossbow_firework_{trim[i]}_{material[j]}" }}'''
            else:
                lineO = lineO + "\n" + f'''
        {{ "predicate": {{ "custom_model_data": {model_data} }}, "model": "tooltrims:item/trims/crossbow_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "pulling": 1 }}, "model": "tooltrims:item/trims/crossbow_pulling_0_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "pulling": 1, "pull": 0.58 }}, "model": "tooltrims:item/trims/crossbow_pulling_1_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "pulling": 1, "pull": 1.0 }}, "model": "tooltrims:item/trims/crossbow_pulling_2_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "charged": 1 }}, "model": "tooltrims:item/trims/crossbow_arrow_{trim[i]}_{material[j]}" }}, 
        {{ "predicate": {{ "custom_model_data": {model_data}, "charged": 1, "firework": 1 }}, "model": "tooltrims:item/trims/crossbow_firework_{trim[i]}_{material[j]}" }},'''

    line8 = "    ]"
    line9 = "}"

    lines = line1 + vanillaline + lineO + "\n" + line8 + "\n" + line9


    filename = f"crossbow.json"
    text = lines
        
    # Write the text to the file
    with open(filename, "w") as file:
        file.write(text)