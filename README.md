# image-multisize-resizer

To resize an image into multiple sizes using a Python CLI, you can combine the  library (built into Python) with , the standard Python imaging library. [1, 2]  
Here is a complete, production-ready script that accepts an image path and a comma-separated list of target maximum widths. It will automatically calculate proportional heights to maintain the original aspect ratio. [3, 4, 5, 6]  

## Installation 

`pip install -r reqirements.txt`

## Usage

`python multi_resizer.py -i photo.jpg -s 400,800,1200`

or

`python multi_resizer.py --image elements.png --sizes 150,300 --output ./thumbnails`

## CLI Usage Examples 

• Basic Usage (Saves copies directly next to your original file): 
• Output files generated: , , and  
• Custom Output Directory (Saves copies into a dedicated folder): 

