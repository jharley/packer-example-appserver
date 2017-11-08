def test_ami_launch(host):
    assert host.system_info.type == 'linux'

def test_appserver(host):
    assert host.socket('tcp://80').is_listening

    cmd = host.run("curl -s http://localhost | grep 'Hello, DevOps TO'")
    assert cmd.rc == 0
