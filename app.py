schema_version: "1.0"

tasks:
  - name: crm_plus_nas_landing
    layer: alpha
    engine: spark
    golden_source:
      type: filesystem
      transport: smb
      name: crm_nas
      path: "prd/gcaprods/CRM"
      ingest_mode: incremental
      module: ../modules/crm_plus_app.py
      function: nas_landing_log
      api_params:
        s3_prefix: "landing/crm_nas/crm_nas/current/"
    write_mode: append
    schema_evolution: permissive
    metadata:
      project: crm
