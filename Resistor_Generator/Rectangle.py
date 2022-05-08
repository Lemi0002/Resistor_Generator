def Draw(image: list, imageSize: tuple, rectanglePosition: tuple, rectangleSize: tuple, rectangleColor: tuple) -> bool:
    if imageSize.__len__() < 2 or rectanglePosition.__len__() < 2 or rectangleSize.__len__() < 2:
        print("ERROR: Not correct tuple format")
        print("-> Inserted size and position tuples must be two dimensional")
        return False

    for counterY in range(rectanglePosition[1], rectanglePosition[1] + rectangleSize[1]):
        for counterX in range(rectanglePosition[0], rectanglePosition[0] + rectangleSize[0]):
            if (counterX >= 0 and counterX < imageSize[0]) and (counterY >= 0 and counterY < imageSize[1]):
                image[counterX + counterY * imageSize[0]] = rectangleColor

    return True
