# Rank-of-a-Matrix-with-Visual-Interface
Rank of a Matrix is a web-based tool to calculate the rank of any matrix. Users can input matrices, visualize row-reduction steps, and get the rank instantly. Built with Python backend for computation and HTML, CSS, JS frontend for an interactive, user-friendly interface.


A web-based tool to calculate the rank of any matrix. Users can input matrices manually or via CSV files and get the rank instantly with a visually interactive interface. Built with Python (Flask) backend and HTML/CSS/JS frontend.

## Features
- Dynamic matrix input via text area or CSV upload
- Rank calculation using Python NumPy backend
- Step-by-step visualization of row operations (optional)
- Light/Dark mode theme toggle
- Responsive and animated UI with dynamic colors


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Rank-of-a-Matrix-with-Visual-Interface.git


cd Rank-of-a-Matrix-with-Visual-Interface


python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate      # Mac/Linux


pip install -r requirements.txt


### **Usage**
```markdown
## Usage

Run the Flask server:
```bash
python app.py

Open your browser at http://127.0.0.1:5000 and start calculating matrix ranks!

### **Folder Structure (Optional but helps)**
```markdown
## Folder Structure


matrix_rank_app/
│
├── app.py            # Python backend
├── templates/
│   └── index.html    # Frontend HTML
├──static
    └── style.css     # Optional CSS
    
## Dependencies
- Python 3.x
- Flask
- NumPy

## License
This project is licensed under MIT License.

Flask==2.3.3
numpy==1.26.0

![Screenshot](assets/screenshot.png)


