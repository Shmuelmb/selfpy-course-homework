def process_user_choice(choice, data):
    """
    Process user's choice and perform the corresponding operation on the given data.

    Args:
        choice (int): User's choice (between 1 and 7).
        data (dict): Dictionary containing the data.

    Returns:
        None

    Raises:
        ValueError: If the choice is not between 1 and 7.
    """
    match choice:
        case 1:
            last_name = data['last_name']
            print(f"Last Name: {last_name}")
        case 2:
            birth_month = data['birth_date'][3:5]
            print(f"Birth Month: {birth_month}")
        case 3:
            hobbies_count = len(data['hobbies'])
            print(f"Number of Hobbies: {hobbies_count}")
        case 4:
            last_hobby = data['hobbies'][-1]
            print(f"Last Hobby: {last_hobby}")
        case 5:
            data['hobbies'].append('Cooking')
            updated_hobbies = data['hobbies']
            print(f"Updated Hobbies: {updated_hobbies}")
        case 6:
            birth_date = tuple(data['birth_date'].split('.'))
            print(f"Birth Date: {birth_date}")
        case 7:
            data['age'] = 52
            age = data['age']
            print(f"Age: {age}")
        case default:
            raise ValueError("Invalid choice. Please enter a number between 1 and 7.")


# Example usage
kh = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}

user_choice = int(input("Enter a number between 1 and 7: "))
process_user_choice(user_choice, kh)
