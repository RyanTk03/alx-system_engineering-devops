#  fix web stack debugging #4 for task 0

exec { 'append to nginx default':
    command => 'echo \'ULIMIT="-n 4096"\' >> /etc/default/nginx',
    unless  => 'grep -q \'ULIMIT="-n 4096"\' /etc/default/nginx',
}

service { 'nginx':
    ensure    => running,
    subscribe => File['/etc/default/nginx']
}
