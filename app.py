from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'html', 'css', 'js'}

# Создаем папку для загрузок, если она не существует
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_directory_size(path):
    """Рассчитывает общий размер файлов в директории"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp) and os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size_bytes):
    """Форматирует размер в байтах в удобочитаемый формат"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.1f} MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.1f} GB"

@app.route('/')
def index():
    # Получаем список файлов в корневой директории
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    directories = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    
    # Получаем размер текущей директории
    dir_size = get_directory_size('.')
    formatted_size = format_size(dir_size)
    
    # Получаем размеры файлов
    file_sizes = {}
    for file in files:
        try:
            file_sizes[file] = format_size(os.path.getsize(file))
        except:
            file_sizes[file] = "0 B"
    
    current_year = datetime.datetime.now().year
    platform = os.name.upper() if os.name else "Termux"
    
    return render_template('index.html', 
                          files=files, 
                          directories=directories, 
                          path='.',
                          total_size=formatted_size,
                          file_sizes=file_sizes,
                          current_year=current_year,
                          platform=platform)

@app.route('/browse/<path:subpath>')
def browse(subpath):
    # Проверка на безопасность пути
    if '..' in subpath:
        return "Доступ запрещен", 403
    
    full_path = os.path.join('.', subpath)
    if os.path.isfile(full_path):
        return send_from_directory('.', subpath)
    
    files = [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]
    directories = [d for d in os.listdir(full_path) if os.path.isdir(os.path.join(full_path, d)) and not d.startswith('.')]
    
    # Получаем размер текущей директории
    dir_size = get_directory_size(full_path)
    formatted_size = format_size(dir_size)
    
    # Получаем размеры файлов
    file_sizes = {}
    for file in files:
        try:
            file_path = os.path.join(full_path, file)
            file_sizes[file] = format_size(os.path.getsize(file_path))
        except:
            file_sizes[file] = "0 B"
    
    current_year = datetime.datetime.now().year
    platform = os.name.upper() if os.name else "Termux"
    
    return render_template('index.html', 
                          files=files, 
                          directories=directories, 
                          path=subpath,
                          total_size=formatted_size,
                          file_sizes=file_sizes,
                          current_year=current_year,
                          platform=platform)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Проверяем, был ли файл отправлен
    if 'file' not in request.files:
        return redirect(request.referrer or url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.referrer or url_for('index'))
    
    if file and allowed_file(file.filename):
        # Определяем директорию для загрузки в зависимости от типа файла
        filename = file.filename
        file_extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
        
        # Если это HTML-файл, всегда загружаем в UPLOAD_FOLDER
        if file_extension == 'html':
            upload_path = app.config['UPLOAD_FOLDER']
        else:
            # Для других типов файлов используем указанный путь
            upload_path = request.form.get('path', app.config['UPLOAD_FOLDER'])
            # Проверка на безопасность пути
            if '..' in upload_path:
                return "Доступ запрещен", 403
        
        # Создаем директорию, если не существует
        os.makedirs(upload_path, exist_ok=True)
        
        # Сохраняем файл
        filepath = os.path.join(upload_path, file.filename)
        file.save(filepath)
        
        # Перенаправляем обратно
        return redirect(request.referrer or url_for('index'))
    
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
