# 🚀 DEPLOYMENT GUIDE

## Local Development

### Quick Start

```bash
pip install -r requirements.txt
python main.py
```

The bot will start polling and handle messages immediately.

---

## Cloud Deployment Options

### Option 1: DigitalOcean (Recommended - $3-5/month)

#### Setup

1. Create a new Droplet (Ubuntu 20.04)
2. SSH into the server
3. Install Python and dependencies:

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip git
```

4. Clone your project:

```bash
git clone https://github.com/yourusername/telegram-service-bot.git
cd telegram-service-bot
```

5. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Run bot in background using `screen` or `systemd`

#### Option A: Using Screen (Quick)

```bash
screen -S bot
python main.py
# Press Ctrl+A+D to detach
```

To reattach:

```bash
screen -r bot
```

#### Option B: Using Systemd (Persistent)

Create `/etc/systemd/system/coach-bot.service`:

```ini
[Unit]
Description=Telegram Coach Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/telegram-service-bot
ExecStart=/root/telegram-service-bot/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable coach-bot
sudo systemctl start coach-bot

# Check status
sudo systemctl status coach-bot

# View logs
sudo journalctl -u coach-bot -f
```

---

### Option 2: Docker on Any VPS

#### Prerequisites

- Docker installed

#### Deploy

```bash
# Build image
docker build -t coach-bot .

# Run container
docker run -d \
  --name coach-bot \
  --restart unless-stopped \
  coach-bot

# View logs
docker logs -f coach-bot

# Stop/restart
docker stop coach-bot
docker start coach-bot
```

#### Using Docker Compose (Recommended)

```bash
# Update config in docker-compose.yml first
docker-compose up -d

# View logs
docker-compose logs -f coach-bot

# Stop
docker-compose down
```

---

### Option 3: PythonAnywhere (Free Tier)

1. Create account at https://www.pythonanywhere.com
2. Upload files via their file manager
3. Create a console
4. Install requirements:

```bash
pip install -r requirements.txt
```

5. Create a scheduled task or long-running process
6. Run `python main.py`

---

### Option 4: AWS Lambda + API Gateway

For serverless deployment (advanced):

- Requires webhook setup instead of polling
- More complex but scales better
- Use `aiogram.web.* ` for webhook mode

---

## Monitoring & Maintenance

### Monitor Bot Status

```bash
# Check if process is running
ps aux | grep main.py

# Check disk space
df -h

# Check memory usage
free -h

# View system logs
tail -f /var/log/syslog
```

### Backup Configuration

```bash
# Backup config.py
cp config.py config.py.backup

# You can also version control it
git add config.py
git commit -m "Updated config"
```

### Update Bot Code

```bash
# Pull latest changes
git pull origin main

# Restart service
sudo systemctl restart coach-bot
# or
docker-compose restart coach-bot
```

---

## Environment Variables (for .env file)

If using `main_env.py`:

```bash
BOT_TOKEN=your_token
ADMIN_CHAT_ID=your_id
BOOKING_URL=https://calendly.com/...
WEBSITE_URL=https://your-site.com
PAYMENT_URL=https://your-site.com/pricing
WHATSAPP_URL=https://wa.me/...
EMAIL=your@email.com
```

---

## SSL Certificate (for HTTPS webhook, if needed)

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --standalone -d your-domain.com
```

---

## Troubleshooting Deployment

### Bot not responding

1. Check logs: `docker logs coach-bot` or `sudo journalctl -u coach-bot -f`
2. Verify token is correct
3. Check internet connection: `ping 8.8.8.8`
4. Restart bot service

### Memory leak

1. Monitor with: `docker stats coach-bot`
2. Restart bot weekly: `sudo systemctl restart coach-bot`
3. Check for infinite loops in code

### Port conflicts

- Polling bot doesn't use ports
- If using webhook, ensure port 8080+ is available

### File permissions

```bash
chmod +x main.py
chmod 755 -R /app/
```

---

## Cost Estimation

| Provider       | Cost/Month      | Best For                  |
| -------------- | --------------- | ------------------------- |
| DigitalOcean   | $3-6            | Production, Recommended   |
| Linode         | $3-6            | Production, Good uptime   |
| AWS            | $1-2            | High volume, need scaling |
| PythonAnywhere | Free            | Testing, learning         |
| Heroku         | Free tier ended | -                         |

---

## Example: Full DigitalOcean Setup (5min)

```bash
# 1. SSH into your droplet
ssh root@your.ip.address

# 2. Install Python
apt-get update && apt-get install -y python3-pip git

# 3. Clone and setup
git clone <your-repo>
cd telegram-service-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Create systemd service
cat > /etc/systemd/system/coach-bot.service << EOF
[Unit]
Description=Telegram Coach Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/venv/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# 5. Enable and start
systemctl daemon-reload
systemctl enable coach-bot
systemctl start coach-bot

# 6. Verify
systemctl status coach-bot
```

Done! Bot is now running 24/7. 🎉

---

## Scaling (if bot gets popular)

Currently designed for single-user polling. To scale:

1. **Multiple instances:**

   - Use load balancer
   - Run multiple bot processes
   - Share state in Redis/PostgreSQL

2. **Database:**

   - Replace in-memory state with real DB
   - Switch from `database.py` to SQLAlchemy

3. **Caching:**

   - Add Redis for session caching
   - Reduce API calls

4. **Monitoring:**
   - Add Prometheus metrics
   - Use DataDog or similar for alerting

---

## Security Best Practices

1. **Never commit token to git:**

   ```bash
   # Use .env or environment variables
   git checkout .env
   ```

2. **Use secrets management:**

   - AWS Secrets Manager
   - Heroku Config Vars
   - Docker secrets

3. **Regular backups:**

   ```bash
   tar -czf config-backup-$(date +%Y%m%d).tar.gz config.py
   ```

4. **Monitor logs for suspicious activity:**
   ```bash
   tail -f /var/log/coach-bot.log | grep -i error
   ```

---

**Questions? Check README.md or QUICK_START.md**
