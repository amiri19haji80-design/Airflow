W=$(sudo docker ps -q -f name=airflow_airflow-worker | head -1)
sudo docker exec $W python -c "
import traceback
from core.config.parser import parse_tasks_file
from core.config.validator import validate_tasks
p='/opt/airflow/dags/pipelines/sources/crm/crm_plus/crm_plus_nas_landing/app.yaml'
try:
    t=parse_tasks_file(p); print('PARSED:', t)
    print('VALID:', validate_tasks(t))
except Exception: traceback.print_exc()
"
