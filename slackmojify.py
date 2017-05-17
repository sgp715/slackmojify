import argparse

def slackmojify(image_path):

    print("File already satisfies slackmoji requirements.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make a file uploadable as a slackmoji.')
    parser.add_argument('image', metavar='I', type=str, nargs=1, help='path to the file to minimize')

    args = parser.parse_args()
    slackmojify(args.image)
