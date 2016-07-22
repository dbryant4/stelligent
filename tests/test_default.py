def test_nginx_package(Package):
    package = Package('nginx')

    assert package.is_installed

def test_nginx_working(Command):
    response = Command('curl http://127.0.0.1/')

    assert 'Automation for the People' in response.stdout

def test_nginx_service(Service, Socket):
    service = Service('nginx')
    socket = Socket('tcp://0.0.0.0:80')

    assert service.is_running
    assert service.is_enabled
    assert socket.is_listening

def test_index_html(File):
    index = File('/usr/share/nginx/html/index.html')

    assert index.content.strip() == 'Automation for the People'
