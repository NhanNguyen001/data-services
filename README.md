# Data Processing Environment

A production-ready data processing environment that integrates Apache Airflow, Jupyter Lab, and Apache Spark. This setup provides a robust platform for data engineering, analysis, and machine learning workflows.

## 🚀 Features

- **Apache Airflow** (v2.7.3) for workflow orchestration
- **Jupyter Lab** with Python 3.11 for interactive development
- **Apache Spark** (v3.5) for distributed data processing
- Containerized environment using Docker
- Pre-configured integration between all services

## 📋 Prerequisites

- Docker Engine (20.10.0+)
- Docker Compose (v2.0.0+)
- At least 4GB of available RAM
- 10GB of free disk space

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-services.git
   cd data-services
   ```

2. Start the services:
   ```bash
   docker-compose up --build
   ```

## 🌐 Accessing Services

| Service | URL | Credentials |
|---------|-----|-------------|
| Airflow UI | http://localhost:8080 | username: `admin`<br>password: `admin` |
| Jupyter Lab | http://localhost:8888 | No authentication required |
| Spark UI | http://localhost:8090 | No authentication required |

## 📁 Project Structure

```
data-services/
├── airflow/
│   ├── dags/           # Airflow DAG files
│   ├── logs/           # Airflow logs
│   └── plugins/        # Airflow plugins
├── data/               # Shared data directory
├── notebooks/          # Jupyter notebooks
├── docker-compose.yml  # Docker services configuration
├── Dockerfile.airflow  # Airflow container configuration
├── Dockerfile.jupyter  # Jupyter container configuration
└── README.md
```

## 💡 Usage Examples

### Creating a PySpark Session in Jupyter

```python
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("MyApp") \
    .master("spark://spark-master:7077") \
    .config("spark.driver.memory", "1g") \
    .config("spark.executor.memory", "1g") \
    .getOrCreate()

# Create a sample DataFrame
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["name", "value"])
df.show()
```

### Running an Airflow DAG

1. Place your DAG file in the `airflow/dags` directory
2. The DAG will automatically be picked up by Airflow
3. Access the Airflow UI to trigger and monitor your DAG

## 🔧 Configuration

### Modifying Resource Allocation

Adjust the following parameters in `docker-compose.yml`:

```yaml
services:
  jupyter:
    environment:
      SPARK_DRIVER_MEMORY: 1g
      SPARK_EXECUTOR_MEMORY: 1g

  spark-worker:
    environment:
      SPARK_WORKER_MEMORY: 1G
      SPARK_WORKER_CORES: 1
```

## 🔍 Monitoring

- **Airflow**: View task status, logs, and DAG runs in the Airflow UI
- **Spark**: Monitor job progress and resource usage in the Spark UI
- **Container Logs**: 
  ```bash
  # View all logs
  docker-compose logs -f

  # View specific service logs
  docker-compose logs -f [service-name]
  ```

## 🛑 Stopping Services

```bash
# Stop and remove containers while preserving data
docker-compose down

# Stop and remove everything including volumes
docker-compose down -v
```

## 🔒 Security Notes

- Default credentials are for development only
- Change passwords before deploying to production
- Consider enabling authentication for Jupyter and Spark UI
- Review and adjust file permissions as needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Troubleshooting

### Common Issues

1. **Spark Connection Issues**
   - Verify Spark master URL is correct
   - Check if Spark worker is running
   - Ensure sufficient memory allocation

2. **Airflow DAG Not Appearing**
   - Check DAG file syntax
   - Verify file permissions
   - Review Airflow scheduler logs

3. **Container Memory Issues**
   - Adjust Docker memory limits
   - Reduce Spark executor memory
   - Monitor resource usage

For more detailed troubleshooting, check the container logs or create an issue in the repository.