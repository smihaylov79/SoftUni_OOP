from project.library import Library
from project.user import User
class Registration:

    @staticmethod
    def add_user(user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        return f"We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if new_username == user.username:
                    return f"Please check again the provided username - it should be different than the username used so far!"
                else:
                    old_un=user.username
                    user.username = new_username
                    if old_un in library.rented_books:
                        library.rented_books[new_username]=library.rented_books[old_un]
                        del library.rented_books[old_un]
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
            return f"There is no user with id = {user_id}!"

