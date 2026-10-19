"""
Flask SSO App mit Microsoft Entra ID (Azure AD) Integration
Auftrag 13: SSO Python App
"""

import os
from flask import Flask, redirect, url_for, session, render_template_string
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')

# OAuth Setup für Microsoft Entra ID
oauth = OAuth(app)

# Microsoft Entra ID Configuration
microsoft = oauth.register(
    'microsoft',
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    server_metadata_url=f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}/v2.0/.well-known/openid-configuration",
    client_kwargs={
        'scope': 'openid profile email'
    }
)

# HTML Templates
LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SSO Login - Entra ID</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 30px;
        }
        .login-btn {
            background: #0078d4;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            text-decoration: none;
            display: inline-block;
        }
        .login-btn:hover {
            background: #005a9e;
        }
        .info {
            margin-top: 20px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔐 SSO Login mit Entra ID</h1>
        <p>Klick auf den Button um dich mit Entra ID anzumelden</p>
        <a href="{{ url_for('login') }}" class="login-btn">Login mit Microsoft</a>
        <div class="info">
            <p>Es sollte KEIN Passwort-Prompt kommen!</p>
            <p>Du solltest automatisch angemeldet werden.</p>
        </div>
    </div>
</body>
</html>
'''

SUCCESS_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SSO Success</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #28a745;
            margin-bottom: 20px;
        }
        .user-info {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 4px;
            margin: 20px 0;
            text-align: left;
        }
        .user-info p {
            margin: 10px 0;
            color: #333;
        }
        .logout-btn {
            background: #dc3545;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        .logout-btn:hover {
            background: #c82333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ SSO Login erfolgreich!</h1>
        <p>Du bist jetzt angemeldet über Entra ID!</p>

        <div class="user-info">
            <h3>Benutzer-Informationen:</h3>
            <p><strong>Name:</strong> {{ user.get('name', 'N/A') }}</p>
            <p><strong>Email:</strong> {{ user.get('email', 'N/A') }}</p>
            <p><strong>User ID:</strong> {{ user.get('sub', 'N/A') }}</p>
        </div>

        <p style="color: #28a745; font-weight: bold;">
            🎉 Kein Passwort-Prompt! Das ist Single Sign-On (SSO)!
        </p>

        <a href="{{ url_for('logout') }}" class="logout-btn">Logout</a>
    </div>
</body>
</html>
'''

ERROR_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SSO Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #dc3545;
        }
        .error-msg {
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 4px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>❌ Error beim Login</h1>
        <div class="error-msg">
            {{ error }}
        </div>
        <a href="{{ url_for('index') }}" style="color: #0078d4;">← Zurück zum Login</a>
    </div>
</body>
</html>
'''

# Routes
@app.route('/')
def index():
    """Home/Login Seite"""
    return render_template_string(LOGIN_PAGE)

@app.route('/login')
def login():
    """Login Route - Redirect zu Entra ID"""
    redirect_uri = url_for('authorize', _external=True)
    logger.info(f"Login redirect_uri: {redirect_uri}")
    return microsoft.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    """Callback Route von Entra ID"""
    try:
        token = microsoft.authorize_access_token()
        session['token'] = token

        # User Info aus Token auslesen
        user = token.get('userinfo')
        if user:
            session['user'] = {
                'name': user.get('name', 'N/A'),
                'email': user.get('email', 'N/A'),
                'sub': user.get('sub', 'N/A')
            }
            logger.info(f"User logged in: {user.get('email')}")

        return redirect(url_for('dashboard'))
    except Exception as e:
        logger.error(f"Authorization error: {str(e)}")
        return render_template_string(ERROR_PAGE, error=str(e))

@app.route('/dashboard')
def dashboard():
    """Dashboard Seite - nur für angemeldete User"""
    user = session.get('user')

    if not user:
        return redirect(url_for('index'))

    return render_template_string(SUCCESS_PAGE, user=user)

@app.route('/logout')
def logout():
    """Logout Route"""
    session.clear()

    # Optional: Redirect zu Entra ID logout
    # logout_url = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}/oauth2/v2.0/logout"
    # return redirect(logout_url)

    return redirect(url_for('index'))

@app.route('/api/user')
def api_user():
    """API Endpoint für User Info"""
    user = session.get('user')

    if not user:
        return {'error': 'Not authenticated'}, 401

    return user

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return render_template_string(ERROR_PAGE, error="Seite nicht gefunden (404)"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template_string(ERROR_PAGE, error="Server Error (500)"), 500

if __name__ == '__main__':
    logger.info("=" * 50)
    logger.info("🚀 SSO Flask App startet...")
    logger.info(f"📍 http://localhost:5000")
    logger.info("=" * 50)

    # WICHTIG: Muss auf localhost:5000 laufen (nicht 127.0.0.1)!
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        ssl_context='adhoc'  # HTTPS für SSO (optional)
    )
