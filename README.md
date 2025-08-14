<div align="center">

# 🎯 GitHitBox

*A fast, reusable GitHub profile hit counter that generates beautiful badge images*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](https://opensource.org/licenses/MIT)

</div>

## 🚀 Features

- **🌍 Universal**: Works for any GitHub username
- **🎨 4 Badge Styles**: flat, plastic, counter, for-the-badge
- **⚡ Fast**: Built with FastAPI
- **💾 Persistent**: Database storage (SQLite/PostgreSQL)
- **🚀 Easy to Deploy**: Works on any hosting platform

## 📖 Usage

Add to your GitHub profile README:

```markdown
![Profile Views](https://githitbox.duckdns.org/badge/your-username)
```

**Styles Available:**

| Style | Example |
|-------|---------|
| Flat (default) | ![Flat](https://githitbox.duckdns.org/badge/demo1?v=1) |
| Plastic | ![Plastic](https://githitbox.duckdns.org/badge/demo2?style=plastic&v=1) |
| Counter | ![Counter](https://githitbox.duckdns.org/badge/demo3?style=counter&v=1) |
| For-the-badge | ![Badge](https://githitbox.duckdns.org/badge/demo4?style=for-the-badge&v=1) |

> 💡 **Tip**: Add `?v=2` to bypass GitHub's image cache

## 🛠️ Local Development

```bash
git clone https://github.com/siiddhantt/githitbox
cd githitbox
pip install -r requirements.txt
python main.py
```

Visit `http://localhost:3001/docs` for API documentation.

## 🔌 API Endpoints

- `GET /badge/{username}?style={style}` - Badge image
- `GET /count/{username}` - JSON hit count
- `GET /stats` - Global statistics
- `GET /health` - Health check

## ⚙️ Configuration

**Environment Variables:**
- `DATABASE_URL` - Database connection (defaults to SQLite)

**Badge Styles:**
- `flat` - Clean, modern (default)
- `plastic` - Rounded, glossy
- `counter` - Digital display with dark theme
- `for-the-badge` - Bold, rectangular

## 📝 License

MIT License - free to use for your projects!

---

<div align="center">

⭐ **Star this repo if you find it useful!**

[![GitHub stars](https://img.shields.io/github/stars/siiddhantt/githitbox?style=social)](https://github.com/siiddhantt/githitbox/stargazers)

</div>
