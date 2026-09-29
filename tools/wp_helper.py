"""Ajudante de acesso ao WordPress. A senha vem da variável de ambiente WP_PASS (nunca gravada em arquivo)."""
import http.cookiejar, urllib.request, urllib.parse, urllib.error, json, os, re, ssl, uuid

BASE = 'https://elovital.com.br'
USER = os.environ.get('WP_USER', 'Claude Code')

class WP:
    def __init__(self):
        self.jar = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar), urllib.request.HTTPRedirectHandler())
        self.op.addheaders = [('User-Agent', 'Mozilla/5.0 (compatible; ClaudeCode-Elovital)')]
        self.nonce = None

    def _do(self, req, timeout=120):
        try:
            r = self.op.open(req, timeout=timeout); return r.status, r.read(), dict(r.headers)
        except urllib.error.HTTPError as e:
            return e.code, e.read(), dict(e.headers)

    def get(self, url, timeout=120, headers=None):
        req = urllib.request.Request(url if url.startswith('http') else BASE + url, headers=headers or {})
        return self._do(req, timeout)

    def login(self):
        self.get('/wp-login.php')
        self.jar.set_cookie(http.cookiejar.Cookie(0, 'wordpress_test_cookie', 'WP%20Cookie%20check', None, False, 'elovital.com.br', True, False, '/', True, True, None, False, None, None, {}))
        data = urllib.parse.urlencode({'log': USER, 'pwd': os.environ['WP_PASS'], 'redirect_to': BASE + '/wp-admin/', 'testcookie': '1'}).encode()
        st, body, h = self._do(urllib.request.Request(BASE + '/wp-login.php', data=data))
        assert any('wordpress_logged_in' in c.name for c in self.jar), 'login falhou'
        st, body, h = self.get('/wp-admin/admin-ajax.php?action=rest-nonce')
        self.nonce = body.decode().strip()
        return self

    def rest(self, method, path, payload=None, raw=None, headers=None, timeout=180):
        h = {'X-WP-Nonce': self.nonce}
        data = None
        if payload is not None:
            data = json.dumps(payload).encode(); h['Content-Type'] = 'application/json'
        if raw is not None: data = raw
        if headers: h.update(headers)
        req = urllib.request.Request(BASE + '/wp-json' + path, data=data, method=method, headers=h)
        st, body, hd = self._do(req, timeout)
        try: js = json.loads(body)
        except Exception: js = body[:300]
        return st, js

    def post_form(self, path, fields, timeout=300):
        data = urllib.parse.urlencode(fields).encode()
        return self._do(urllib.request.Request(BASE + path, data=data), timeout)

    def upload_media(self, filepath, filename, mime, title=None):
        with open(filepath, 'rb') as f: raw = f.read()
        st, js = self.rest('POST', '/wp/v2/media', raw=raw, headers={
            'Content-Type': mime, 'Content-Disposition': f'attachment; filename="{filename}"'}, timeout=300)
        return st, js
