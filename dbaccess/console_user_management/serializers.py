def user_role_assignment_serializer(assignments):
    def serializer(a):
        return {
            "id": a.id,
            "user": {
                "id": a.user.id,
                "email": a.user.email,
            },
            "role": {
                "id": a.role.id,
                "role_name": a.role.role_name,
            },
            "expiry_date": a.expiry_date.isoformat(),
        }

    return [serializer(a) for a in assignments]
