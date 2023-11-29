def is_user_authenticated(user):
    return user.is_authenticated

def is_user_superuser(user):
    return user.is_authenticated and user.is_superuser