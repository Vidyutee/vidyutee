# vidyutee

## Inspiration
Electricity is like Oxygen for the modern era, yet sustainability in energy generation is a big problem. It is majorly because of the non-uniform electricity consumption across the day.

Power generators run at overloading capacity at some parts of the day while they run idle for the other part. To make a sustainable solution for saving energy and distributing the load on Power generators throughout the day, we created the application **VIDYUTEE**. Vidyutee took in the appliances, preferred **ON** durations, and scheduled them across the day, such that the devices run more towards the time when the load is less, reducing the burden on the generating stations.

This reduces the burden on the Power Generating stations and lowers the peak loads on them by distributing the load across the complete day. This application caters to the **7, 9, 11, and 12th Sustainable Development Goals** of the United Nations.

## How to use this application
1. Download the apk from [here](https://github.com/Vidyutee/vidyutee/releases/tag/preliminary-version) and install the app.
2. Register if you're a new user, or directly login with your credentials.
3. You will land on the `Appliance Set` page. Here, click on `+ Add New` button and create a new appliance set. An appliance set will serve as the collection of all the appliances which need to be scheduled.
4. Click on the created appliance set, and you will land on the `Appliances` page. Click on `+Add New Appliance` button to add a new appliance.
5. A dialog box will appear asking for the following details:
  ```
  - Appliance Name
  - Appliance Rating (in kW which is mentioned on the appliances)
  - ON duration (duration for the `ON` time of the device in minutes): (ranges from `15 min - 1439 min`)
  ```
6. Click on `Upload Now` to upload all the data of your appliances in our database.
7. Finally click on `Schedule Now` to run our backend algorithm and give the best time slots to run your appliances.
8. The :bulb: stands for a device to be `ON` in that time block, while `-` refers to the device being `OFF`.
