# Vidyutee

## Inspiration
Modern society relies heavily on electricity, but sustainable energy generation is a major challenge. This is mainly due to non-uniform electricity consumption throughout the day.

The power generators run at overloading capacity during some parts of the day and idle during others. To make a sustainable solution for distributing the load on power generators over the day, we developed **VIDYUTEE**. Vidyutee takes in the appliances, preferred **ON** durations, and schedule them across the day.

The load is distributed across the whole day, which reduces the burden on the Power Generating Stations. United Nations Sustainable Development Goals **7, 9, 11, and 12** are addressed in this application.

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
9. You can also set the `Location` to get more personalized results for that location. Location page can be accessed via the navigation menu at the bottom of the screen.
