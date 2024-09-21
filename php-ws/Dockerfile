FROM php:8.3.0-cli-bookworm

ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions opcache sockets @composer && \
    ln -s composer /usr/local/bin/c

COPY ./composer.json ./composer.lock /var/www/html/

WORKDIR /var/www/html

RUN composer install --optimize-autoloader

COPY . /var/www/html/

CMD ["php", "src/index.php"]
