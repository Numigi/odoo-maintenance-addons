FROM quay.io/numigi/odoo-public:12.0
MAINTAINER numigi <contact@numigi.com>

COPY maintenance_equipment_model /mnt/extra-addons/maintenance_equipment_model

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo
