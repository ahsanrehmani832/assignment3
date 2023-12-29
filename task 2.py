class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email  # protected attribute
        self.__password = password  # private attribute
        self.posts = []

    def create_post(self, content):
        new_post = Post(content, self)
        self.posts.append(new_post)
        print(f"Post created by {self.username}")

    def like_post(self, post):
        post.add_like(self)
        print(f"{self.username} liked a post")

    def get_email(self):
        return self._email

class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)

    def manage_user_roles(self, user, new_role):
        # Assume roles can be strings like 'regular', 'moderator', 'admin', etc.
        user.role = new_role
        print(f"User role updated: {user.username} is now a {new_role}")


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []

    def add_like(self, user):
        self.likes.append(user)
        print(f"Post liked by {user.username}")

# Example Usage:

# Create users and admin
user1 = User("Alice", "alice@example.com", "password123")
user2 = User("Bob", "bob@example.com", "password456")
admin1 = Admin("AdminUser", "admin@example.com", "adminpass")

# Users create posts
user1.create_post("Hello, world!")
user2.create_post("Just posted something cool!")

# Users like posts
user1.like_post(user2.posts[0])

# Admin manages user roles
admin1.manage_user_roles(user2, "moderator")
