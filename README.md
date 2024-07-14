# Let It <strike>```Burn 🔥```</strike> 
https://let-it-not-fire.onrender.com/

# How To...
https://github.com/user-attachments/assets/d273a768-fc32-43e0-b0e3-efe6e0090f5e

# Problem Statement  
Algeria experiences frequent forest fires, particularly during the hot and dry summer months. These fires primarily affect the northern regions of the country, where Mediterranean forests and woodlands are prevalent. The fires can be caused by natural factors like extreme heat and drought, but human activities such as agricultural burning or accidental ignitions also play a significant role.
Forest fires in Algeria pose serious threats to biodiversity, property, and human life. They contribute to deforestation and soil erosion, which can have long-term environmental impacts. The Algerian government and firefighting services work to combat these fires, but limited resources and challenging terrain often complicate their efforts.
In recent years, Algeria has faced particularly severe fire seasons, with some years seeing hundreds of fires and thousands of hectares of forest destroyed. Climate change is expected to exacerbate the risk and intensity of forest fires in the region.

# Solution Approach

Highly Accurate Prediction Based On Easily Available Data Such As Temparature,Relative Humadity,Wind Speed etc.. Can Help Mitigate The Spread Of Bush Fire.

# Best Model 

We Proposed a Highly Accurate Predictive Model Based On **TEN** Easily Available Data Based On The Canadian Forest Fire Weather Index (FWI) System to Address This Problem.   
**Elasticnet CV -- R2 Of *97.1%*** 

![Screenshot (79)](https://github.com/user-attachments/assets/5e206c34-1dae-4229-91b5-c3416a567e95)

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
## Target
- Fire Weather Index (FWI) || Index: 0 to 31.1 

### Download It Here
[Algerian Forest Fires Dataset](https://www.kaggle.com/datasets/nitinchoudhary012/algerian-forest-fires-dataset)

# Workflow Diagram

![Work Flow Bush Fire_page-0001](https://github.com/user-attachments/assets/9c751441-edee-4f21-a4fa-ca7cf0bac02e)

[Work Flow Bush Fire.pdf](https://github.com/user-attachments/files/16216577/Work.Flow.Bush.Fire.pdf)




