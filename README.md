# GitHitBox

A production-ready, reusable GitHub profile hit counter service that generates beautiful badge images and tracks page views.

## 🚀 Features

- **Universal**: Works for any GitHub username
- **Customizable**: Multiple badge styles (flat, plastic, for-the-badge)
- **Fast**: Built with FastAPI for high performance
- **Persistent**: SQLite database for reliable data storage
- **Production Ready**: Comprehensive error handling and validation
- **Free to Host**: Designed for free hosting services

## 📖 Usage

### In Your GitHub Profile README

Simply add this to your GitHub profile README.md:

```markdown
![Profile Views](https://your-deployed-url.com/badge/your-username)
```

Replace `your-username` with your actual GitHub username and `your-deployed-url.com` with your deployed service URL.

### Available Endpoints

#### 1. Badge Endpoint
```
GET /badge/{username}?style={style}
```
- Returns a PNG badge image
- **Parameters:**
  - `username`: GitHub username (required)
  - `style`: Badge style - `flat` (default), `plastic`, `counter`, or `for-the-badge`

**Examples:**
- `https://your-domain.com/badge/octocat`
- `https://your-domain.com/badge/octocat?style=plastic`
- `https://your-domain.com/badge/octocat?style=counter`
- `https://your-domain.com/badge/octocat?style=for-the-badge`

#### 2. Count Endpoint
```
GET /count/{username}
```
Returns JSON with hit count data:
```json
{
  "username": "octocat",
  "count": 42,
  "created_at": "2024-01-01T00:00:00",
  "last_hit": "2024-01-01T12:00:00"
}
```

#### 3. Global Stats
```
GET /stats
```
Returns global statistics:
```json
{
  "total_profiles": 100,
  "total_hits": 5000,
  "service": "GitHitBox"
}
```

## 🛠️ Development

### Prerequisites
- Python 3.8+
- pip

### Local Setup

1. **Clone and navigate to the project:**
   ```bash
   cd profile-counter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   python main.py
   ```

The service will be available at `http://localhost:8000`

### API Documentation
Once running, visit `http://localhost:8000/docs` for interactive API documentation.

## 🚀 Deployment

### Free Hosting Options

#### 1. Railway (Recommended)
- **Pros**: Easy deployment, generous free tier, automatic SSL
- **Setup**: Connect GitHub repo, auto-deploys on push
- **Free Tier**: 500 hours/month, sufficient for most use cases

#### 2. Render
- **Pros**: Simple setup, good free tier, built-in SSL
- **Free Tier**: 750 hours/month, sleeps after 15min inactivity

#### 3. Fly.io
- **Pros**: Global edge deployment, excellent performance
- **Free Tier**: 160GB-hours/month, minimal cold starts

#### 4. Heroku
- **Pros**: Mature platform, lots of documentation
- **Note**: Free tier discontinued, but still a good option for paid hosting

### Environment Variables

For production deployment, set these environment variables:

```bash
DATABASE_URL=your_database_url  # Optional: defaults to SQLite
```

### Railway Deployment

1. Fork this repository
2. Connect your GitHub account to Railway
3. Create a new project from your forked repo
4. Railway will automatically detect the Python app and deploy

### Render Deployment

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repo
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

## 🏗️ Architecture

- **Backend**: FastAPI (Python)
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Image Generation**: Pillow (PIL)
- **Deployment**: Platform-agnostic (Railway, Render, Fly.io)

## 🔧 Configuration

### Badge Styles

1. **Flat** (default): Clean, modern look
2. **Plastic**: Slightly rounded, glossy appearance
3. **Counter**: Digital counter with individual digit boxes (dark theme)
4. **For-the-badge**: Bold, rectangular style

### Database

- **Development**: SQLite (included)
- **Production**: PostgreSQL recommended for high traffic

## 📊 Monitoring

- Health check endpoint: `/health`
- Global statistics: `/stats`
- Individual user stats: `/count/{username}`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

MIT License - feel free to use this for your own projects!

## 🌟 Examples

Here are some example badges:

- Flat style: `![Profile Views](https://your-domain.com/badge/octocat)`
- Plastic style: `![Profile Views](https://your-domain.com/badge/octocat?style=plastic)`
- Counter style: `![Profile Views](https://your-domain.com/badge/octocat?style=counter)`
- For-the-badge style: `![Profile Views](https://your-domain.com/badge/octocat?style=for-the-badge)`

## ⚡ Performance

- **Response Time**: < 100ms for badge generation
- **Concurrent Users**: Supports hundreds of concurrent requests
- **Database**: Optimized queries with proper indexing
- **Caching**: Headers set to prevent unwanted caching of dynamic content

## 🔒 Security

- Input validation for usernames
- SQL injection prevention with SQLAlchemy ORM
- Rate limiting ready (can be added with middleware)
- CORS support (can be configured as needed)

---

Made with ❤️ for the GitHub community
