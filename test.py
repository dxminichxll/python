<<<<<<< HEAD
print(ord("A"))
=======
def make_readable(seconds):
    hours = seconds // 3600
    new_seconds = seconds % 60
    if hours > 0:
        minutes = (seconds % 3600) // 60
    else:
        minutes = seconds // 60
    return hours, minutes, new_seconds

make_readable(0)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)
>>>>>>> c5b8e09be9d3d483dad989a1dba286aac90e5e02
