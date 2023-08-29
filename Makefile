run_api:
	uvicorn judgeabook.api.api:app --reload

# reset_local_files:
# 	rm -rf ${ML_DIR}
# 	mkdir -p ~/.lewagon/mlops/data/
# 	mkdir ~/.lewagon/mlops/data/raw
# 	mkdir ~/.lewagon/mlops/data/processed
# 	mkdir ~/.lewagon/mlops/training_outputs
# 	mkdir ~/.lewagon/mlops/training_outputs/metrics
# 	mkdir ~/.lewagon/mlops/training_outputs/models
# 	mkdir ~/.lewagon/mlops/training_outputs/params
