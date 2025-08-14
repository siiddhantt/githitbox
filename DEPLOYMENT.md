# 🚀 Deployment Guide

This guide covers deploying GitHitBox to various free hosting platforms.

## Free Hosting Options (Recommended)

### 1. Railway (⭐ Recommended)
**Why Railway?** Zero-config deployment, generous free tier, automatic HTTPS, and global CDN.

**Free Tier:**
- 500 hours/month execution time
- $5 free credit monthly
- Custom domains supported
- Automatic SSL certificates

**Steps:**
1. Fork this repository to your GitHub account
2. Visit [railway.app](https://railway.app) and sign up
3. Click "Deploy from GitHub repo"
4. Select your forked repository
5. Railway auto-detects the Python app and deploys
6. Your API will be live at: `https://your-app-name.railway.app`

**Usage:**
```markdown
![Profile Views](https://your-app-name.railway.app/badge/your-username)
```

### 2. Render
**Free Tier:**
- 750 hours/month
- Sleeps after 15 minutes of inactivity
- Custom domains on paid plans

**Steps:**
1. Fork this repository
2. Visit [render.com](https://render.com) and create account
3. Create "New Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Environment**: Python 3

### 3. Fly.io
**Free Tier:**
- 160GB-hours/month
- 3 shared-cpu-1x VMs
- Global deployment

**Steps:**
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Sign up: `fly auth signup`
3. In project directory: `fly launch`
4. Deploy: `fly deploy`

### 4. Heroku (Paid)
**Note:** Heroku discontinued free tier, but still good for production

**Steps:**
1. Install Heroku CLI
2. `heroku create your-app-name`
3. `git push heroku main`

## Environment Configuration

For production deployments, you can set these environment variables:

- `DATABASE_URL`: Database connection string (defaults to SQLite)
- `PORT`: Port number (defaults to 8000)

## Database Options

### SQLite (Default)
- Perfect for small to medium traffic
- No setup required
- Data persists in `profile_counter.db` file

### PostgreSQL (Recommended for High Traffic)
```bash
# Set this environment variable in your hosting platform
DATABASE_URL=postgresql://user:password@host:port/database
```

## Custom Domain Setup

### Railway
1. Go to your project settings
2. Add custom domain
3. Update your DNS CNAME record

### Render
1. Available on paid plans
2. Configure in service settings

## Monitoring and Analytics

Your deployed service includes:

- **Health Check**: `GET /health`
- **Global Stats**: `GET /stats` 
- **Individual Stats**: `GET /count/{username}`

## Performance Tips

1. **Database Indexing**: Already optimized with SQLAlchemy indexes
2. **Caching**: Consider adding Redis for high-traffic scenarios
3. **CDN**: Use hosting platform's built-in CDN
4. **Monitoring**: Set up uptime monitoring with UptimeRobot (free)

## Scaling Considerations

### For High Traffic (1M+ hits/day):
1. Switch to PostgreSQL database
2. Add Redis caching
3. Use multiple instances with load balancer
4. Consider paid hosting tiers

### Database Migration:
```python
# Update DATABASE_URL environment variable
DATABASE_URL=postgresql://user:pass@host:port/db
```

## Security Best Practices

1. **Rate Limiting**: Add middleware for rate limiting
2. **CORS**: Configure allowed origins in production
3. **Environment Variables**: Never commit sensitive data
4. **HTTPS**: Always use HTTPS (automatic on most platforms)

## Troubleshooting

### Common Issues:

1. **Build Fails**: Check `requirements.txt` format
2. **Database Issues**: Verify `DATABASE_URL` format
3. **Port Issues**: Ensure your hosting platform can bind to the correct port
4. **Timeout Issues**: Increase health check timeout

### Debug Commands:
```bash
# Check logs (Railway)
railway logs

# Check logs (Render)
# View in dashboard

# Local testing
python main.py
```

## Cost Estimation

### Traffic Estimates:
- **Railway**: ~500K requests/month on free tier
- **Render**: ~750K requests/month (with sleep limitations)
- **Fly.io**: ~1M requests/month

### Upgrade Costs:
- **Railway**: $5/month for more resources
- **Render**: $7/month for always-on service
- **Fly.io**: Pay-as-you-go pricing

## Backup and Recovery

### SQLite Backup:
```bash
# Download database file from hosting platform
# Store backup securely
```

### PostgreSQL Backup:
```bash
# Use hosting platform's backup features
# Or pg_dump for manual backups
```

---

Choose Railway for the easiest deployment experience with the best free tier for this project!
