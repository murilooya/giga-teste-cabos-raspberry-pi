# giga-teste-cabos-raspberry-pi
Script feito para Raspberry Pi que testa conexões entre cabos. Verificando se os mesmos estão em curto ou em aberto.

Há também dois scripts que se coloca na pasta /home/pi/Desktop da RaspOS chamado, giga-config-sh.
Esse script faz alterações no crontab para a inicialização da script de teste no inicio do boot.

O nome do script de teste está denominado como boottest.py como default, assim caso o script em python esteja com nome diferente,
altere o nome boottest.py no script do giga-config.sh.
