# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 85

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 3. О связанности и абстракциях 85
 def move(self, src, dest):
 self.append(('MOVE', src, dest))
 def delete(self, dest):
 self.append(('DELETE', src, dest))
def test_when_a_file_exists_in_the_source_but_not_the_destination():
 source = {"sha1": "my-file" }
 dest = {}
 filesystem = FakeFileSystem()
 reader = {"/source": source, "/dest": dest}
 synchronise_dirs(reader.pop, filesystem, "/source", "/dest")
 assert filesystem == [("COPY", "/source/my-file", "/dest/my-file")]
def test_when_a_file_has_been_renamed_in_the_source():
 source = {"sha1": "renamed-file" }
 dest = {"sha1": "original-file" }
 filesystem = FakeFileSystem()
 reader = {"/source": source, "/dest": dest}
 synchronise_dirs(reader.pop, filesystem, "/source", "/dest")
 assert filesystem == [("MOVE", "/dest/original-file", "/dest/
 renamed-file")]
 Боб обожает использовать списки для построения простых тестовых
двойников, даже если это бесит его коллег. Это означает, что мы можем
писать тесты вроде проверки того, что foo нет в базе данных, assert foo
not in database.
 Каждый метод в поддельной файловой системе, FakeFileSystem, про -
сто добавляет что-то в список, чтобы мы могли проверить его позже. Это
пример объекта-шпиона.
Преимущество этого подхода в том, что тесты работают с той же самой
функцией, которая используется производственным кодом. Недостатком
является то, что мы должны сделать компоненты с внутренним состоянием
явными и передавать их туда-сюда. Дэвид Хайнемайер Ханссон, создатель
Ruby on Rails, как известно, описал это как «спровоцированное тестом
повреждение дизайна» (test-induced design damage).
В любом случае теперь можно работать над исправлением всех ошибок в реа-
лизации; перечислять тесты для всех крайних случаев теперь намного проще.
