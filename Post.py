class Post():
    def __init__(self, username, location, description, likes_counter=0, comments=None):
        self.username = username
        self.location = location
        self. description = description
        self.likes_counter = likes_counter
        self.comments = comments
    def add_like(self, likes_counter):
        likes_counter+=1

    def add_comment(self, text):
        self.comments.append(text)

    def display(self):
        print(self.username)
        print(self.location)
        print(self. description)
        print(self.likes_counter)
        print(self.comments)

