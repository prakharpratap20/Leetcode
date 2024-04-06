"""Given an array of integers citations where citations[i] is the number
of citations a reseracher recevied for their i th paper, return the 
reseracher's h-index.
According to the definition of h-index on Wikipedia: The h-index is definded
as the maximum value of h such that the given reseracher has published at least h
papers that have each been cited at least h times."""

def h_index(citations):
    citations.sort(reverse=True)

    if len(citations) == 1 and citations[0] > 0:
        return 1
    if citations[-1] >= len(citations):
        return len(citations)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    
    return 0

citation = [3, 0, 6, 1, 5, 4, 4]
print(h_index(citation))
