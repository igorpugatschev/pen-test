# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 275

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Эпилог 275
Пакет выставления счетов
Папка
parent: W orkspace
children: List[Folder ]
copy_to(target: Folder )
add_document(document: Document )
Рабочее пространство
account: Account
owner: User
members: List[User]
add_member(member: User )
Учетная запись
owner: User
packages: List[BillingPackage]
workspaces: List[W orkspace]
add_package ()
Версия документа
title: str
version number: in t
document: Documen t
Документ
add_version ()
workspace: W orkspace
parent: Folder
versions: List[Document Ve rsion]
Пользователь
account: Account
