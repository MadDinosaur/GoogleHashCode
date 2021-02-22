total_books = 6
total_libraries = 2
total_days = 7
libraries = []
registered_libraries = []

scores = [[1], [2], [3], [6], [5], [4]]

final_score = 0


def createLibrary(n_books, set_books, n_days, n_perday):
    library = {
        "stock": n_books,
        "scores": [scores[x] for x in set_books],
        "signup": n_days,
        "shipping": n_perday
    }
    return library


libraries.append(createLibrary(5, [0, 1, 2, 3, 4], 2, 2))
libraries.append(createLibrary(4, [3, 2, 5, 0], 3, 1))


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
    if registering_lib is None:
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

print(final_score)
