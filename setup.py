from setuptools import setup

packages = [line.strip() for line in open("requirements.txt").readlines()]

APP = ['main.py']
APP_NAME = "Debug50"
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'ui/assets/icons/app.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "AI-powered rubberducking",
        'CFBundleIdentifier': "com.oscaem.debug50",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
    },
    'packages': packages,
}

setup(
    app=APP,
    name=APP_NAME,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)