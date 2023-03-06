import random
from pprint import pprint
import time
import json
start_time = time.time()

authors = ["Gabriel Garcia Marquez", "Harper Lee", "Albert Camus", "Fyodor Dostoevsky",
           "Chinua Achebe", "J.D. Salinger", "Franz Kafka", "Leo Tolstoy", "Virginia Woolf",
           "Jane Austen", "Ernest Hemingway", "Yukio Mishima", "Gustave Flaubert", "James Joyce",
           "Isabel Allende", "Khaled Hosseini", "Miguel de Cervantes", "Nikolai Gogol",
           "Aldous Huxley", "Margaret Atwood", "Kazuo Ishiguro", "Jules Verne", "Toni Morrison",
           "Ray Bradbury", "Italo Calvino", "José Saramago", "Hermann Hesse", "J.R.R. Tolkien",
           "Emily Bronte", "Octavio Paz", "George Orwell", "Chimamanda Ngozi Adichie",
           "F. Scott Fitzgerald", "Chuang Tzu", "Umberto Eco", "Jorge Luis Borges", "Mary Shelley",
           "Orhan Pamuk", "John Steinbeck"]

languages = ["Spanish", "English", "French", "Russian", "Japanese", "German", "Italian", "Portuguese",
             "Chinese", "Turkish"]

titles = ["Cien Años de Soledad", "To Kill a Mockingbird", "L'étranger", "Crime and Punishment",
          "Things Fall Apart", "The Catcher in the Rye", "Die Verwandlung", "War and Peace",
          "Mrs Dalloway", "Pride and Prejudice", "The Old Man and the Sea", "Confessions of a Mask",
          "Madame Bovary", "Ulysses", "La Casa de los Espíritus", "The Kite Runner",
          "Don Quijote de la Mancha", "Dead Souls", "Brave New World", "The Handmaid's Tale",
          "Never Let Me Go", "Journey to the Center of the Earth", "Beloved", "Fahrenheit 451",
          "Il Barone Rampante", "Ensaio Sobre a Cegueira", "Siddhartha", "The Lord of the Rings",
          "Wuthering Heights", "El Laberinto de la Soledad", "Animal Farm", "Half of a Yellow Sun",
          "The Great Gatsby", "Zhuangzi", "Il Nome della Rosa", "Ficciones", "Frankenstein",
          "Kara Kitap", "Of Mice and Men", "The Brothers Karamazov", "Heart of Darkness", "The Trial",
          "One Hundred Years of Solitude", "The Stranger", "1984", "The Sound and the Fury",
          "The Picture of Dorian Gray", "The Scarlet Letter", "Gone with the Wind", "The Odyssey",
          "Moby-Dick", "The Adventures of Huckleberry Finn", "Les Misérables", "The Count of Monte Cristo",
          "Anna Karenina", "The Idiot", "Dracula", "The Hound of the Baskervilles", "Alice's Adventures in Wonderland",
          "Through the Looking-Glass", "Gulliver's Travels", "Robinson Crusoe",]


books = []

while len(books) < 10000:
    author = random.choice(authors)
    language = random.choice(languages)
    title = random.choice(titles)
    book = {"author": author, "language": language, "title": title}
    if book not in books:
        books.append(book)

with open("books.json", "w") as f:
    json.dump(books, f)


end_time = time.time()

print("Time elapsed: {:.2f} seconds".format(end_time - start_time))