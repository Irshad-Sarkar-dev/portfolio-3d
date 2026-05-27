from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from functools import wraps

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'jpg', 'jpeg', 'png', 'gif', 'doc', 'docx'}

# Initialize database
db = SQLAlchemy(app)

# ==================== DATABASE MODELS ====================

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    category = db.Column(db.String(100))
    featured_image = db.Column(db.String(255))
    pdf_file = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    published = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'content': self.content,
            'category': self.category,
            'featured_image': self.featured_image,
            'pdf_file': self.pdf_file,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M'),
            'views': self.views,
            'published': self.published
        }


# Portfolio Data
PORTFOLIO_DATA = {
    "name": "Your Name",
    "title": "Developer & Problem Solver",
    "bio": "Building intelligent solutions with code. Passionate about AI/ML, data analysis, and creating seamless user experiences.",
    "email": "your.email@example.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",
    "projects": [
        {
            "id": 1,
            "title": "Question Pattern Predictor",
            "description": "An intelligent system that analyzes educational content and predicts question patterns with probability calculations.",
            "tags": ["Python", "ML", "Data Analysis", "NLP"],
            "github": "https://github.com/yourusername/question-predictor",
        },
        {
            "id": 2,
            "title": "PDF Question Extractor",
            "description": "Extract and analyze questions from PDF documents automatically.",
            "tags": ["Python", "PDF Processing"],
            "github": "https://github.com/yourusername/pdf-extractor",
        }
    ],
    "skills": ["Python", "JavaScript", "Machine Learning", "Data Analysis", "Web Development", "Flask", "Three.js"]
}

# ==================== UTILITY FUNCTIONS ====================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            flash('Please log in first', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function


# ==================== PUBLIC ROUTES ====================

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/tutorials')
def tutorials():
    articles = Article.query.filter_by(published=True).order_by(Article.created_at.desc()).all()
    return render_template('tutorials.html', articles=articles, data=PORTFOLIO_DATA)


@app.route('/tutorial/<int:article_id>')
def tutorial_detail(article_id):
    article = Article.query.get_or_404(article_id)
    if not article.published:
        return redirect(url_for('tutorials'))
    
    # Increment views
    article.views += 1
    db.session.commit()
    
    return render_template('tutorial_detail.html', article=article, data=PORTFOLIO_DATA)


@app.route('/api/portfolio')
def api_portfolio():
    return jsonify(PORTFOLIO_DATA)


@app.route('/api/articles')
def api_articles():
    articles = Article.query.filter_by(published=True).order_by(Article.created_at.desc()).all()
    return jsonify([article.to_dict() for article in articles])


# ==================== ADMIN ROUTES ====================

@app.route('/admin')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    
    stats = {
        'total_articles': Article.query.count(),
        'published_articles': Article.query.filter_by(published=True).count(),
        'total_views': sum(a.views for a in Article.query.all())
    }
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('admin/dashboard.html', articles=articles, stats=stats)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username
            flash(f'Welcome {username}!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('admin/login.html')


@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('admin_login'))


@app.route('/admin/create', methods=['GET', 'POST'])
@login_required
def admin_create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        content = request.form.get('content')
        category = request.form.get('category', 'General')
        
        article = Article(
            title=title,
            description=description,
            content=content,
            category=category
        )
        
        # Handle featured image upload
        if 'featured_image' in request.files:
            file = request.files['featured_image']
            if file and allowed_file(file.filename):
                filename = secure_filename(f"img_{datetime.utcnow().timestamp()}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'images', filename))
                article.featured_image = f"uploads/images/{filename}"
        
        # Handle PDF upload
        if 'pdf_file' in request.files:
            file = request.files['pdf_file']
            if file and allowed_file(file.filename):
                filename = secure_filename(f"pdf_{datetime.utcnow().timestamp()}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'articles', filename))
                article.pdf_file = f"uploads/articles/{filename}"
        
        db.session.add(article)
        db.session.commit()
        
        flash(f'Article "{title}" created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/create_article.html')


@app.route('/admin/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.description = request.form.get('description')
        article.content = request.form.get('content')
        article.category = request.form.get('category', 'General')
        article.published = request.form.get('published') == 'on'
        
        # Handle featured image upload
        if 'featured_image' in request.files:
            file = request.files['featured_image']
            if file and allowed_file(file.filename):
                filename = secure_filename(f"img_{datetime.utcnow().timestamp()}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'images', filename))
                article.featured_image = f"uploads/images/{filename}"
        
        # Handle PDF upload
        if 'pdf_file' in request.files:
            file = request.files['pdf_file']
            if file and allowed_file(file.filename):
                filename = secure_filename(f"pdf_{datetime.utcnow().timestamp()}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'articles', filename))
                article.pdf_file = f"uploads/articles/{filename}"
        
        db.session.commit()
        
        flash(f'Article "{article.title}" updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/edit_article.html', article=article)


@app.route('/admin/delete/<int:article_id>', methods=['POST'])
@login_required
def admin_delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    title = article.title
    db.session.delete(article)
    db.session.commit()
    
    flash(f'Article "{title}" deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/toggle/<int:article_id>', methods=['POST'])
@login_required
def admin_toggle_publish(article_id):
    article = Article.query.get_or_404(article_id)
    article.published = not article.published
    db.session.commit()
    
    status = 'published' if article.published else 'unpublished'
    flash(f'Article "{article.title}" {status}!', 'success')
    return redirect(url_for('admin_dashboard'))


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


# ==================== MAIN ====================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Create default admin if not exists
        if not Admin.query.filter_by(username='Irshad').first():
            admin = Admin(username='Irshad')
            admin.set_password('admin123')  # CHANGE THIS!
            db.session.add(admin)
            db.session.commit()
            print("✅ Default admin created: username='Irshad', password='admin123'")
            print("⚠️  IMPORTANT: Change the default password in production!")
    
    print("🚀 Portfolio Website with Admin Panel running at http://localhost:5000")
    print("📝 Admin Panel at http://localhost:5000/admin/login")
    app.run(debug=True, host='localhost', port=5000)
