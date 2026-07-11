 AI-Powered Food Segmentation & Calorie Estimator
This project utilizes a YOLOv8-Seg instance segmentation model fine-tuned on the FoodSeg103 dataset to detect food items from images, calculate their physical portions via adaptive mask area analytics, and live-query the USDA FoodData Central API to calculate precise overall meal caloric metrics.

 Getting Started on Kaggle
Follow these steps to deploy and run the entire pipeline in your own interactive environment.

1. Create a Notebook & Import the Dataset
Log into your account at Kaggle.

Go to the dataset page for FoodSeg103 (or the specific upload you are using).

Click the "New Notebook" button in the upper-right corner of the dataset interface. This spins up a notebook with the data pre-loaded into the read-only directory: /kaggle/input/.

2. Configure Accelerator Settings
Before running any machine learning operations, ensure you have GPU support enabled:

In the right sidebar panel of your Kaggle notebook, look under the "Settings" dropdown.

Under "Accelerator", change the selection from None to GPU T4 x2 or GPU P100.

Setting up your USDA API Key
To pull accurate nutritional data dynamically, the pipeline connects directly to the official government registry.

Head over to USDA FoodData Central API Guide and sign up for a free personal account.

Check your registered email inbox to retrieve your unique API Key.

Inside the notebook script cell, locate the configuration variable and update it:

USDA_API_KEY = "YOUR_ACTUAL_USDA_API_KEY_HERE"
