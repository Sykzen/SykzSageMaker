apt install udhcpd
touch /var/lib/misc/udhcpd.leases

# enregistrer des copies
if [ -e /etc/rc.local ]
then
    cp /etc/rc.local /etc/rc.local.adhoc_bak
fi

if [ -e /etc/udhcpd.conf ]
then
    cp /etc/udhcpd.conf /etc/udhcpd.conf.adhoc_bak
fi

if [ -e /etc/dhcpcd.conf ]
then
    cp /etc/dhcpcd.conf /etc/dhcpcd.conf.adhoc_bak
fi
cp rc.local /etc
cp udhcpd.conf /etc
cp dhcpcd.conf /etc
exit 0