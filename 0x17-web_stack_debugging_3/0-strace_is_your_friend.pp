# Fixes bad `phpp` extensions in causing 500 error code

exec { 'fix-wordpress-server-errors':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
