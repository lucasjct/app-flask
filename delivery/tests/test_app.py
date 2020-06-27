def test_app(app):
    assert app.name == 'delivery.app'
    
def test_config(config):
    assert config['DEBUG'] is False
    
def status_code_404(client):
    assert client.get("/url_not_found").status_code == 404
    

    