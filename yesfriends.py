import requests
import json

def main():

    URL = 'https://yesfriends.co/products/mens-t-shirt-black'
    response = requests.get(URL)
    index_start = response.text.index('product:', 0) + len('product:')
    index_finish = response.text.index(', }', index_start)
    json_obj = json.loads(response.text[index_start:index_finish])

    for variant in json_obj['variants']:
        available = 'IN STOCK' if variant['available'] else 'OUT OF STOCK'
        print(variant['id'], variant['option1'], available)

if __name__ == '__main__':
    main()