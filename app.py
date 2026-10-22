F=/mnt/nfs/ci-cd/dags/core/src/core/mappings/config/golden_sources/databases.yaml
sed -i '129s|^\(\s*\)cyberark_vault: "IV2ACMPPCIA-OPSD"|\1# cyberark_vault: "IV2ACMPPCIA-OPSD"|; 130s|^\(\s*\)cyberark_key: "CORE_CIA_RO".*|\1# cyberark_key: "CORE_CIA_RO"\n\1airflow_conn_id: "cia"|' $F
sed -n '126,133p' $F



W=$(sudo docker ps -q -f name=airflow_airflow-worker | head -1)
sudo docker exec $W python -c "
import yaml; d=yaml.safe_load(open('/opt/airflow/dags/core/src/core/mappings/config/golden_sources/databases.yaml'))
print(d['cia']['ALL'])"
