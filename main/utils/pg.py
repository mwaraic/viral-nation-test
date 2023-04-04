from main.models import users

class Pg:
    """
    PostgreSQL Class
    """

    def __init__(self):
        pass

    def retrieve_data(self) -> list:
        """
        retrieve data from users table
        """

        users_list = list(users.objects.all().values())

        return users_list

    def store_data(self, data: list):
        """
        store data in users table
        """

        users_list = []

        for user_data in data:
            user =users(
                id=user_data['id'],
                address=user_data['address'],
                username=user_data['username'],
                password=user_data['password'],
                first_name=user_data['name']['firstname'],
                last_name=user_data['name']['lastname'],
                phone_number=user_data['phone']
            )
            users_list.append(user)
        
        users.objects.bulk_create(users_list, ignore_conflicts=True, update_fields=['id', 'username'])
            


