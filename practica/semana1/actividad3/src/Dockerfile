FROM ubuntu:14.04
RUN echo 'mysql-server mysql-server/root_password password secretpw' | \
debconf-set-selections && \
echo 'mysql-server mysql-server/root_password_again password secretpw' | \
debconf-set-selections
RUN apt-get update && apt-get -y install \
apache2 \
php5 \
php5-mysql \
supervisor \
wget \
mysql-server
RUN wget http://wordpress.org/latest.tar.gz && \
tar xzvf latest.tar.gz && \
rm latest.tar.gz && \
cp -R ./wordpress/* /var/www/html && \
rm /var/www/html/index.html
RUN (/usr/bin/mysqld_safe --skip-grant-tables &) && \
sleep 5 && \
mysqladmin -u root create wordpress
COPY wp-config.php /var/www/html/wp-config.php
RUN chown -R www-data:www-data /var/www/html
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 80
CMD ["/usr/bin/supervisord"]
