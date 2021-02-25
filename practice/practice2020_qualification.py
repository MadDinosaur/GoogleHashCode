
filename = "input/a_example.txt"
file = open(filename, "r")

#Read and save info from first line of file
line = file.readline().split(" ")

total_books = int(line[0])
total_libraries = int(line[1])
total_days = int(line[2])

#Read and save info of scores (each score is stored in an array, as it is a mutable data type)
line = file.readline().split(" ")
scores = []
for score in line:
    arr = []
    arr.append(int(score))
    scores.append(arr)

#Store all libraries available
libraries = []
#Store all signed up libraries
registered_libraries = []
#Sum of all the scanned books scores
final_score = 0

def createLibrary(n_books, set_books, n_days, n_perday):
    library = {
        "stock": n_books,
        "scores": [scores[int(x)] for x in set_books],
        "signup": n_days,
        "shipping": n_perday
    }
    return library

for i in range(total_libraries):
    lib_info = file.readline().split(" ")
    libraries.append(createLibrary(int(lib_info[0]), file.readline().split(" "), int(lib_info[1]), int(lib_info[2])))

file.close()

def calculateIntersections(y, days_left):
    intersect = (-1, None)
    for lib in libraries:
        if lib["signup"] > days_left:
            libraries.remove(lib)
            continue
        total_score = sum([j for sub in lib["scores"] for j in sub])
        # y = (shipping * total score) / stock * x - signup
        x = y / (lib["shipping"] * total_score / lib["stock"]) + lib["signup"]
        if not 0 <= intersect[0] <= x:
            intersect = (x, lib)

    signup_lib = intersect[1]
    if signup_lib is not None:
        libraries.remove(signup_lib)

    return signup_lib


days_left = total_days
while days_left > 0:
    registering_lib = calculateIntersections(4, days_left)
    if not registering_lib:
        idle_time = days_left
    else:
        idle_time = registering_lib["signup"]
    while idle_time > 0:
        for lib in registered_libraries:
            for i in range(lib["shipping"]):
                best_book = max(lib["scores"])
                final_score += best_book[0]
                lib["scores"][lib["scores"].index(best_book)][0] = 0
        idle_time -= 1
        days_left -= 1
    registered_libraries.append(registering_lib)

print("total score = " + str(final_score))
