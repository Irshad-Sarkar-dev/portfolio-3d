# 🚀 3D Portfolio Website - Setup & Customization Guide

Your modern, interactive 3D portfolio is ready! This guide will help you customize it and get it online.

## ✅ What You Have

A complete 3D portfolio website with:
- **3D Animated Background** - Rotating geometric shapes with floating particles
- **Responsive Design** - Works on all devices
- **Professional Dark Theme** - Cyan & pink neon accents
- **Project Showcase** - Display your work
- **Contact Section** - Links to your social profiles
- **Smooth Animations** - Modern, polished interactions

## 🎯 Step 1: Customize Your Portfolio (Important!)

Edit `app.py` and update the `PORTFOLIO_DATA` dictionary with YOUR information:

```python
PORTFOLIO_DATA = {
    "name": "YOUR NAME",                    # ← Your name
    "title": "YOUR TITLE",                  # ← e.g., "Full Stack Developer"
    "bio": "YOUR BIO",                      # ← About yourself
    "email": "your.email@example.com",      # ← Your email
    "github": "https://github.com/yourname",# ← Your GitHub URL
    "linkedin": "https://linkedin.com/in/yourname",  # ← LinkedIn URL
    "projects": [
        # Your projects here - see examples below
    ],
    "skills": ["Python", "JavaScript", "Three.js"]  # ← Your skills
}
```

### Example: Add Your Question Predictor Project

```python
"projects": [
    {
        "id": 1,
        "title": "Question Pattern Predictor",
        "description": "Analyzes educational content and predicts question patterns using ML.",
        "tags": ["Python", "Machine Learning", "Data Analysis"],
        "github": "https://github.com/yourname/question-predictor",
    },
    {
        "id": 2,
        "title": "PDF Question Extractor",
        "description": "Automatically extracts and analyzes questions from PDF files.",
        "tags": ["Python", "PDF Processing"],
        "github": "https://github.com/yourname/pdf-extractor",
    }
]
```

## 🏃 Step 2: Run Your Website

### Option A: Using the startup script (easiest)
```bash
cd portfolio-3d
./run.sh
```

### Option B: Direct Python command
```bash
cd portfolio-3d
python3 app.py
```

Then open **http://localhost:5000** in your browser.

## 🎨 Step 3: Customize the Look (Optional)

### Change Colors
Edit `static/css/style.css` and modify the CSS variables:

```css
:root {
  --primary: #1a1a2e;    /* Main background */
  --secondary: #16213e;  /* Secondary background */
  --accent: #00d4ff;     /* Cyan accent color */
  --text: #eaeaea;       /* Text color */
}
```

Try these color combinations:
- **Purple & Pink**: `--accent: #ff006e;`
- **Green & Teal**: `--accent: #00ff88;`
- **Orange & Gold**: `--accent: #ff8800;`
- **Blue & Electric**: `--accent: #00aaff;`

### Add More 3D Elements
Edit `static/js/three-setup.js` in the `createGeometricElements()` function:

```javascript
// Example: Add a spinning sphere
const sphereGeometry = new THREE.SphereGeometry(5, 32, 32);
const sphereMaterial = new THREE.MeshPhongMaterial({ color: 0x00d4ff });
const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
sphere.position.set(-20, -5, 0);
scene.add(sphere);
```

### Adjust Animation Speed
In `static/js/three-setup.js`, find the `animate()` function:

```javascript
// These control rotation speed (increase = faster)
scene.userData.cube.rotation.x += 0.005;      // ← Change this
scene.userData.cube.rotation.y += 0.008;      // ← Or this
```

### Modify Particle Effects
In `static/js/three-setup.js`, find `createParticles()`:

```javascript
const particleCount = 100;  // ← Reduce for better performance
```

## 📱 Step 4: Test on Mobile

1. Find your computer's IP address:
   ```bash
   ifconfig | grep "inet " | grep -v 127.0.0.1
   ```

2. On your phone, go to: `http://YOUR_IP:5000`

3. Test scrolling, buttons, and 3D animations

## 🌐 Step 5: Deploy Online

### Deploy to Vercel (Recommended for Flask)
1. Create account at https://vercel.com
2. Install Vercel CLI: `npm i -g vercel`
3. In your project folder: `vercel`
4. Follow the prompts

### Deploy to Replit
1. Go to https://replit.com
2. Click "Create Repl" → "Python"
3. Upload your files
4. Click "Run"

### Deploy to PythonAnywhere
1. Sign up at https://www.pythonanywhere.com
2. Upload your Flask app
3. Configure the WSGI file
4. Get a free subdomain

### Deploy to Heroku (now paid, but simple)
1. Install Heroku CLI
2. Create Procfile:
   ```
   web: python app.py
   ```
3. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

## 🔧 File Structure Reference

```
portfolio-3d/
├── app.py                 ← EDIT THIS! (Your portfolio data)
├── requirements.txt       ← Python dependencies
├── README.md             ← Main documentation
├── run.sh                ← Easy startup script
├── static/
│   ├── css/
│   │   └── style.css     ← Styling & colors
│   └── js/
│       ├── three-setup.js  ← 3D scene & animations
│       └── scroll.js       ← Smooth scrolling
└── templates/
    └── index.html        ← HTML structure
```

## 📝 Quick Edits Cheatsheet

| What to Change | Where to Edit | What to Look For |
|---|---|---|
| Your name, bio, skills | `app.py` | `PORTFOLIO_DATA = {` |
| Add/remove projects | `app.py` | `"projects": [` |
| Colors (accent, background) | `static/css/style.css` | `:root { --accent:` |
| Text colors | `static/css/style.css` | `--text:` |
| 3D shapes rotation speed | `static/js/three-setup.js` | `.rotation.x +=` |
| Particle count | `static/js/three-setup.js` | `const particleCount =` |
| Add new 3D objects | `static/js/three-setup.js` | `createGeometricElements()` |

## 🐛 Troubleshooting

### "Flask app won't start"
- Make sure Flask is installed: `pip3 install Flask`
- Check for syntax errors in `app.py`
- Try: `python3 -m flask run`

### "3D elements not showing"
- Check browser console (F12) for errors
- Three.js CDN might be down, try refreshing
- Some browsers have WebGL disabled

### "Styling looks wrong"
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Try a different browser
- Check CSS file was edited correctly

### "Can't access from phone"
- Make sure phone and computer are on same WiFi
- Use your actual IP, not localhost
- Check firewall isn't blocking port 5000

## 💡 Pro Tips

1. **Add a favicon**: Save a .ico file to `static/favicon.ico` and add to `index.html`:
   ```html
   <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}">
   ```

2. **Add Google Analytics**: Paste code in `templates/index.html` before `</head>`

3. **Custom domain**: Get a domain from Namecheap/GoDaddy, then point to your hosting

4. **Social media cards**: Add Open Graph tags to `index.html` for better sharing

5. **SEO improvement**: Update meta tags in `index.html`

## 🎓 Learning Resources

- **Flask**: https://flask.palletsprojects.com
- **Three.js**: https://threejs.org/docs
- **CSS**: https://developer.mozilla.org/en-US/docs/Web/CSS
- **JavaScript**: https://javascript.info

## 📞 Need Help?

- Check if your code has syntax errors using Python: `python3 -m py_compile app.py`
- Read error messages carefully (they usually tell you what's wrong)
- Test in different browsers
- Check the browser console for JavaScript errors (F12)

## ✨ Next Steps

1. ✅ Customize `app.py` with your info
2. ✅ Run the website locally and test it
3. ✅ Customize colors if you like
4. ✅ Test on your phone
5. ✅ Deploy to the web
6. ✅ Share your portfolio with the world!

---

**Enjoy your beautiful 3D portfolio! 🎉**

Built with Flask, Three.js, and ❤️
