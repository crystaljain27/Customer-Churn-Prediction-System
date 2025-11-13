# Customer Churn Prediction - Frontend

Beautiful Streamlit web application for predicting customer churn.

## Features

- 🎨 **Modern UI**: Beautiful, gradient-based design with custom styling
- 🔮 **Single Prediction**: Predict churn for individual customers
- 📊 **Batch Prediction**: Upload CSV for multiple predictions
- 📈 **Model Info**: View model performance and metrics
- 🎯 **Interactive Visualizations**: Plotly charts and gauges
- 🚦 **Risk Classification**: Color-coded risk levels (Low/Medium/High)
- 📥 **Export Results**: Download prediction results as CSV

## Installation

Make sure you have all dependencies installed:

```bash
pip install streamlit plotly requests pandas
```

Or install from project root:

```bash
pip install -r requirements.txt
```

## Running the Application

### Step 1: Start the Backend API

First, make sure the FastAPI backend is running:

```bash
# From project root
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 2: Start the Streamlit App

In a new terminal, run:

```bash
# From project root
streamlit run frontend/app.py
```

Or:

```bash
# From frontend directory
cd frontend
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Usage

### 🏠 Home Page
- Overview of the system
- Key performance metrics
- Project insights

### 🔮 Single Prediction
1. Fill in customer details in the form
2. Click "Predict Churn"
3. View probability gauge and risk level
4. Get recommended actions

### 📊 Batch Prediction
1. Download the CSV template
2. Fill in customer data
3. Upload the CSV file
4. Click "Run Batch Prediction"
5. View analytics and download results

### 📈 Model Info
- View model performance metrics
- See radar chart visualization
- Compare different ML models

## Pages Overview

### Home Page
- Key metrics display (ROC-AUC, Accuracy, Features, Model)
- System features and benefits
- Key insights from data analysis
- Getting started guide

### Single Prediction Page
- Interactive form with all customer fields
- Real-time prediction with probability gauge
- Risk level visualization (High/Medium/Low)
- Actionable recommendations based on risk

### Batch Prediction Page
- CSV file upload
- Template download
- Batch processing for multiple customers
- Risk distribution charts (pie & bar)
- Probability distribution histogram
- Filterable results table
- Export results to CSV

### Model Info Page
- Model details and metadata
- Performance metrics cards
- Radar chart visualization
- Model comparison table
- Training date and features count

## Features & Benefits

### Visual Design
- **Gradient backgrounds**: Modern, professional look
- **Custom CSS styling**: Enhanced UI components
- **Responsive layout**: Works on different screen sizes
- **Color-coded risks**: Easy identification (🟢🟡🔴)

### Interactive Elements
- **Probability gauge**: Visual representation of churn risk
- **Dynamic charts**: Plotly interactive visualizations
- **Real-time updates**: Instant predictions
- **Smooth animations**: Enhanced user experience

### Data Handling
- **CSV template**: Easy data preparation
- **Batch processing**: Handle multiple customers
- **Data filtering**: Filter results by risk/churn
- **Export capability**: Download predictions as CSV

## API Configuration

The app connects to the FastAPI backend at:
```python
API_URL = "http://localhost:8000"
```

To change this, modify the `API_URL` variable in `app.py`.

## Screenshots

### Home Page
- Clean, modern interface
- Key metrics at a glance
- Quick navigation

### Single Prediction
- Intuitive form layout
- Beautiful probability gauge
- Clear risk indication

### Batch Prediction
- Easy CSV upload
- Rich analytics dashboard
- Comprehensive results table

## Troubleshooting

### API Connection Error
If you see "Cannot connect to the API":
1. Make sure the backend is running: `uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000`
2. Check if `http://localhost:8000/health` returns a response
3. Verify API_URL in `app.py` is correct

### Import Errors
If you get module import errors:
```bash
pip install streamlit plotly requests pandas
```

### Port Already in Use
If port 8501 is busy:
```bash
streamlit run frontend/app.py --server.port 8502
```

## Dependencies

- **streamlit**: Web application framework
- **plotly**: Interactive visualizations
- **requests**: API communication
- **pandas**: Data manipulation

## Customization

### Change Colors
Edit the CSS in the `st.markdown()` section at the top of `app.py`:
```python
st.markdown("""<style>...</style>""", unsafe_allow_html=True)
```

### Modify Risk Thresholds
Update the `get_risk_color()` function to change risk colors.

### Add New Pages
Add new functions like `show_new_page()` and update the navigation radio buttons.

## Performance

- **Fast predictions**: Real-time response
- **Efficient batch processing**: Handles large CSV files
- **Smooth rendering**: Optimized Plotly charts
- **Responsive UI**: Quick page loads

## Best Practices

1. **Always start backend first** before launching Streamlit
2. **Use CSV template** for batch predictions
3. **Check API status** in sidebar
4. **Download results** for record-keeping

## Future Enhancements

Potential improvements:
- [ ] User authentication
- [ ] Historical predictions tracking
- [ ] Advanced filtering options
- [ ] More visualization types
- [ ] Dark mode toggle
- [ ] Multi-language support

## Support

For issues or questions:
1. Check backend is running
2. Verify all dependencies are installed
3. Review browser console for errors
4. Check API health endpoint

---

**Enjoy predicting customer churn with style! 🚀**

