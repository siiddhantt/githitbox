# GitHitBox

A fast, reusable GitHub profile hit counter that generates beautiful badge images.

## 🚀 Features

- **Universal**: Works for any GitHub username
- **4 Badge Styles**: flat, plastic, counter, for-the-badge
- **Fast**: Built with FastAPI
- **Persistent**: Database storage (SQLite/PostgreSQL)
- **Easy to Deploy**: Works on any hosting platform

## 📖 Usage

Add to your GitHub profile README:

```markdown
![Profile Views](https://githitbox.duckdns.org/badge/your-username)
```

Replace `your-username` with your GitHub username.

**Note**: GitHub caches images. To see updated counts immediately, add a version parameter:
```markdown
![Profile Views](https://githitbox.duckdns.org/badge/your-username?v=2)
```

### Live Examples:

![Flat](https://githitbox.duckdns.org/badge/octocat?v=2)
![Plastic](https://githitbox.duckdns.org/badge/octocat?style=plastic&v=2) 
![Counter](https://githitbox.duckdns.org/badge/octocat?style=counter&v=2)
![For-the-badge](https://githitbox.duckdns.org/badge/octocat?style=for-the-badge&v=2)

## 🛠️ Local Development

```bash
git clone https://github.com/yourusername/githitbox
cd githitbox
pip install -r requirements.txt
python main.py
```

Visit `http://localhost:3001/docs` for API documentation.

## � API Endpoints

- `GET /badge/{username}?style={style}` - Badge image
- `GET /count/{username}` - JSON hit count
- `GET /stats` - Global statistics
- `GET /health` - Health check

## 🔧 Configuration

### Environment Variables
- `DATABASE_URL` - Database connection (defaults to SQLite)

### Badge Styles
- **flat** - Clean, modern (default)
- **plastic** - Rounded, glossy
- **counter** - Digital display with dark theme
- **for-the-badge** - Bold, rectangular

## 📝 License

MIT License - free to use for your projects!

---

⭐ Star this repo if you find it useful!
