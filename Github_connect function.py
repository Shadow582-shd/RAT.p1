def github_connect():
    with open('secret.txt') as f:
        token = f.read().strip()
    user = 'hackspark'
    sess = github3.login(token=token)
    return sess.repository(user, 'Trojan')
