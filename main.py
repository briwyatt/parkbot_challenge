import argparse
import json


def parse_parking_spots_by_args(*args):
    response = []
    with open('airgarage-data.json') as d:
        spot_data = json.load(d)
    if args:
        for spot in spot_data:
            if spot['address']['state'] == str(args[0]):
                response.append(spot)
            else:
                response.append(spot)
    else:
        response = spot_data
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser('add optional location parameter for your query')
    parser.add_argument('--locale', type=str, help='2 letter state code goes here')
    args = parser.parse_args()
    if args:
        output = parse_parking_spots_by_args(args)
    else:
        output = parse_parking_spots_by_args()
    print(output)
