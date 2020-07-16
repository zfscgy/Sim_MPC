import requests

task_request = {
    "task_name": "test-task",
    "model_name": "shared_nn",
    "configs": {
        "train_config": {
            "max_iter": 12345,
            "loss_func": "mse",
            "metrics": "auc_ks"
        }
    },
    "clients": {
        "main_client": {
            "addr": "127.0.0.1",
            "http_port": 8377,
            "computation_port": 8378
        },
        "crypto_producer": {
            "addr": "127.0.0.1",
            "http_port": 8390,
            "computation_port": 8391
        },
        "feature_clients": [
            {
                "addr": "127.0.0.1",
                "http_port": 8084,
                "computation_port": 8085,
                "data_file": "Splitted_Indexed_Data/credit_default_data1.csv",
                "dim": 30
            },
            {
                "addr": "127.0.0.1",
                "http_port": 8082,
                "computation_port": 8083,
                "data_file": "Splitted_Indexed_Data/credit_default_data2.csv",
                "dim": 42
            }
        ],
        "label_client": {
            "addr": "127.0.0.1",
            "http_port": 8884,
            "computation_port": 8885,
            "data_file": "Splitted_Indexed_Data/credit_default_label.csv",
            "dim": 1,
        }
    }
}

resp = requests.post("http://127.0.0.1:8380/createTask", json=task_request)
print(resp.status_code, resp.text)