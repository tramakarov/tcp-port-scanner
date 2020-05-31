import socket
import sys


def scan(start, finish):
    """Main client method"""
    messages = ['Scanning...', 'Scanning.  ', 'Scanning . ', 'Scanning  .']
    for port in range(start, finish + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.01)
            try:
                sock.connect(('localhost', port))
                print('\r127.0.0.1:{}\t OPENED\n{}\r'.format(port, messages[port % 4]), end='')
            except:
                print('\r{}'.format(messages[port % 4]), end='')

    print('\rScanning completed')


def print_help():
    pass


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] in ['-h', '--help']:
            print_help()
            exit(0)
        else:
            try:
                end = start = int(sys.argv[1])
            except ValueError:
                start = end = None
    elif len(sys.argv) == 3:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            
            if end > 65535:
                print('Port numbers must be less than 65535')
                exit(-1)
            elif start > end:
                print('Invalid arguments')
                exit(-1)
        except ValueError:
            start = end = None
    else:
        print('Unexpected arguments')
        exit(-1)

    if start is not None:
        scan(start, end)
    else:
        print('Port number must be integer')
        exit(-1)
