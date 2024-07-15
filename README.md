# Let It <strike>```Burn 🔥```</strike> 
https://let-it-not-fire.onrender.com/
> Can Take Up To 50 Seconds To Run Due To Free Plan. Patience Please 🥺

<br>

# How To...
https://github.com/user-attachments/assets/d273a768-fc32-43e0-b0e3-efe6e0090f5e

# Problem Statement  
Algeria has frequent wildfires, especially in the north during summer. These fires are caused by both natural factors (heat, drought) and human activities (agriculture, accidents). The fires damage the environment and are difficult to fight due to limited resources and terrain. The situation is expected to worsen due to climate change.

# Solution Approach

Highly Accurate Prediction Based On Easily Available Data Such As Temparature,Relative Humadity,Wind Speed etc.. Can Help Mitigate The Spread Of Bush Fire.

# Best Model 

We Proposed a Highly Accurate Predictive Model Based On **TEN** Easily Available Data Based On The Canadian Forest Fire Weather Index (FWI) System to Address This Problem.   
**Elasticnet CV -- R2 Of *97.1%*** 

![Screenshot (79)](https://github.com/user-attachments/assets/5e206c34-1dae-4229-91b5-c3416a567e95)

# Stack Used
- Numpy
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Pickle
- Flask
  
# Dataset
The Dataset Contains 14 Features. We Used 9 Features and Enginerred 1 featue From Existing Dataset.
## Usable Features
- Temperature || Celsius degrees: 22 to 42
- Relative Humadity (RH) || Relative Humidity in %: 21 to 90
- Wind Speed (WS) || Wind speed in km/h: 6 to 29
- Rain || Total day in mm: 0 to 16.8
- Fine Fuel Moisture Code (FFMC) || Index from the FWI system: 28.6 to 92.5
- Duff Moisture Code (DMC) || Index from the FWI system: 1.1 to 65.9
- Drought Code (DC) ||  Index from the FWI system: 7 to 220.4
- Initial Spread Index (ISI) || Index from the FWI system: 0 to 18.5
- Buildup Index (BUI) || Index from the FWI system: 1.1 to 68
- Classes: two classes || [0--> Not Fire] [1--> Fire]
- Region
   - Bejaia -> 0
   - Sidi Bel-abbes -> 1
## Target
- Fire Weather Index (FWI) || Index: 0 to 31.1 

### Download It Here
[Algerian Forest Fires Dataset](https://www.kaggle.com/datasets/nitinchoudhary012/algerian-forest-fires-dataset)

# Workflow Diagram

![Workflow Diagram_page-0001](https://github.com/user-attachments/assets/a66180f9-876b-4585-bfc1-d431192787a3)

[Workflow Diagram.pdf](https://github.com/user-attachments/files/16227597/Workflow.Diagram.pdf)

# Install Libraries
```
pip install numpy pandas scikit-learn Flask gunicorn
```

# Clone The Repo

``` 
https://github.com/secrakib/Save-The-Forest.git
```
# Licenses
<table><tr><td> MIT License </td></tr></table>

