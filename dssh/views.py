from django.shortcuts import render
from django.http import HttpResponse
import paramiko


def index(request):
    return render(request, 'static/index.html')


def cssh(request):
    string = ''
    dos = request.POST['dos']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.149.130', 22, 'root', 'toor')
    stdin, stdout, stderr = ssh.exec_command(dos)
    result_err = stdout.read(), stderr.read()
    for line in result_err:
        string += line

    ssh.close()
    return render(request, 'static/index.html', {'string': string})


