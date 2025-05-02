import re
from collections import defaultdict

def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    index = defaultdict(lambda: defaultdict(int))

    for i, doc in enumerate(documents):
        words = re.findall(r'\b\w+\b', doc.lower())
        for word in words:
            index[word][i] += 1

    results = []
    for query in queries:
        q = query.lower()
        if q in index:
            doc_counts = index[q]
            sorted_docs = sorted(doc_counts.items(), key=lambda x: (-x[1], -x[0]))
            results.append([doc_id for doc_id, _ in sorted_docs])
        else:
            results.append([])

    return results



if __name__ == "__main__":
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())


    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())


    results = index_documents(documents, queries)

    print("Wyniki:")
    for res in results:
        print(res)