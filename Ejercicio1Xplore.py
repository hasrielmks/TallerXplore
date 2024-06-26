# Program que cuenta cuantas veces fue citado un articulo del mismo autor 
import json
from collections import defaultdict

def read_input():
    N = int(input().strip())
    articles = [input().strip() for _ in range(N)]
    return articles

def parse_articles(articles):
    author_citations = defaultdict(list)
    for article in articles:
        data = json.loads(article)
        author = data["author"]
        citations = data["citations"]
        author_citations[author].append(citations)
    return author_citations

def calculate_h_index(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index

def get_authors_h_indices(author_citations):
    author_h_indices = []
    for author, citations in author_citations.items():
        h_index = calculate_h_index(citations)
        author_h_indices.append((author, h_index))
    return author_h_indices

def sort_authors_by_h_index(author_h_indices):
    return sorted(author_h_indices, key=lambda x: (-x[1], x[0]))

def print_results(sorted_authors):
    for author, h_index in sorted_authors:
        print(f"{author} {h_index}")

def main():
    articles = read_input()
    author_citations = parse_articles(articles)
    author_h_indices = get_authors_h_indices(author_citations)
    sorted_authors = sort_authors_by_h_index(author_h_indices)
    print_results(sorted_authors)

if __name__ == "__main__":
    main()

'''
# FORMA ADEACUADA DE ENTRADA POR CONSOLA
10
{"author": "Alice", "citations": 5}
{"author": "Bob", "citations": 3}
{"author": "Charlie", "citations": 8}
{"author": "Alice", "citations": 10}
{"author": "Charlie", "citations": 2}
{"author": "Bob", "citations": 5}
{"author": "David", "citations": 7}
{"author": "Eve", "citations": 1}
{"author": "David", "citations": 3}
{"author": "Alice", "citations": 6}
'''