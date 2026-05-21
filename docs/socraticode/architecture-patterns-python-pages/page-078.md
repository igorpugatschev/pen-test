# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 78

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

78 Часть I. Создание архитектуры для поддержки моделирования предметной области
Фантастика! У нас появилось немного кода, и он выглядит нормально,
но прежде, чем мы выполним его, возможно, следует его протестировать.
И как же такое тестировать?
Немного сквозных тестов (test_sync.py)
def test_when_a_file_exists_in_the_source_but_not_the_destination():
 try:
 source = tempfile.mkdtemp()
 dest = tempfile.mkdtemp()
 content = "Я — очень полезный файл"
 (Path(source) / 'my-file').write_text(content)
 sync(source, dest)
 expected_path = Path(dest) / 'my-file'
 assert expected_path.exists()
 assert expected_path.read_text() == content
 finally:
 shutil.rmtree(source)
 shutil.rmtree(dest)
def test_when_a_file_has_been_renamed_in_the_source():
 try:
 source = tempfile.mkdtemp()
 dest = tempfile.mkdtemp()
 content = "Я — файл, который переименовали"
 source_path = Path(source) / 'source-filename'
 old_dest_path = Path(dest) / 'dest-filename'
 expected_dest_path = Path(dest) / 'source-filename'
 source_path.write_text(content)
 old_dest_path.write_text(content)
 sync(source, dest)
 assert old_dest_path.exists() is False
 assert expected_dest_path.read_text() == content
 finally:
 shutil.rmtree(source)
 shutil.rmtree(dest)
Вот это да! Да тут уйма настроек для двух простых случаев! Проблема
в том, что предметная логика — «выяснить разницу между двумя каталога-
