# GitHitBox

A fast, reusable GitHub profile hit counter that generates beautiful badge images.

## 🚀 Features

- **Universal**: Works for any GitHub username
- **4 Badge Styles**: flat, plastic, counter, for-the-badge
- **Fast**: Built with FastAPI
- **Persistent**: SQLite database
- **Free to Host**: Railway, Render, Fly.io ready

## 📖 Usage

Add to your GitHub profile README:

```markdown
![Profile Views](https://your-app.railway.app/badge/your-username)
```

Replace `your-username` with your GitHub username and `your-app.railway.app` with your deployed URL.

### Badge Styles

```markdown
![Flat](https://your-app.railway.app/badge/octocat)
![Plastic](https://your-app.railway.app/badge/octocat?style=plastic) 
![Counter](https://your-app.railway.app/badge/octocat?style=counter)
![For-the-badge](https://your-app.railway.app/badge/octocat?style=for-the-badge)
```

## 🛠️ Local Development

```bash
git clone https://github.com/yourusername/githitbox
cd githitbox
pip install -r requirements.txt
python main.py
```

Visit `http://localhost:8000/docs` for API documentation.

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
