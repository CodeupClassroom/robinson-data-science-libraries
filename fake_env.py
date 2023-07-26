# this is a fake env file to show off what we 
# would want inside of an env file
# an env file is there to help store/obfuscate 
# credentials so prying eyes dont get the same
# access that you do!
# this is important! especially when you have admin privs!
# we really only need three things here:
# (you may have more in the future)
# user: who you are
# host: where you're going
# password: how you get in

user = 'my_username'
host = 'my_server'
password = 'my_secrets'

def create_url(user, host, password, db):
    return f'sql+pymysql://{user}:{password}@{host}/{db}'