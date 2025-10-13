# Explore The Book - Hugo Site

A containerized Hugo development environment for exploring books and literature.

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed and running
- WSL 2 enabled (Windows)

### Development Commands

```bash
# Start the development server (runs at http://localhost:1313)
docker-compose up

# Stop the development server
docker-compose down

# Create a new blog post
docker-compose run --rm hugo hugo new content posts/your-post-name.md

# Build the site for production
docker-compose run --rm hugo hugo --minify

# Access the container shell for advanced operations
docker-compose run --rm hugo bash
```

## 📁 Project Structure

```
explorethebook/
├── content/          # Your content (posts, pages)
├── themes/           # Hugo themes (PaperMod installed)
├── static/           # Static assets (images, CSS, JS)
├── layouts/          # Custom layout templates
├── data/             # Data files
├── assets/           # Pipeline assets
├── hugo.toml         # Hugo configuration
├── Dockerfile        # Container definition
└── docker-compose.yml # Development orchestration
```

## 🎨 Theme

This site uses the **PaperMod** theme, which provides:
- Clean, modern design
- Dark/light mode toggle
- Search functionality
- SEO optimization
- Mobile-responsive layout

## ✍️ Creating Content

1. Create a new post:
   ```bash
   docker-compose run --rm hugo hugo new content posts/my-new-post.md
   ```

2. Edit the created file in `content/posts/`
3. Set `draft: false` in the front matter to publish
4. The site will auto-reload with your changes

## 🔧 Configuration

Edit `hugo.toml` to customize:
- Site title and description
- Theme settings
- Menu structure
- Social links
- SEO settings

## 🌐 Access Your Site

- **Development**: http://localhost:1313
- **Container**: The site runs inside a Docker container with Hugo 0.146.0
- **Live Reload**: Changes to content and configuration auto-refresh the browser

## 📦 Benefits of This Setup

✅ **Isolated Environment**: No need to install Hugo on your Windows machine  
✅ **Consistent**: Same Hugo version across all environments  
✅ **Clean**: No pollution of your local system  
✅ **Portable**: Easy to share and deploy  
✅ **Version Controlled**: All configuration is in git  

Happy writing! 📚✨