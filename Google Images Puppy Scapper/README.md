# Google Images Puppy Scapper

Utilized the Beautiful Soup library to randomly webscrap images from Google Images.

Search terms are defined in a dictionary and then one is randomly chosen by key term value. 
```Python
SEARCH= {"dog": 1, "dogs":2, "pupper":3, "puppers":4, "puppy":5,"doggo":6, "doggie:":7, "cute dogs":8, "small puppies":9, "puppies":10, "doggies":11}
```

```Python
#A portion of download_images()
 def download_images():
     data = random.choice(list(SEARCH))
     print(f"searching for {data}")
     num_images = randint(1,80)
     print('searching...')
```
After that the number of images for that search term is then chosen out of a maximum of 80 files. 

## Images
