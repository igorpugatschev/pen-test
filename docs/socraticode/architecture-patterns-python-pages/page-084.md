# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 84

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

84 Часть I. Создание архитектуры для поддержки моделирования предметной области
тивизируют все систему целиком, но подделывают операции ввода-вывода
как бы от края до края.
Явные зависимости (sync.py)
def sync(reader, filesystem, source_root, dest_root): 
 source_hashes = reader(source_root) 
 dest_hashes = reader(dest_root)
 for sha, filename in src_hashes.items():
 if sha not in dest_hashes:
 sourcepath = source_root / filename
 destpath = dest_root / filename
 filesystem.copy(destpath, sourcepath) 
 elif dest_hashes[sha] != filename:
 olddestpath = dest_root / dest_hashes[sha]
 newdestpath = dest_root / filename
 filesystem.move(olddestpath, newdestpath)
 for sha, filename in dst_hashes.items():
 if sha not in source_hashes:
 filesystem.delete(dest_root/filename)
 Верхнеуровневая функция теперь выставляет наружу две новые за-
висимости: читателя reader и файловую систему filesystem.
 Вызываем reader, чтобы создать словарь с файлами.
 Вызываем filesystem, чтобы применить обнаруженные изменения.
Хотя мы используем внедрение зависимостей, определять абстрактный
базовый класс или какой-либо явный интерфейс не нужно. В этой книге
мы часто показываем абстрактные базовые классы: так мы надеемся
объяснить, что такое абстракция. Но использовать их необязательно.
Динамическая природа языка Python означает, что всегда можно по -
ложиться на утиную типизацию.
Т есты с внедрением зависимостей
class FakeFileSystem(list): 
 def copy(self, src, dest): 
 self.append(('COPY', src, dest))
