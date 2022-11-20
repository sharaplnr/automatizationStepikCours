s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


# проверка, что в url содержится строка login
# assert 'login' in browser.current_url, 'сообщение об ошибке'

def substring(full_string, substring):
    assert substring in full_string, f'expected \'{substring}\', to be substring of \'{full_string}\''


substring('My Name is Julia', 'Name')
