# from transformers import pipeline


# # load the model (downloads first time, be patient)
# classifier = pipeline("image-classification", model="dima806/clothes_image_detection" , framework="pt")

# # your photos
# images = ["notebook/test_images/kurta_testimg.JPG", "notebook/test_images/top_testimg.JPG", "notebook/test_images/tshirt_testimg.JPG"]

# # loop through images, get prediction, print result
# for img in images:
#     results = classifier(img)
#     top = results[0]
#     print(f"{img} → {top['label']} ({top['score']:.0%})")

# top['label']    
# top['score']    


#using next model 

from transformers import pipeline


class_names = ["Blazer",
"Blouse",
"Cardigan",
"Dress",
"Hoodie",
"Jacket",
"Jeans",
"Nightgown",
"Outerwear",
"Pajamas","Rain jacket",
"Rain trousers",
"Robe",
"Shirt",
"Shorts",
"Skirt",
"Sweater",
"T-shirt",
"Tank top",
"Tights",
"Top",
"Training top",
"Trousers",
"Tunic",
"Vest",
"Winter jacket","Winter trousers"]

# load the model (downloads first time, be patient)
classifier = pipeline("image-classification", model="wargoninnovation/wargon-clothing-classifier" , framework="pt")

# your photos
images = ["notebook/test_images/kurta_testimg.JPG", "notebook/test_images/top_testimg.JPG", "notebook/test_images/tshirt_testimg.JPG"]

# loop through images, get prediction, print result
for img in images:
    results = classifier(img)
    top = results[0]
    number = int(top['label'].replace("LABEL_", ""))
    garment = class_names[number]
    print(f"{img} → {garment} ({top['score']:.0%})")

# sanity check: full guess list for the one garment we're sure about
print(classifier("notebook/test_images/tshirt_testimg.JPG"))