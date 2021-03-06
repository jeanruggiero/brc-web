# brc_api

BrcApi - JavaScript client for brc_api
This is an API that allows access to Boealps BRC course and participant data.
This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install brc_api --save
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing 
into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

Finally, switch to the directory you want to use your brc_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

You should now be able to `require('brc_api')` in javascript files from the directory you ran the last 
command above from.

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/YOUR_USERNAME/brc_api
then install it via:

```shell
    npm install YOUR_USERNAME/brc_api --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually 
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var BrcApi = require('brc_api');

var api = new BrcApi.DefaultApi()

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.gearGet(callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/jeanruggiero/brc-web/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrcApi.DefaultApi* | [**gearGet**](../brc-react/docs/DefaultApi.md#gearGet) | **GET** /gear | returns a list of all gear
*BrcApi.DefaultApi* | [**homeworkGet**](../brc-react/docs/DefaultApi.md#homeworkGet) | **GET** /homework | returns a list of homework matching the criteria
*BrcApi.DefaultApi* | [**meetingsLecturesGet**](../brc-react/docs/DefaultApi.md#meetingsLecturesGet) | **GET** /meetings/lectures | returns a list of lectures matching the criteria
*BrcApi.DefaultApi* | [**meetingsOutingsGet**](../brc-react/docs/DefaultApi.md#meetingsOutingsGet) | **GET** /meetings/outings | returns a list of outings matching the criteria
*BrcApi.DefaultApi* | [**postsGet**](../brc-react/docs/DefaultApi.md#postsGet) | **GET** /posts | returns a list of all course updates
*BrcApi.DefaultApi* | [**reviewsGradClimbGet**](../brc-react/docs/DefaultApi.md#reviewsGradClimbGet) | **GET** /reviews/grad_climb | returns a list of grad climb reviews
*BrcApi.DefaultApi* | [**reviewsGradClimbIdGet**](../brc-react/docs/DefaultApi.md#reviewsGradClimbIdGet) | **GET** /reviews/grad_climb/{id} | returns the grad climb review with the specified id
*BrcApi.DefaultApi* | [**reviewsGradClimbIdPut**](../brc-react/docs/DefaultApi.md#reviewsGradClimbIdPut) | **PUT** /reviews/grad_climb/{id} | updates an existing grad climb review
*BrcApi.DefaultApi* | [**reviewsGradClimbPost**](../brc-react/docs/DefaultApi.md#reviewsGradClimbPost) | **POST** /reviews/grad_climb | creates a new grad climb review
*BrcApi.DefaultApi* | [**reviewsInstructorReviewGet**](../brc-react/docs/DefaultApi.md#reviewsInstructorReviewGet) | **GET** /reviews/instructor_review | returns a list of instructor reviews matching the criteria
*BrcApi.DefaultApi* | [**reviewsInstructorReviewIdGet**](../brc-react/docs/DefaultApi.md#reviewsInstructorReviewIdGet) | **GET** /reviews/instructor_review/{id} | returns the instructor review with the specified id
*BrcApi.DefaultApi* | [**reviewsInstructorReviewIdPut**](../brc-react/docs/DefaultApi.md#reviewsInstructorReviewIdPut) | **PUT** /reviews/instructor_review/{id} | updates an existing instructor review
*BrcApi.DefaultApi* | [**reviewsInstructorReviewPost**](../brc-react/docs/DefaultApi.md#reviewsInstructorReviewPost) | **POST** /reviews/instructor_review | creates a new instructor review
*BrcApi.DefaultApi* | [**reviewsLeavenworthGet**](../brc-react/docs/DefaultApi.md#reviewsLeavenworthGet) | **GET** /reviews/leavenworth | returns a list of leavenworth reviews matching the criteria
*BrcApi.DefaultApi* | [**reviewsLeavenworthIdGet**](../brc-react/docs/DefaultApi.md#reviewsLeavenworthIdGet) | **GET** /reviews/leavenworth/{id} | returns the leavenworth review with specified id
*BrcApi.DefaultApi* | [**reviewsLeavenworthIdPut**](../brc-react/docs/DefaultApi.md#reviewsLeavenworthIdPut) | **PUT** /reviews/leavenworth/{id} | updates an existing leavenworth review
*BrcApi.DefaultApi* | [**reviewsLeavenworthPost**](../brc-react/docs/DefaultApi.md#reviewsLeavenworthPost) | **POST** /reviews/leavenworth | creates a new leavenworth review
*BrcApi.DefaultApi* | [**reviewsSkillsNightGet**](../brc-react/docs/DefaultApi.md#reviewsSkillsNightGet) | **GET** /reviews/skills_night | returns a list of skills night reviews matching the criteria
*BrcApi.DefaultApi* | [**reviewsSkillsNightIdGet**](../brc-react/docs/DefaultApi.md#reviewsSkillsNightIdGet) | **GET** /reviews/skills_night/{id} | returns the skills night review with the specified id
*BrcApi.DefaultApi* | [**reviewsSkillsNightIdPut**](../brc-react/docs/DefaultApi.md#reviewsSkillsNightIdPut) | **PUT** /reviews/skills_night/{id} | updates an existing skills night review
*BrcApi.DefaultApi* | [**reviewsSkillsNightPost**](../brc-react/docs/DefaultApi.md#reviewsSkillsNightPost) | **POST** /reviews/skills_night | creates a new skills night review
*BrcApi.DefaultApi* | [**reviewsSquamish1Get**](../brc-react/docs/DefaultApi.md#reviewsSquamish1Get) | **GET** /reviews/squamish1 | returns a list of squamish1 reviews matching the criteria
*BrcApi.DefaultApi* | [**reviewsSquamish1IdGet**](../brc-react/docs/DefaultApi.md#reviewsSquamish1IdGet) | **GET** /reviews/squamish1/{id} | returns the squamish1 review with the specified id
*BrcApi.DefaultApi* | [**reviewsSquamish1IdPut**](../brc-react/docs/DefaultApi.md#reviewsSquamish1IdPut) | **PUT** /reviews/squamish1/{id} | updates an existing squamish1 review
*BrcApi.DefaultApi* | [**reviewsSquamish1Post**](../brc-react/docs/DefaultApi.md#reviewsSquamish1Post) | **POST** /reviews/squamish1 | creates a new squamish1 review
*BrcApi.DefaultApi* | [**reviewsSquamish2Get**](../brc-react/docs/DefaultApi.md#reviewsSquamish2Get) | **GET** /reviews/squamish2 | returns a list of squamish2 reviews matching the criteria
*BrcApi.DefaultApi* | [**reviewsSquamish2IdGet**](../brc-react/docs/DefaultApi.md#reviewsSquamish2IdGet) | **GET** /reviews/squamish2/{id} | returns the squamish2 review with the specified id
*BrcApi.DefaultApi* | [**reviewsSquamish2IdPut**](../brc-react/docs/DefaultApi.md#reviewsSquamish2IdPut) | **PUT** /reviews/squamish2/{id} | updates an existing squamish2 review
*BrcApi.DefaultApi* | [**reviewsSquamish2Post**](../brc-react/docs/DefaultApi.md#reviewsSquamish2Post) | **POST** /reviews/squamish2 | creates a new squamish2 review
*BrcApi.DefaultApi* | [**studentsGet**](../brc-react/docs/DefaultApi.md#studentsGet) | **GET** /students | returns all students matching criteria
*BrcApi.DefaultApi* | [**studentsIdGet**](../brc-react/docs/DefaultApi.md#studentsIdGet) | **GET** /students/{id} | returns the student with the specified id
*BrcApi.DefaultApi* | [**studentsIdPut**](../brc-react/docs/DefaultApi.md#studentsIdPut) | **PUT** /students/{id} | updates an existing student's profile


## Documentation for Models

 - [BrcApi.Gear](../brc-react/docs/Gear.md)
 - [BrcApi.GradClimbReview](../brc-react/docs/GradClimbReview.md)
 - [BrcApi.Homework](../brc-react/docs/Homework.md)
 - [BrcApi.InstructorReview](../brc-react/docs/InstructorReview.md)
 - [BrcApi.LeavenworthReview](../brc-react/docs/LeavenworthReview.md)
 - [BrcApi.Lecture](../brc-react/docs/Lecture.md)
 - [BrcApi.Outing](../brc-react/docs/Outing.md)
 - [BrcApi.SkillsNightReview](../brc-react/docs/SkillsNightReview.md)
 - [BrcApi.Squamish1Review](../brc-react/docs/Squamish1Review.md)
 - [BrcApi.Squamish2Review](../brc-react/docs/Squamish2Review.md)
 - [BrcApi.Student](../brc-react/docs/Student.md)
 - [BrcApi.Update](../brc-react/docs/Update.md)


## Documentation for Authorization

 All endpoints do not require authorization.

