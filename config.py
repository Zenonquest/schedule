# from scheduler.models import ClientSecret
# cs = ClientSecret.objects.get(pk=1)

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = cs['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = cs['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']
# SOCIAL_AUTH_GOOGLE_SCOPE = [
# 	cs['SOCIAL_AUTH_GOOGLE_SCOPE1'],
# 	cs['SOCIAL_AUTH_GOOGLE_SCOPE2']
# ]


# SOCIAL_AUTH_LOGIN_REDIRECT_URL = cs['SOCIAL_AUTH_LOGIN_REDIRECT_URL']
# SOCIAL_AUTH_LOGIN_URL = cs['SOCIAL_AUTH_LOGIN_URL']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '323423619559-orlpuuiaalb7sp3ooblt4mjmp32ffq1t.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '49JMMebwB4NwwFPic3UZ9z3m'
SOCIAL_AUTH_GOOGLE_SCOPE = [
	'https://www.googleapis.com/auth/calendar',
	'https://www.googleapis.com/auth/plus.login',
]



SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/scheduler/login'

