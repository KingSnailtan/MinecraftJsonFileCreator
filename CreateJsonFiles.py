tex_path = input("Enter path to textures: ")
model_path = input("Enter path where you want your json files to be saved: ")
resource_path = tex_path.split("textures")[1];
resource_path = resource_path.replace("\\","")
import os
for file in os.listdir(tex_path):
    if file.endswith(".png"):
        json = open((model_path+"/"+file.title().split(".")[0]+".json").lower(),'w')
        json.write("}\n   \"parent\": \"minecraft:item/handheld\",\n   \"textures\": {\n        \"layer0\": \"minecraft:"+resource_path+"/"+(file.title().split(".")[0]).lower()+"\n   }\n}")
        json.close
