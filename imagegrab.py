import requests

def downloadImage(url, name='temp', folder=None):
    path = ''

    if folder == None:
        path = name + '.jpg'
    else:
        path = f"{folder}/{name}.jpg"

    with open(path, 'wb') as targetfile:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            targetfile.write(block)

def downloadImages(url, names, folder=None):
    for name in names:
        thisurl = url[0] + name + url[1]
        downloadImage(thisurl, name, folder)

# download a single image to a folder
url = "http://openweathermap.org/img/wn/10d@2x.png"
downloadImage(url)

# download multiple images and store them in a folder
images = ["01d", "01n",
          "02d", "02n",
          "03d", "03n",
          "04d", "04n",
          "09d", "09d",
          "10d", "10n",
          "11d", "11n",
          "13d", "13n",
          "50d", "50n"]
folder = "Images"
url = ["http://openweathermap.org/img/wn/", "@2x.png"]
downloadImages(url, images, folder)
