import os

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '323423619559-orlpuuiaalb7sp3ooblt4mjmp32ffq1t.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['CLIENT_SECRET']
SOCIAL_AUTH_GOOGLE_SCOPE = [
	'https://www.googleapis.com/auth/calendar',
	'https://www.googleapis.com/auth/plus.login',
]
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/scheduler/login'

