# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 265

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 13. Внедрение зависимостей (и начальная загрузка) 265
 dockerfile: Dockerfile
 image: allocation-image
 ...
 api:
 image: allocation-image
 ...
 postgres:
 image: postgres:9.6
 ...
 redis:
 image: redis:alpine
 ...
 mailhog:
 image: mailhog/mailhog
 ports:
 - "11025:1025"
 - "18025:8025"
В интеграционных тестах мы используем класс реальных уведомлений
EmailNotifications, который связывается с сервером MailHog в кластере
Docker.
Интеграционный тест для электронной почты (tests/integration/test_email.py)
@pytest.fixture
def bus(sqlite_session_factory):
 bus = bootstrap.bootstrap(
 start_orm=True,
 uow=unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory),
 notifications=notifications.EmailNotifications(), 
 publish=lambda *args: None,
 )
 yield bus
 clear_mappers()
def get_email_from_mailhog(sku): 
 host, port = map(config.get_email_host_and_port().get, ['host',
 'http_port'])
 all_emails = requests.get(f'http://{host}:{port}/api/v2/
 messages').json()
 return next(m for m in all_emails['items'] if sku in str(m))
