#!/usr/bin/env python3
"""
Google Drive Upload Script with OAuth Flow
Sets up OAuth authorization and uploads files to Google Drive
"""

import os
import json
import pickle
import sys
import time
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
    import io
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please install: pip install google-auth google-auth-oauthlib google-api-python-client oauthlib google-auth-httplib2")
    sys.exit(1)

# File paths for OAuth credentials and tokens
TOKEN_PATH = '/root/openclaw/token.pickle'
CREDS_PATH = '/root/openclaw/credentials.json'

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Files to upload
FILES_TO_UPLOAD = [
    '/root/openclaw/aleph-cloud-marketing-analysis.md',
    '/root/openclaw/aleph-cloud-seo-analysis.md',
    '/root/openclaw/space-strategy-game/README.md',
    '/root/openclaw/space-strategy-game/PROGRESS.md',
    '/root/openclaw/space-strategy-game/SETUP_SUMMARY.md',
    '/root/openclaw/space-strategy-game/PROJECT_COORDINATION.md',
    '/root/openclaw/space-strategy-game/docs/ARCHITECTURE.md',
    '/root/openclaw/space-strategy-game/docs/ECONOMY.md',
    '/root/openclaw/space-strategy-game/docs/TASKS.md'
]

def create_credentials_json(client_id, client_secret):
    """
    Create credentials.json file from client ID and secret
    This simulates the OAuth client credentials flow
    """
    creds_data = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uris": ["http://localhost:8080"],
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }
    
    with open(CREDS_PATH, 'w') as f:
        json.dump(creds_data, f, indent=2)
    
    print(f"✓ Created credentials.json")
    return CREDS_PATH

def get_credentials():
    """
    Get valid credentials for the Google Drive API.
    Returns credentials if valid, otherwise starts OAuth flow.
    """
    credentials = None
    
    if os.path.exists(TOKEN_PATH):
        credentials = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    # If no valid credentials or credentials are expired, start OAuth flow
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
                print("✓ Refreshed access token")
            except Exception as e:
                print(f"Error refreshing token: {e}")
                credentials = None
        
        if not credentials:
            print("\n🔐 Starting OAuth authorization flow...")
            print("✓ Browser will open automatically")
            print("✓ Please authorize this application to access your Google Drive")
            print("✓ Then copy the authorization code and paste it below\n")
            
            # Load client secrets
            with open(CREDS_PATH, 'r') as f:
                client_config = json.load(f)
            
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            credentials = flow.run_local_server(port=8080)
            
            # Save the credentials for next time
            with open(TOKEN_PATH, 'w') as token:
                pickle.dump(credentials, token)
            print("\n✓ Credentials saved!")
    
    return credentials

def upload_file(service, file_path, file_name=None):
    """
    Upload a file to Google Drive
    """
    if file_name is None:
        file_name = os.path.basename(file_path)
    
    file_metadata = {
        'name': file_name,
        'mimeType': 'application/octet-stream'
    }
    
    # Check if file already exists in Drive
    try:
        response = service.files().list(
            q=f"name = '{file_name}'",
            spaces='drive',
            fields='files(id, name, modifiedTime)'
        ).execute()
        
        existing_files = response.get('files', [])
        
        if existing_files:
            print(f"  → File already exists (skipping): {file_name}")
            return None
    except Exception as e:
        print(f"  → Error checking for existing file: {e}")
    
    print(f"  → Uploading: {file_name}...", end='')
    
    try:
        # Upload the file
        media = MediaFileUpload(
            file_path,
            resumable=True
        )
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()
        
        print(" ✓")
        return file
    except Exception as e:
        print(f" ✗ Error: {e}")
        return None

def main():
    """Main function to set up OAuth and upload files"""
    print("=" * 70)
    print("Google Drive File Uploader")
    print("=" * 70)
    print()
    
    # Your OAuth credentials
    CLIENT_ID = "870251413533-mdpid0h8fucclfq5saabmu5v0jfeghep.apps.googleusercontent.com"
    CLIENT_SECRET = "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"
    
    # Create credentials.json if it doesn't exist
    if not os.path.exists(CREDS_PATH):
        print("⚠️  Creating credentials.json from Client ID and Secret...")
        create_credentials_json(CLIENT_ID, CLIENT_SECRET)
    else:
        print("✓ credentials.json already exists")
    
    print()
    
    # Get credentials (OAuth flow)
    credentials = get_credentials()
    
    if not credentials:
        print("Error: Could not get valid credentials")
        return
    
    print(f"\n✓ Using credentials: {credentials.token if credentials.token else 'None'}")
    
    # Build Google Drive API service
    print("\n📁 Connecting to Google Drive API...")
    try:
        service = build('drive', 'v3', credentials=credentials)
        print("✓ Connected successfully")
    except Exception as e:
        print(f"✗ Error building service: {e}")
        return
    
    # Upload files
    print("\n" + "=" * 70)
    print("UPLOADING FILES")
    print("=" * 70)
    print()
    
    uploaded_files = []
    skipped_files = []
    failed_files = []
    
    for file_path in FILES_TO_UPLOAD:
        if not os.path.exists(file_path):
            print(f"  ✗ File not found: {file_path}")
            failed_files.append(file_path)
            continue
        
        result = upload_file(service, file_path)
        
        if result:
            file_id = result.get('id')
            file_name = result.get('name')
            view_link = result.get('webViewLink')
            
            uploaded_files.append({
                'name': file_name,
                'id': file_id,
                'link': view_link
            })
            
            print(f"    📄 View: {view_link}")
        elif result is None:
            skipped_files.append(os.path.basename(file_path))
        else:
            failed_files.append(file_path)
    
    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"✅ Successfully uploaded: {len(uploaded_files)} files")
    print(f"⏭️  Skipped: {len(skipped_files)} files")
    print(f"❌ Failed: {len(failed_files)} files")
    print()
    
    if uploaded_files:
        print("Uploaded Files:")
        for f in uploaded_files:
            print(f"  • {f['name']}")
            print(f"    Link: {f['link']}")
            print()
    
    if skipped_files:
        print("Skipped Files (already exist in Drive):")
        for f in skipped_files:
            print(f"  • {f}")
        print()
    
    if failed_files:
        print("Failed Files:")
        for f in failed_files:
            print(f"  • {f}")
        print()
    
    # Save upload report
    report_path = '/root/openclaw/drive_upload_report.json'
    report = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'uploaded_count': len(uploaded_files),
        'skipped_count': len(skipped_files),
        'failed_count': len(failed_files),
        'uploaded_files': uploaded_files,
        'skipped_files': skipped_files,
        'failed_files': failed_files
    }
    
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📄 Report saved to: {report_path}")
    print()
    print("=" * 70)
    print("Upload complete!")
    print("=" * 70)

if __name__ == '__main__':
    main()
