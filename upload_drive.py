#!/usr/bin/env python3
import os
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# OAuth 2.0 Configuration
CLIENT_ID = '870251413533-mdpid0h8fucclfq5saabmu5v0jfeghep.apps.googleusercontent.com'
CLIENT_SECRET = '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'
SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_FILE = 'token.json'

def get_credentials():
    """Get valid user credentials from storage or run the authorization flow."""
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        if credentials and credentials.valid:
            return credentials

    # Create client secrets config
    client_secrets = {
        'web': {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uris': ['http://localhost:8080'],
            'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            'token_uri': 'https://oauth2.googleapis.com/token'
        }
    }

    # Save client secrets to file
    with open('client_secret.json', 'w') as f:
        import json
        json.dump(client_secrets, f)

    # Use the web application flow
    flow = InstalledAppFlow.from_client_config(client_secrets, SCOPES)

    print("🔐 Opening browser for Google Drive authorization...\n")
    print("1. Open this URL: http://localhost:8080")
    print("2. Authorize the app")
    print("3. You'll be redirected to a localhost URL\n")

    credentials = flow.run_local_server(
        host='localhost',
        port=8080,
        open_browser=True
    )

    # Save the credentials for future use
    with open(TOKEN_FILE, 'w') as token:
        token.write(credentials.to_json())

    return credentials

def upload_file(file_path):
    """Upload a file to Google Drive."""
    file_name = os.path.basename(file_path)

    # Determine MIME type
    if file_path.endswith('.md'):
        mime_type = 'text/markdown'
    else:
        mime_type = 'text/plain'

    print(f"📄 Uploading {file_name} to Google Drive...")

    # Create service
    credentials = get_credentials()
    service = build('drive', 'v3', credentials=credentials)

    # Create the file
    file_metadata = {
        'name': file_name,
        'parents': ['root'],
        'mimeType': mime_type
    }

    # Upload the file
    media = MediaFileUpload(
        file_path,
        mimetype=mime_type,
        resumable=True
    )

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"✅ Uploaded: {file_name} (ID: {file.get('id')})\n")

def upload_all_files():
    """Upload all markdown files to Google Drive."""
    files = [
        'aleph-cloud-marketing-analysis.md',
        'aleph-cloud-seo-analysis.md',
        'space-strategy-game/README.md',
        'space-strategy-game/PROGRESS.md',
        'space-strategy-game/SETUP_SUMMARY.md',
        'space-strategy-game/PROJECT_COORDINATION.md',
        'space-strategy-game/docs/ARCHITECTURE.md',
        'space-strategy-game/docs/ECONOMY.md',
        'space-strategy-game/docs/TASKS.md'
    ]

    print("🦀 Clawdberg Google Drive Uploader\n")
    print("================================\n")

    success_count = 0

    for file_path in files:
        full_path = os.path.join('/root/openclaw', file_path)

        if not os.path.exists(full_path):
            print(f"⚠️  Skipped (not found): {file_path}\n")
            continue

        try:
            upload_file(full_path)
            success_count += 1
        except Exception as e:
            print(f"❌ Error uploading {file_path}: {e}\n")

    print("================================")
    print(f"✅ Uploaded {success_count}/{len(files)} files\n")

if __name__ == '__main__':
    upload_all_files()
