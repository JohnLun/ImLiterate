import os

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    
    res = []
    for i in range(1,len(texts)):
        print(texts[i].description)
        res.append(texts[i].description)

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return res

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "striped-option-362104-9d3f8028bfa8.json"
word_list = detect_text("practice-image.png")
for word in word_list:
    print(word)

