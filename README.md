# Vidyutee

## Inspiration and Problem Statement
Modern society relies heavily on electricity, but sustainable energy generation is a major challenge. This is mainly due to non-uniform electricity consumption throughout the day.

The power generators run at overloading capacity during some parts of the day and idle during others. To make a sustainable solution for distributing the load on power generators over the day, we developed **VIDYUTEE**. Vidyutee takes in the appliances, preferred **ON** durations, and schedule them across the day.

The load is distributed across the whole day, which reduces the burden on the Power Generating Stations. United Nations Sustainable Development Goals **7, 9, 11, and 12** are addressed in this application.

![thumbnail_vidyutee](https://user-images.githubusercontent.com/76818035/229581007-dfaf70c3-e6ce-448f-884b-1ef8d2fafad2.png)



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

## How to run the code
Below steps are required to run fully gateway application which include Flutter - IOT - Web dashboard.

- Clone project to local machine:
`git clone git@github.com:Vidyutee/vidyutee.git`

- Get into the project directory and open `frontend` directory with terminal.

- Open your terminal and run:
`flutter pub get`

- Connect a physical device. (Make sure that the `developer mode` is switched ON for that device.)

- Write `flutter run` and there you go 😄.


## Youtube Demo
https://youtu.be/nn1wQCAg5n8

## Project Implementation

#### Frontend
Flutter application

#### Backend
It consists of the following components:
- Fast API containing the scheduling algorithm hosted on Google Cloud Run.
- Web Scraping script scheduled to extract data from Indian Energy Exchange to get the prior predicted load. The script is scheduled using GitHub actions.
- Firestore and Firebase Authentication used for storing and authentication purposes.

#### Technologies, Platforms and Languages:
- Firebase: Good Scalability and easy handling. NoSQL database was apt for our implementation. Also, its easy connection with Flutter and excellent documentation made it a nice choice.
- Flutter: Flutter allowed us to create an app for multiple platforms with a single codebase. Its active Community was also a big reason for us to choose it.
- Google Cloud Platform: High scalability, reliability, and high uptime.
- FastAPI: One of the most recent and best frameworks to create APIs.
- GitHub Actions: Used for Web scraping on each day at the scheduled time.
- Python: Great for our purpose due to its rich collection of libraries.
- Dart: For Flutter.

**Link for Webscraping Script**
https://github.com/Vidyutee/load_fetcher

## Feedback / Testing / Iteration
Being from the major in Electrical Engineering, we took help of our professors and intern mentors (at power substations) to test and get the feedback for the application. Here are some of the points we received:

- As the `Smart meters` are being installed in every corner of our country, our solution would be a great one, if it could directly take the readings from those meters and provide a schedule, rather than the user filling all details manually.
- The Solution could also help a lot in reducing the burden on the power grids which in turn, will also decrease the burden of high electricity costs on the consumers.
- There is a drawback that the scheduling algorithm doesn't consider the preferred time for the device by the user. For example, geysers are used in the morning time, but the algorithm can schedule it to run at night. We are still working on its implementation.
- Initially, we designed the algorithm on a general data for the whole country, but then we added the feature to add the region, to give region-wise schedule to the users.
- The app User Experience was improved, according to the suggestions, to give more ease of handling.
- various bugs in API and other parts of the app were cleared iteratively.


## Success and Completion of Solution
The Electrical Load Profile was carefully studied (data extracted from the Indian Energy Exchange) and then we tried to schedule some appliances. Though we don't have any particular impact directly shown, but mathematically, the loads were shifted accurately. We also took reference data from a research paper (provided by our professor), having similar goals, and matched our schedule with the one in the paper, and found a high level of similarity.

We are basically trying to shift the load from Peak hours to Off Peak hours, which reduces the damage and idle runs of the power generators. This app can be extremely useful if administered by the government directly.

## Scalability / Next Steps
- The app needs improvements in terms of UI and UX.
- The location feature is still in its primary phase, and needs to be improved.
- The user prefered time consideration is to be implemented in the algorithm. (We already have some ideas, and will work on them soon)

As of scalability, we don't expect any problem as all the actions are being handled on Firebase and Google Cloud Run, which handle the issues of scalability.

## Thank you for viewing our application 😄
