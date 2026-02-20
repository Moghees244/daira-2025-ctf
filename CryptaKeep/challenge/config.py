class Config:
    SECRET_KEY = 'secretkey'
    JWT_SECRET_KEY = "verysecurekey"
    JWT_TOKEN_LOCATION = "cookies"
    JWT_COOKIE_CSRF_PROTECT = False