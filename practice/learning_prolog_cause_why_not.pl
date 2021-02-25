index([], -1, X).
index([X|_], I, X).
index([X|T], 0, V) :-
    X \= V,
    index(T, 1, V).