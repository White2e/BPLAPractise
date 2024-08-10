import jwt
import practise_2_15_srv


SECRET_KEY = 'my_KEY'


def request_token(user_id):
    return practise_2_15_srv.create_token(user_id)


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.InvalidTokenError:
        print('Invalid token')
        return None
    except jwt.ExpiredSignatureError:
        print('Expired token')
        return None


user_id = 'user123'
token = request_token(user_id)
print(f'Generated token: {token}')

verified_user_id = verify_token(token)
print(f'Verified user ID: {verified_user_id}')

user_id_from_token = verify_token(token)
if user_id_from_token:
    print(f'User ID from token matches: {user_id == verified_user_id}')
else:
    print('User ID from token does not match')


# # Проверка невалидного токена
# invalid_token = 'invalid_token'
# invalid_verified_user_id = verify_token(invalid_token)
# print(f'Invalid verified user ID: {invalid_verified_user_id}')
#
# # Проверка истекшего токена
# expired_token = jwt.encode({'user_id': user_id}, SECRET_KEY, algorithm='HS256', expires_in=0)
# expired_verified_user_id = verify_token(expired_token)
# print(f'Expired verified user ID: {expired_verified_user_id}')
#

