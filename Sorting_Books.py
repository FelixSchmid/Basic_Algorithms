import Books
import Insertion_Sort

der_prozess = Books.Books('Der Prozess', 'Franz Kafka', '9783958551930', 263)
vermessung_der_welt = Books.Books('Die Vermessung der Welt', 'Daniel Kehlmann', '9783499241000', 224)
the_phycisian = Books.Books('The Physician', 'Noah Gordon', '1453271104', 600)

der_prozess.add_author('Ghostwriter')

books_list = [der_prozess, vermessung_der_welt, the_phycisian]
for element in books_list:
    print(element.title)

books_list_sorted = Insertion_Sort.insort(books_list)
for element in books_list_sorted:
    print(element.title)
