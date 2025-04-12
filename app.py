<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>fhost</title>
    <style>
        :root {
            --primary-color: #0095ff;
            --primary-dark: #007acc;
            --secondary-color: #bb86fc;
            --text-color: #e1e1e1;
            --bg-color: #121212;
            --card-bg: #1e1e1e;
            --card-header-bg: #252525;
            --border-color: #333;
            --path-bg: #252525;
            --path-border: #007acc;
            --empty-color: #666;
            --border-radius: 8px;
            --shadow: 0 4px 12px rgba(0,0,0,0.2);
            --transition: all 0.3s ease;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            font-size: 16px;
            line-height: 1.6;
        }
        
        /* Полоса прокрутки */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1a1a;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #444;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #666;
        }
        
        .app {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        
        .project-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .stat-card {
            background-color: var(--card-bg);
            border-radius: var(--border-radius);
            padding: 15px;
            box-shadow: var(--shadow);
            text-align: center;
            border-top: 3px solid var(--primary-color);
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 500;
            margin-bottom: 5px;
            color: var(--primary-color);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #999;
        }
        
        h1 {
            font-size: 1.6rem;
            font-weight: 500;
            margin: 0 0 20px 0;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        h1 svg {
            color: var(--primary-color);
        }
        
        main {
            flex: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px 20px;
            width: 100%;
        }
        
        .grid-layout {
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
        }
        
        .card {
            background-color: var(--card-bg);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: var(--transition);
            border: 1px solid var(--border-color);
        }
        
        .card:hover {
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }
        
        .card-header {
            padding: 18px 24px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: var(--card-header-bg);
        }
        
        .card-title {
            font-size: 1.2rem;
            font-weight: 500;
            color: var(--text-color);
            margin: 0;
        }
        
        .card-body {
            padding: 24px;
        }
        
        .path-info {
            background-color: var(--path-bg);
            padding: 14px 18px;
            border-radius: var(--border-radius);
            font-family: 'Consolas', 'Monaco', monospace;
            word-break: break-all;
            font-size: 0.9rem;
            color: var(--primary-color);
            border-left: 4px solid var(--path-border);
            margin-bottom: 20px;
        }
        
        .back-button {
            display: inline-flex;
            align-items: center;
            background-color: transparent;
            border: 1px solid var(--primary-color);
            padding: 8px 16px;
            border-radius: var(--border-radius);
            text-decoration: none;
            color: var(--primary-color);
            font-weight: 500;
            transition: var(--transition);
            margin-bottom: 20px;
        }
        
        .back-button:hover {
            background-color: var(--primary-color);
            color: white;
        }
        
        .back-button svg {
            margin-right: 8px;
        }
        
        .file-list {
            list-style-type: none;
        }
        
        .file-item {
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }
        
        .file-item:last-child {
            border-bottom: none;
        }
        
        .file-item:hover {
            background-color: rgba(0, 149, 255, 0.1);
        }
        
        .file-link {
            padding: 14px 16px;
            text-decoration: none;
            color: var(--text-color);
            display: flex;
            align-items: center;
        }
        
        .file-icon {
            margin-right: 12px;
            color: var(--primary-color);
            font-size: 1.2rem;
        }
        
        .directory-icon {
            color: var(--secondary-color);
        }
        
        .file-name {
            word-break: break-all;
            flex-grow: 1;
        }
        
        .file-size {
            color: #888;
            font-size: 0.85em;
            margin-left: 5px;
        }
        
        .directory-name {
            font-weight: 500;
            color: var(--secondary-color);
        }
        
        .upload-form {
            margin-top: 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .file-input-wrapper {
            position: relative;
            margin-bottom: 20px;
            border: 2px dashed #444;
            border-radius: var(--border-radius);
            padding: 30px 20px;
            text-align: center;
            transition: var(--transition);
            cursor: pointer;
            background-color: rgba(0, 0, 0, 0.2);
        }
        
        .file-input-wrapper:hover {
            border-color: var(--primary-color);
            background-color: rgba(0, 149, 255, 0.05);
        }
        
        .file-input-wrapper input[type="file"] {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            opacity: 0;
            cursor: pointer;
        }
        
        .file-input-message {
            color: #aaa;
            font-size: 1rem;
        }
        
        .file-input-icon {
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 10px;
        }
        
        .btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: var(--border-radius);
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            transition: var(--transition);
            text-align: center;
            display: inline-block;
            text-transform: none;
        }
        
        .btn:hover {
            background-color: var(--primary-dark);
        }
        
        .btn-block {
            display: block;
            width: 100%;
        }
        
        .empty-dir {
            padding: 40px 0;
            text-align: center;
            color: var(--empty-color);
        }
        
        .empty-dir-icon {
            font-size: 3rem;
            margin-bottom: 10px;
            color: #444;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid var(--border-color);
            background-color: var(--card-bg);
        }
        
        /* Адаптивный дизайн */
        @media (min-width: 768px) {
            h1 {
                font-size: 1.8rem;
            }
            
            .grid-layout {
                grid-template-columns: 2fr 1fr;
            }
            
            .card-header {
                padding: 20px 30px;
            }
            
            .card-body {
                padding: 30px;
            }
        }
        
        @media (max-width: 767px) {
            .header-content {
                flex-direction: column;
                text-align: center;
                gap: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="app">
        <main>
            <h1>
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M2 9V5c0-1.1.9-2 2-2h3.93a2 2 0 0 1 1.66.9l.82 1.2a2 2 0 0 0 1.66.9H20a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-1"/>
                    <path d="M2 13h10"/>
                    <path d="m9 16 3-3-3-3"/>
                </svg>
                fhost
            </h1>
            
            <div class="project-stats">
                <div class="stat-card">
                    <div class="stat-value">{{ directories|length }}</div>
                    <div class="stat-label">Директории</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{{ files|length }}</div>
                    <div class="stat-label">Файлы</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{{ total_size }}</div>
                    <div class="stat-label">Размер</div>
                </div>
            </div>
            
            <div class="path-info">
                Текущий путь: {{ path }}
            </div>
            
            {% if path != '.' %}
            <a href="/" class="back-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M19 12H5M12 19l-7-7 7-7"/>
                </svg>
                На главную
            </a>
            {% endif %}
            
            <div class="grid-layout">
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Содержимое директории</h2>
                    </div>
                    <div class="card-body">
                        <ul class="file-list">
                            {% for directory in directories %}
                                <li class="file-item">
                                    <a href="{{ url_for('browse', subpath=path + '/' + directory if path != '.' else directory) }}" class="file-link">
                                        <span class="file-icon directory-icon">📁</span>
                                        <span class="file-name directory-name">{{ directory }}/</span>
                                    </a>
                                </li>
                            {% endfor %}
                            
                            {% for file in files %}
                                <li class="file-item">
                                    <a href="{{ url_for('browse', subpath=path + '/' + file if path != '.' else file) }}" class="file-link">
                                        <span class="file-icon">📄</span>
                                        <span class="file-name">{{ file }} <span class="file-size">({{ file_sizes[file] }})</span></span>
                                    </a>
                                </li>
                            {% endfor %}
                            
                            {% if not files and not directories %}
                                <div class="empty-dir">
                                    <div class="empty-dir-icon">📂</div>
                                    <p>Директория пуста</p>
                                </div>
                            {% endif %}
                        </ul>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Загрузить файл</h2>
                    </div>
                    <div class="card-body">
                        <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data" class="upload-form">
                            <input type="hidden" name="path" value="{{ path }}">
                            
                            <div class="file-input-wrapper">
                                <div class="file-input-icon">📤</div>
                                <div class="file-input-message">Нажмите или перетащите файл</div>
                                <input type="file" name="file" required>
                            </div>
                            
                            <button type="submit" class="btn btn-block">Загрузить</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
        
        <footer>
            &copy; {{ current_year }} fhost | Запущен на {{ platform }}
        </footer>
        
        <script>
            // Обработчик для отображения имени и размера выбранного файла
            document.addEventListener('DOMContentLoaded', function() {
                // Добавляем обработчик для input file
                const fileInput = document.querySelector('input[type="file"]');
                const fileMessage = document.querySelector('.file-input-message');
                const originalMessage = fileMessage.textContent;
                
                fileInput.addEventListener('change', function() {
                    if (this.files.length) {
                        const file = this.files[0];
                        fileMessage.textContent = file.name + ' (' + formatFileSize(file.size) + ')';
                    } else {
                        fileMessage.textContent = originalMessage;
                    }
                });
                
                function formatFileSize(bytes) {
                    if (bytes >= 1024 * 1024) {
                        return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
                    } else if (bytes >= 1024) {
                        return (bytes / 1024).toFixed(1) + ' KB';
                    } else {
                        return bytes + ' bytes';
                    }
                }
            });
        </script>
    </div>
</body>
</html>
