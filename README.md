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
![Profile Views](https://your-deployed-url.com/badge/your-username)
```

Replace `your-username` with your GitHub username and `your-deployed-url.com` with your deployed application URL.

### Badge Styles

```markdown
![Flat](https://your-deployed-url.com/badge/octocat)
![Plastic](https://your-deployed-url.com/badge/octocat?style=plastic) 
![Counter](https://your-deployed-url.com/badge/octocat?style=counter)
![For-the-badge](https://your-deployed-url.com/badge/octocat?style=for-the-badge)
```

## 🛠️ Local Development

```bash
git clone https://github.com/yourusername/githitbox
cd githitbox
pip install -r requirements.txt
python main.py
```

Visit `http://localhost:8000/docs` for API documentation.

## 🐳 Docker Deployment

### Quick Start
```bash
git clone https://github.com/yourusername/githitbox
cd githitbox
docker-compose up -d
```

### Production Deployment
```bash
# On your server
git clone https://github.com/yourusername/githitbox
cd githitbox

# Set up environment variables
cp .env.example .env
# Edit .env with your database URL

# Deploy
chmod +x deploy.sh
./deploy.sh
```

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
