# 3D Portfolio Website 🚀

A modern, interactive 3D portfolio website built with **Flask** and **Three.js**. Showcase your projects with stunning 3D animations and smooth interactions.

## Features ✨

- **3D Background**: Animated 3D elements (cubes, octahedrons, torus) with floating particles
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Modern UI**: Professional dark theme with cyan/pink neon accents
- **Smooth Navigation**: Smooth scrolling between sections
- **Project Showcase**: Display your projects with tags and links
- **Contact Section**: Easy links to email, GitHub, and LinkedIn
- **Performance Optimized**: Efficient rendering with Three.js

## Quick Start 🎯

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Customize Your Portfolio
Edit `app.py` and update the `PORTFOLIO_DATA` dictionary:
```python
PORTFOLIO_DATA = {
    "name": "Your Name",
    "title": "Your Title",
    "bio": "Your bio here...",
    "email": "your.email@example.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",
    "projects": [
        # Add your projects here
    ],
    "skills": ["Your", "Skills", "Here"]
}
```

### 3. Run the Website
```bash
python app.py
```

Open your browser and go to **http://localhost:5000**

## File Structure 📁

```
portfolio-3d/
├── app.py                          # Flask application (customize here!)
├── requirements.txt                # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css              # Main styling
│   └── js/
│       ├── three-setup.js         # 3D scene initialization
│       └── scroll.js              # Smooth scrolling
├── templates/
│   └── index.html                 # HTML template
└── README.md                       # This file
```

## Customization Guide 🎨

### Change Colors
Edit `static/css/style.css` - modify CSS variables:
```css
:root {
  --primary: #1a1a2e;    /* Background */
  --accent: #00d4ff;     /* Cyan accent */
  --secondary: #16213e;  /* Secondary bg */
}
```

### Add More Projects
Add entries to `PORTFOLIO_DATA['projects']` in `app.py`:
```python
{
    "id": 3,
    "title": "Your Project",
    "description": "Project description...",
    "tags": ["Tag1", "Tag2"],
    "github": "https://github.com/yourusername/project",
}
```

### Modify 3D Elements
Edit `static/js/three-setup.js`:
- Change rotation speeds
- Add/remove 3D objects
- Adjust lighting and colors
- Modify particle effects

### Add New Sections
1. Add HTML in `templates/index.html`
2. Add CSS in `static/css/style.css`
3. Update navigation in `<nav>`

## Deployment 🌐

### Deploy to Vercel
```bash
pip freeze > requirements.txt
vercel --prod
```

### Deploy to Heroku
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Deploy to PythonAnywhere
1. Upload files to PythonAnywhere
2. Configure Flask app
3. Set `FLASK_ENV=production`

## Browser Support 🌍

- Chrome/Edge 60+
- Firefox 55+
- Safari 12+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Tips 💡

- **Performance**: Reduce particle count in `createParticles()` for slower devices
- **Mobile**: Test on mobile before deploying
- **SEO**: Update meta tags in `index.html`
- **Analytics**: Add Google Analytics to track visitors

## Technologies Used 🛠️

- **Flask** - Python web framework
- **Three.js** - WebGL 3D library
- **CSS3** - Modern styling
- **JavaScript** - Interactivity
- **Jinja2** - Template engine

## License 📄

Feel free to use this template for your portfolio!

## Need Help? 🤝

- Check Flask docs: https://flask.palletsprojects.com
- Three.js docs: https://threejs.org/docs
- CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS

---

**Made with ❤️ for developers**
