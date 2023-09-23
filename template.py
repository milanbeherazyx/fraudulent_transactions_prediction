import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "fraud"

# Define the directory structure
directory_structure = [
    f".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "artifacts/__init__.py",
    "css/style.css",
    "research/trials_eda.ipynb",
    "research/trials_training.ipynb",
    "templates/home.html",
    "templates/index.html",
    "app.py",
    "streamlit_app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md"
]

for item in directory_structure:
    item_path = Path(item)
    if item_path.parent != Path(""):
        os.makedirs(item_path.parent, exist_ok=True)
        logging.info(f"Creating directory: {item_path.parent} for the file {item_path.name}")

    if not item_path.is_file() or item_path.stat().st_size == 0:
        with open(item_path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {item_path}")

    else:
        logging.info(f"{item_path.name} already exists")
