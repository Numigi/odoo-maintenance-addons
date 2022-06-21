FROM quay.io/numigi/odoo-public:12.0
MAINTAINER numigi <contact@numigi.com>

ENV THIRD_PARTY_ADDONS /mnt/third-party-addons
RUN mkdir -p "${THIRD_PARTY_ADDONS}" && chown -R odoo "${THIRD_PARTY_ADDONS}"
COPY ./gitoo.yml /gitoo.yml
RUN gitoo install-all --conf_file /gitoo.yml --destination "${THIRD_PARTY_ADDONS}"

COPY maintenance_equipment_model /mnt/extra-addons/maintenance_equipment_model

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo
