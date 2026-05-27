# 🛡️ Admin Panel Guide

Your portfolio now includes a complete **Admin Panel** for managing articles and tutorials!

## 🚀 Quick Start

### 1. Login to Admin Panel
- Go to: `http://localhost:5000/admin/login`
- **Username**: `Irshad`
- **Password**: `admin123`

⚠️ **IMPORTANT**: Change the default password in production!

### 2. Admin Dashboard
After login, you'll see:
- 📊 Statistics (total articles, published count, views)
- 📝 All your articles in a table
- ✅ Quick actions: Edit, Publish/Unpublish, Delete

### 3. Create New Article
1. Click **"+ New Article"** button
2. Fill in the form:
   - **Title** (required) - Article headline
   - **Category** - Python, Web Development, Machine Learning, etc.
   - **Description** - Short summary (shows in article list)
   - **Content** - Full article text (supports HTML)
   - **Featured Image** - Thumbnail image (JPG, PNG)
   - **PDF File** - Optional attachment for download
3. Click **"Create Article"**

### 4. Edit Article
1. Click **"Edit"** button on any article
2. Modify the fields
3. Optionally upload new images/PDFs
4. Toggle "Published" checkbox to show/hide from public
5. Click **"Update Article"**

### 5. Manage Articles
- **Publish/Unpublish**: Toggle visibility to public
- **Edit**: Modify article content
- **Delete**: Remove article (cannot be undone)

## 📚 Article Features

### What You Can Upload
- **Text**: Full article content with formatting
- **Images**: Featured image (displayed at top of article)
- **PDFs**: Readers can download supporting files
- **Multiple files**: One image + one PDF per article

### Supported File Types
- Images: JPG, JPEG, PNG, GIF
- Documents: PDF, TXT, DOC, DOCX
- Max file size: 50MB

### Content Support
- Plain text
- HTML formatting
- Headings, paragraphs, lists
- Links and images in content

## 🔐 Security

### Change Admin Password
Edit `app.py` and find this section:
```python
if not Admin.query.filter_by(username='Irshad').first():
    admin = Admin(username='Irshad')
    admin.set_password('admin123')  # ← CHANGE THIS!
```

Replace `admin123` with a strong password.

Then delete `portfolio.db` file to reset the database with new credentials.

### Add More Admin Users
Edit `app.py` and add after line 383:
```python
new_admin = Admin(username='newusername')
new_admin.set_password('newpassword')
db.session.add(new_admin)
db.session.commit()
```

## 📖 Public Website

### Tutorials Page
- Visit: `http://localhost:5000/tutorials`
- Shows all published articles
- Click any article to read full content
- Views counter updates automatically

### Article Detail Page
- Each article has its own page
- Shows featured image, content, attachments
- Download PDF or view images
- Back link to tutorials list

## 💾 Database

### Where Data is Stored
- **File**: `portfolio.db` (SQLite database)
- **Location**: `/Users/sircar/portfolio-3d/portfolio.db`
- **Automatic**: Created on first run

### Backup Your Data
```bash
cp portfolio.db portfolio.db.backup
```

### Restore from Backup
```bash
cp portfolio.db.backup portfolio.db
```

## 🐛 Troubleshooting

### Can't Login
1. Make sure Flask is running (`python3 app.py`)
2. Check username and password spelling
3. Default: username="Irshad", password="admin123"

### Articles Not Showing
1. Make sure article is "Published" (toggle in dashboard)
2. Try refreshing the page
3. Check if article title and description are not empty

### File Upload Failed
1. Check file size (max 50MB)
2. Check file type (jpg, png, pdf, etc.)
3. Make sure `uploads/` folder exists
4. Check file permissions

### Database Error
1. Delete `portfolio.db` file
2. Restart Flask (`python3 app.py`)
3. Database will be recreated automatically

## 📊 Statistics

The dashboard shows:
- **Total Articles**: All articles (published + draft)
- **Published**: Only articles set to "published"
- **Total Views**: Sum of all article views
- **Views Counter**: Increases each time someone reads an article

## 🎨 Article Tips

### For Better Articles
1. **Good titles**: Clear, descriptive, engaging
2. **Good descriptions**: 1-2 sentences, hooks readers
3. **Good images**: High quality, relevant to content
4. **Good content**: Well organized, easy to read
5. **Categories**: Use consistent category names

### Markdown-like Content
Use basic HTML in content field:
```html
<h2>Heading 2</h2>
<p>Paragraph text</p>
<ul>
  <li>List item 1</li>
  <li>List item 2</li>
</ul>
<a href="https://example.com">Link</a>
```

## 🚀 Deploy with Articles

When deploying to production:
1. Change admin password
2. Update `SECRET_KEY` in app.py (change the string)
3. Set `DEBUG=False` for production
4. Back up database before deploying
5. Use environment variables for sensitive data

## 📝 Workflow Example

**Day 1**: Create tutorial article
1. Login to `/admin/login`
2. Click "New Article"
3. Fill title, description, category, content
4. Upload feature image
5. Publish article
6. Share link to tutorials page

**Day 2**: Update article
1. Click "Edit" on article
2. Fix typos, add info
3. Update image if needed
4. Save changes

**Day 3**: Create next article
1. Repeat process
2. Viewers can see all published articles
3. View counts automatically track

## ✨ Features Summary

✅ Create, Read, Update, Delete articles
✅ Publish/Unpublish articles
✅ Upload images and PDFs
✅ View counts per article
✅ Category organization
✅ Search by category
✅ Admin authentication
✅ Beautiful dashboard
✅ Responsive design
✅ No coding needed

## 🎯 Next Steps

1. ✅ Login to admin panel
2. ✅ Create your first article
3. ✅ View it on tutorials page
4. ✅ Share tutorials link with others
5. ✅ Keep adding more content

---

**Happy publishing!** 📚✨

For more help, check the main documentation files.
