def tee_tuple(x: int, y: int, z: int):
    return (sorted([x,y,z])[0], sorted([x,y,z], reverse=True)[0], x + y + z)

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))
