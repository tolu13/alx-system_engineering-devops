# A puppet manifest that creates file school in /tmp
# permisssions 0744
# web-data group

file  {'/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
