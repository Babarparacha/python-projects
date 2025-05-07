import http.server
import socketserver
import urllib.parse
import json
import os

PORT = 5055
DATA_FILE = "posts.json"

def load_posts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_posts(posts):
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f)

class BlogHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.render_index()
        elif self.path.startswith('/create'):
            self.render_template('templates/create.html')
        elif self.path.startswith('/edit'):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            post_id = int(query.get('id', [0])[0])
            self.render_edit(post_id)
        elif self.path.startswith('/delete'):
            self.handle_delete()
        else:
            super().do_GET()

    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        post_data = urllib.parse.parse_qs(self.rfile.read(length).decode())

        if self.path == '/create':
            title = post_data['title'][0]
            content = post_data['content'][0]
            posts = load_posts()
            post_id = max([p['id'] for p in posts], default=0) + 1
            posts.append({"id": post_id, "title": title, "content": content})
            save_posts(posts)
            self.redirect('/')
        elif self.path.startswith('/edit'):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            post_id = int(query.get('id', [0])[0])
            title = post_data['title'][0]
            content = post_data['content'][0]
            posts = load_posts()
            for post in posts:
                if post['id'] == post_id:
                    post['title'] = title
                    post['content'] = content
                    break
            save_posts(posts)
            self.redirect('/')

    def render_template(self, path, context=None):
        with open(path, 'r') as f:
            html = f.read()
        if context:
            for key, value in context.items():
                html = html.replace(f'{{{{ {key} }}}}', str(value))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(html.encode())

    def render_index(self):
        posts = load_posts()
        items = ""
        for post in posts:
            items += f"""
            <li>
                <h2>{post['title']}</h2>
                <p>{post['content']}</p>
                <a href="/edit?id={post['id']}">Edit</a> |
                <a href="/delete?id={post['id']}">Delete</a>
            </li>
            """
        with open('templates/index.html', 'r') as f:
            html = f.read().replace('{{ posts }}', items)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(html.encode())

    def render_edit(self, post_id):
        posts = load_posts()
        post = next((p for p in posts if p['id'] == post_id), None)
        if post:
            context = {
                "id": post['id'],
                "title": post['title'],
                "content": post['content']
            }
            self.render_template('templates/edit.html', context)
        else:
            self.send_error(404, "Post not found")

    def handle_delete(self):
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        post_id = int(query.get('id', [0])[0])
        posts = load_posts()
        posts = [p for p in posts if p['id'] != post_id]
        save_posts(posts)
        self.redirect('/')

    def redirect(self, location):
        self.send_response(302)
        self.send_header('Location', location)
        self.end_headers()

Handler = BlogHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
