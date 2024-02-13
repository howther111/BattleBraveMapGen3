from PIL import Image, ImageFilter
import settings2 as settings

if __name__ == '__main__':
    print("Program Start")

    backgrouwnIm = Image.open(settings.backgroundImg)

    backgrouwnIm = backgrouwnIm.filter(ImageFilter.GaussianBlur(5))

    backgrouwnIm.save(settings.backgroundImg)

    print("Program End")