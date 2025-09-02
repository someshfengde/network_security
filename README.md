# Network Security Project - Phishing Data Detection

A comprehensive machine learning project for detecting phishing attacks using network security data. This project implements a complete ML pipeline with data ingestion, validation, transformation, and model training capabilities.

## 🚀 Features

- **Complete ML Pipeline**: End-to-end machine learning pipeline with modular components
- **MongoDB Integration**: Seamless data storage and retrieval from MongoDB
- **Data Validation**: Comprehensive data validation with drift detection
- **Model Training**: Automated model training with performance evaluation
- **Docker Support**: Containerized deployment ready
- **Comprehensive Logging**: Detailed logging throughout the pipeline
- **Exception Handling**: Robust error handling across all components

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.12+**
- **MongoDB** (local installation or cloud instance)
- **uv** (Python package manager)
- **Docker** (optional, for containerized deployment)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd network_security
```

### 2. Install Dependencies

```bash
# Install uv if you haven't already
pip install uv

# Sync project dependencies
uv sync
```

### 3. Environment Setup

Create a `.env` file in the project root with your MongoDB configuration:

```bash
# Create .env file
touch .env

# Add MongoDB connection string
echo "MONGO_DB_URL=mongodb+srv://username:password@cluster.mongodb.net/" >> .env
```

**Required Environment Variables:**
- `MONGO_DB_URL`: Your MongoDB connection string

## 📁 Project Structure

```
network_security/
├── src/networksecurity/           # Main package
│   ├── components/                # Pipeline components
│   │   ├── data_ingestion.py     # Data collection from MongoDB
│   │   ├── data_validation.py    # Data quality validation
│   │   ├── data_transformation.py # Data preprocessing
│   │   └── model_trainer.py      # Model training
│   ├── entity/                    # Configuration entities
│   │   ├── config_entity.py      # Configuration classes
│   │   └── artifact_entity.py    # Artifact classes
│   ├── exception/                 # Custom exception handling
│   ├── logging/                   # Logging utilities
│   ├── utils/                     # Utility functions
│   │   ├── main_utils/           # General utilities
│   │   └── ml_utils/             # ML-specific utilities
│   └── constant/                  # Project constants
├── NetworkData/                   # Local data storage
├── Artifacts/                     # Generated artifacts
├── logs/                          # Application logs
├── main.py                        # Main pipeline execution
├── push_data.py                   # Data upload utility
├── Dockerfile                     # Docker configuration
└── pyproject.toml                # Project configuration
```

## 🚀 Running the Project

### 1. Upload Data to MongoDB (First Time Setup)

If you have local CSV data that needs to be uploaded to MongoDB:

```bash
# Upload NetworkData/data.csv to MongoDB
uv run python push_data.py
```

This will:
- Read `NetworkData/data.csv`
- Convert CSV to JSON format
- Upload data to MongoDB collection `NetworkData` in database `NichoTJ`

### 2. Run the Complete ML Pipeline

Execute the full machine learning pipeline:

```bash
# Run the complete training pipeline
uv run python main.py
```

This will execute the following stages sequentially:

1. **Data Ingestion**: Fetch data from MongoDB and split into train/test sets
2. **Data Validation**: Validate data quality and detect data drift
3. **Data Transformation**: Preprocess and transform the data
4. **Model Training**: Train ML model and evaluate performance

### 3. Individual Component Execution

You can also run individual components by importing and using them separately:

```python
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

# Initialize configuration
training_pipeline_config = TrainingPipelineConfig()
data_ingestion_config = DataIngestionConfig(training_pipeline_config)

# Run data ingestion
data_ingestion = DataIngestion(data_ingestion_config)
artifact = data_ingestion.initiate_data_ingestion()
```

## 🐳 Docker Deployment

### Build Docker Image

```bash
# Build the Docker image
docker build -t network-security .
```

### Run with Docker

```bash
# Run the container
docker run -d \
  --name network-security-app \
  -e MONGO_DB_URL="your-mongodb-connection-string" \
  network-security
```

## 📊 Pipeline Workflow

```mermaid
graph TD
    A[Raw Data CSV] --> B[MongoDB Storage]
    B --> C[Data Ingestion]
    C --> D[Data Validation]
    D --> E[Data Transformation]
    E --> F[Model Training]
    F --> G[Model Evaluation]
    G --> H[Final Model]
```

### Pipeline Stages:

1. **Data Ingestion** (`components/data_ingestion.py`)
   - Connects to MongoDB
   - Fetches phishing detection data
   - Splits data into training and testing sets
   - Stores processed data in feature store

2. **Data Validation** (`components/data_validation.py`)
   - Validates data schema and quality
   - Detects data drift using statistical tests
   - Separates valid and invalid data
   - Generates drift reports

3. **Data Transformation** (`components/data_transformation.py`)
   - Handles missing values using KNN imputation
   - Scales and normalizes features
   - Prepares data for model training
   - Saves preprocessing objects

4. **Model Training** (`components/model_trainer.py`)
   - Trains machine learning models
   - Evaluates model performance
   - Validates against expected accuracy thresholds
   - Saves trained model artifacts

## 📈 Model Performance

The model trainer includes automated evaluation with:
- **Expected Accuracy**: Minimum 60% (configurable)
- **Overfitting Detection**: Monitors train-test performance gap
- **Classification Metrics**: Precision, Recall, F1-Score

## 📝 Logging

All pipeline activities are logged with detailed information:
- Logs are stored in `logs/` directory
- Timestamped log files for each run
- Different log levels (INFO, ERROR, DEBUG)

## ⚙️ Configuration

Key configuration parameters can be modified in:
- `src/networksecurity/constant/training_pipeline/__init__.py`

Important settings:
- Database and collection names
- File paths and directories
- Model training parameters
- Data validation thresholds

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 Dependencies

Key dependencies managed via `pyproject.toml`:
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **pymongo**: MongoDB integration
- **mlflow**: ML experiment tracking
- **python-dotenv**: Environment variable management

## 🔧 Troubleshooting

### Common Issues:

1. **MongoDB Connection Error**
   - Ensure MongoDB is running
   - Check `MONGO_DB_URL` in `.env` file
   - Verify network connectivity

2. **Module Import Error**
   - Run `uv sync` to install dependencies
   - Ensure you're in the project root directory

3. **Data Not Found**
   - Run `push_data.py` first to upload data to MongoDB
   - Check if `NetworkData/data.csv` exists

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the logs in `logs/` directory for detailed error information

---

**Built with ❤️ for Network Security and Phishing Detection**