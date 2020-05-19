import os


# Rename all images in this directory
def rename_image(path):
    for count, filename in enumerate(os.listdir(path)):
        dst = str(count) + ".jpg"
        print(filename + " --> " + dst)
        src = os.path.join(path, filename)
        dst = path + "/" + dst

        os.rename(src, dst)


def percentage_corrected(result, answer):
    total = len(result)
    correct = 0
    wrong = 0
    for i in range(total):
        # Remove whitespaces(head, tail)
        result[i] = result[i].strip()
        if result[i] == answer[i]:
            correct += 1
        else:
            wrong += 1

    print(correct, wrong)
    percent = float((correct / total)) * 100.0
    return str(percent) + "%"


def is_rename(path):
    list_image = os.listdir(path)
    list_image.sort(key=lambda f: int(os.path.splitext(f)[0]))
    if list_image[0] == "0.jpg":
        return True
    else:
        return False
