# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 82

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

82 Часть I. Создание архитектуры для поддержки моделирования предметной области
 # шаг 3 с императивным ядром: применить операции ввода-вывода данных
 for action, *paths in actions:
 if action == 'copy':
 shutil.copyfile(*paths)
 if action == 'move':
 shutil.move(*paths)
 if action == 'delete':
 os.remove(paths[0])
 Это первая функция, которую мы перерабатываем, read_paths_and_
hashes() . Она изолирует часть приложения, связанную с операциями
ввода-вывода.
 Здесь мы выкраиваем функциональное ядро, бизнес-логику .
Код для построения словаря путей и хешей теперь пишется тривиально.
Функция, которая просто выполняет операции ввода-вывода (sync.py)
def read_paths_and_hashes(root):
 hashes = {}
 for folder, _, files in os.walk(root):
 for fn in files:
 hashes[hash_file(Path(folder) / fn)] = fn
 return hashes
Функция determine_actions() будет ядром бизнес-логики, которая говорит:
«Что теперь следует скопировать/переместить/удалить, получив эти два
множества хешей и имен файлов?» Она берет простые структуры данных
и возвращает простые структуры данных.
Функция, которая просто выполняет бизнес-логику (sync.py)
def determine_actions(src_hashes, dst_hashes, src_folder, dst_folder):
 for sha, filename in src_hashes.items():
 if sha not in dst_hashes:
 sourcepath = Path(src_folder) / filename
 destpath = Path(dst_folder) / filename
 yield 'copy', ёsourcepath, destpath
 elif dst_hashes[sha] != filename:
 olddestpath = Path(dst_folder) / dst_hashes[sha]
 newdestpath = Path(dst_folder) / filename
 yield 'move', olddestpath, newdestpath
 for sha, filename in dst_hashes.items():
 if sha not in src_hashes:
 yield 'delete', dst_folder / filename
