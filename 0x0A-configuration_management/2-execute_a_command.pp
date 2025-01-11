#Using Puppet, create a manifest that kills a process named killmenow
exec {'kill':
    command => 'pkill -9 killmenow',
    path    => ['/usr/bin/'],
}
