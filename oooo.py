try:
    if __name__ == "__main__":
        __spec__.__bool__ == True
    else:
        __spec__.__bool__ = False
except:
    print("Outstanding")