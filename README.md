## About the Project
---
For the RoboSub competition, I am tasked with enabling the robots to detects certain shaped under the water.

## Built With
---
- CV2
- numpy

## Usage
--- 
The functional project code is the second cell of <Corner_code.ipynb>.

The code read the file's name in the 'raw' and output a slider to adjust the strength of canny filter. The canny proccessed image is feed into CV2 detect corner function and output a corners detected images.

Using the preset function, it is possible to control the strength of any filter thus enabling testing with the corner detection function.

## Goals
---
- [ ] effectively detect still images' corner
- [x] get it to work with videos
- [ ] detect corner in video
- [ ] detect corner underwater 


