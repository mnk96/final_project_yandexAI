MAX_USERS = 3
MAX_GPT_TOKENS = 120

MAX_USER_STT_BLOCKS = 10
MAX_USER_TTS_SYMBOLS = 5000
MAX_USER_GPT_TOKENS = 2000

LOGS = 'logs.txt'
DB_FILE = 'messages.db'

IAM_TOKEN_PATH = '/creds/aim_token.txt'
FOLDER_ID_PATH = '/creds/folder_id.txt'
BOT_TOKEN_PATH = '/creds/bot_token.txt'

SYSTEM_PROMT = [{
    'role': 'system',
    'text': 'Ты весёлый собеседник. Общайся с пользователем на "ты". Общайся как человек и вежливо.'
}]
