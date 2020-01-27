# BrcApi.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/jeanruggiero/brc-web/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gearGet**](DefaultApi.md#gearGet) | **GET** /gear | returns a list of all gear
[**homeworkGet**](DefaultApi.md#homeworkGet) | **GET** /homework | returns a list of homework matching the criteria
[**meetingsLecturesGet**](DefaultApi.md#meetingsLecturesGet) | **GET** /meetings/lectures | returns a list of lectures matching the criteria
[**meetingsOutingsGet**](DefaultApi.md#meetingsOutingsGet) | **GET** /meetings/outings | returns a list of outings matching the criteria
[**postsGet**](DefaultApi.md#postsGet) | **GET** /posts | returns a list of all course updates
[**reviewsGradClimbGet**](DefaultApi.md#reviewsGradClimbGet) | **GET** /reviews/grad_climb | returns a list of grad climb reviews
[**reviewsGradClimbIdGet**](DefaultApi.md#reviewsGradClimbIdGet) | **GET** /reviews/grad_climb/{id} | returns the grad climb review with the specified id
[**reviewsGradClimbIdPut**](DefaultApi.md#reviewsGradClimbIdPut) | **PUT** /reviews/grad_climb/{id} | updates an existing grad climb review
[**reviewsGradClimbPost**](DefaultApi.md#reviewsGradClimbPost) | **POST** /reviews/grad_climb | creates a new grad climb review
[**reviewsInstructorReviewGet**](DefaultApi.md#reviewsInstructorReviewGet) | **GET** /reviews/instructor_review | returns a list of instructor reviews matching the criteria
[**reviewsInstructorReviewIdGet**](DefaultApi.md#reviewsInstructorReviewIdGet) | **GET** /reviews/instructor_review/{id} | returns the instructor review with the specified id
[**reviewsInstructorReviewIdPut**](DefaultApi.md#reviewsInstructorReviewIdPut) | **PUT** /reviews/instructor_review/{id} | updates an existing instructor review
[**reviewsInstructorReviewPost**](DefaultApi.md#reviewsInstructorReviewPost) | **POST** /reviews/instructor_review | creates a new instructor review
[**reviewsLeavenworthGet**](DefaultApi.md#reviewsLeavenworthGet) | **GET** /reviews/leavenworth | returns a list of leavenworth reviews matching the criteria
[**reviewsLeavenworthIdGet**](DefaultApi.md#reviewsLeavenworthIdGet) | **GET** /reviews/leavenworth/{id} | returns the leavenworth review with specified id
[**reviewsLeavenworthIdPut**](DefaultApi.md#reviewsLeavenworthIdPut) | **PUT** /reviews/leavenworth/{id} | updates an existing leavenworth review
[**reviewsLeavenworthPost**](DefaultApi.md#reviewsLeavenworthPost) | **POST** /reviews/leavenworth | creates a new leavenworth review
[**reviewsSkillsNightGet**](DefaultApi.md#reviewsSkillsNightGet) | **GET** /reviews/skills_night | returns a list of skills night reviews matching the criteria
[**reviewsSkillsNightIdGet**](DefaultApi.md#reviewsSkillsNightIdGet) | **GET** /reviews/skills_night/{id} | returns the skills night review with the specified id
[**reviewsSkillsNightIdPut**](DefaultApi.md#reviewsSkillsNightIdPut) | **PUT** /reviews/skills_night/{id} | updates an existing skills night review
[**reviewsSkillsNightPost**](DefaultApi.md#reviewsSkillsNightPost) | **POST** /reviews/skills_night | creates a new skills night review
[**reviewsSquamish1Get**](DefaultApi.md#reviewsSquamish1Get) | **GET** /reviews/squamish1 | returns a list of squamish1 reviews matching the criteria
[**reviewsSquamish1IdGet**](DefaultApi.md#reviewsSquamish1IdGet) | **GET** /reviews/squamish1/{id} | returns the squamish1 review with the specified id
[**reviewsSquamish1IdPut**](DefaultApi.md#reviewsSquamish1IdPut) | **PUT** /reviews/squamish1/{id} | updates an existing squamish1 review
[**reviewsSquamish1Post**](DefaultApi.md#reviewsSquamish1Post) | **POST** /reviews/squamish1 | creates a new squamish1 review
[**reviewsSquamish2Get**](DefaultApi.md#reviewsSquamish2Get) | **GET** /reviews/squamish2 | returns a list of squamish2 reviews matching the criteria
[**reviewsSquamish2IdGet**](DefaultApi.md#reviewsSquamish2IdGet) | **GET** /reviews/squamish2/{id} | returns the squamish2 review with the specified id
[**reviewsSquamish2IdPut**](DefaultApi.md#reviewsSquamish2IdPut) | **PUT** /reviews/squamish2/{id} | updates an existing squamish2 review
[**reviewsSquamish2Post**](DefaultApi.md#reviewsSquamish2Post) | **POST** /reviews/squamish2 | creates a new squamish2 review
[**studentsGet**](DefaultApi.md#studentsGet) | **GET** /students | returns all students matching criteria
[**studentsIdGet**](DefaultApi.md#studentsIdGet) | **GET** /students/{id} | returns the student with the specified id
[**studentsIdPut**](DefaultApi.md#studentsIdPut) | **PUT** /students/{id} | updates an existing student's profile


<a name="gearGet"></a>
# **gearGet**
> [Gear] gearGet()

returns a list of all gear

Returns a list of all gear.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.gearGet(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Gear]**](Gear.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="homeworkGet"></a>
# **homeworkGet**
> [Homework] homeworkGet(opts)

returns a list of homework matching the criteria

Returns a list of homework matching the search criteria. If no search parameters are provided, all homework objects are returned.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'dueAfter': "dueAfter_example", // String | return all homework objects due after the specified date
  'dueBefore': "dueBefore_example" // String | return all homework objects due before the specified date
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.homeworkGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dueAfter** | **String**| return all homework objects due after the specified date | [optional] 
 **dueBefore** | **String**| return all homework objects due before the specified date | [optional] 

### Return type

[**[Homework]**](Homework.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="meetingsLecturesGet"></a>
# **meetingsLecturesGet**
> [Lecture] meetingsLecturesGet(opts)

returns a list of lectures matching the criteria

Returns a list of lectures matching the search criteria. If no search parameters are provided, all lectures are returned.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'occursAfter': "occursAfter_example", // String | return all lectures occurring after the specified date
  'occursBefore': "occursBefore_example" // String | return all lectures occurring before the specified date
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.meetingsLecturesGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **occursAfter** | **String**| return all lectures occurring after the specified date | [optional] 
 **occursBefore** | **String**| return all lectures occurring before the specified date | [optional] 

### Return type

[**[Lecture]**](Lecture.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="meetingsOutingsGet"></a>
# **meetingsOutingsGet**
> [Outing] meetingsOutingsGet(opts)

returns a list of outings matching the criteria

Returns a list of outings matching the search criteria. If no search parameters are provided, all outings are returned.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'occursAfter': "occursAfter_example", // String | return all outings occurring after the specified date
  'occursBefore': "occursBefore_example" // String | return all outings occurring before the specified date
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.meetingsOutingsGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **occursAfter** | **String**| return all outings occurring after the specified date | [optional] 
 **occursBefore** | **String**| return all outings occurring before the specified date | [optional] 

### Return type

[**[Outing]**](Outing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postsGet"></a>
# **postsGet**
> [Update] postsGet()

returns a list of all course updates

Returns a list of all course updates.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.postsGet(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Update]**](Update.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsGradClimbGet"></a>
# **reviewsGradClimbGet**
> [GradClimbReview] reviewsGradClimbGet(opts)

returns a list of grad climb reviews

Returns a list of grad climb reviews for the specified student and/or instructor.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'student': 56, // Number | id of a student
  'instructor': 56 // Number | id of a Django User of type Instructor
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsGradClimbGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | **Number**| id of a student | [optional] 
 **instructor** | **Number**| id of a Django User of type Instructor | [optional] 

### Return type

[**[GradClimbReview]**](GradClimbReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsGradClimbIdGet"></a>
# **reviewsGradClimbIdGet**
> Object reviewsGradClimbIdGet(id)

returns the grad climb review with the specified id

Returns the grad climb review with the specified id.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to get


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsGradClimbIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to get | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsGradClimbIdPut"></a>
# **reviewsGradClimbIdPut**
> reviewsGradClimbIdPut(id, review)

updates an existing grad climb review

Updates an existing review

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to update

var review = new BrcApi.GradClimbReview(); // GradClimbReview | Review to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsGradClimbIdPut(id, review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to update | 
 **review** | [**GradClimbReview**](GradClimbReview.md)| Review to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsGradClimbPost"></a>
# **reviewsGradClimbPost**
> reviewsGradClimbPost(review)

creates a new grad climb review

Creates a new review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var review = new BrcApi.GradClimbReview(); // GradClimbReview | Review to add


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsGradClimbPost(review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**GradClimbReview**](GradClimbReview.md)| Review to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsInstructorReviewGet"></a>
# **reviewsInstructorReviewGet**
> [InstructorReview] reviewsInstructorReviewGet(opts)

returns a list of instructor reviews matching the criteria

Returns a list of instructor reviews for the specified student and/or instructor.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'student': 56, // Number | id of a student
  'instructor': 56 // Number | id of a Django User of type Instructor
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsInstructorReviewGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | **Number**| id of a student | [optional] 
 **instructor** | **Number**| id of a Django User of type Instructor | [optional] 

### Return type

[**[InstructorReview]**](InstructorReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsInstructorReviewIdGet"></a>
# **reviewsInstructorReviewIdGet**
> Object reviewsInstructorReviewIdGet(id)

returns the instructor review with the specified id

Returns the instructor review with the specified id.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to get


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsInstructorReviewIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to get | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsInstructorReviewIdPut"></a>
# **reviewsInstructorReviewIdPut**
> reviewsInstructorReviewIdPut(id, review)

updates an existing instructor review

Updates an existing review

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to update

var review = new BrcApi.InstructorReview(); // InstructorReview | Review to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsInstructorReviewIdPut(id, review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to update | 
 **review** | [**InstructorReview**](InstructorReview.md)| Review to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsInstructorReviewPost"></a>
# **reviewsInstructorReviewPost**
> reviewsInstructorReviewPost(review)

creates a new instructor review

Creates a new review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var review = new BrcApi.InstructorReview(); // InstructorReview | Review to add


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsInstructorReviewPost(review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**InstructorReview**](InstructorReview.md)| Review to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsLeavenworthGet"></a>
# **reviewsLeavenworthGet**
> [LeavenworthReview] reviewsLeavenworthGet(opts)

returns a list of leavenworth reviews matching the criteria

Returns a list of leavenworth reviews for the specified student and/or instructor.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'student': 56, // Number | id of a student
  'instructor': 56 // Number | id of a Django User of type Instructor
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsLeavenworthGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | **Number**| id of a student | [optional] 
 **instructor** | **Number**| id of a Django User of type Instructor | [optional] 

### Return type

[**[LeavenworthReview]**](LeavenworthReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsLeavenworthIdGet"></a>
# **reviewsLeavenworthIdGet**
> Object reviewsLeavenworthIdGet(id)

returns the leavenworth review with specified id

Returns the leavenworth review with the specified id.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to retrieve


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsLeavenworthIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to retrieve | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsLeavenworthIdPut"></a>
# **reviewsLeavenworthIdPut**
> reviewsLeavenworthIdPut(id, review)

updates an existing leavenworth review

Updates an existing review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to update

var review = new BrcApi.LeavenworthReview(); // LeavenworthReview | Review to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsLeavenworthIdPut(id, review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to update | 
 **review** | [**LeavenworthReview**](LeavenworthReview.md)| Review to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsLeavenworthPost"></a>
# **reviewsLeavenworthPost**
> reviewsLeavenworthPost(review)

creates a new leavenworth review

Creates a new review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var review = new BrcApi.LeavenworthReview(); // LeavenworthReview | Review to add


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsLeavenworthPost(review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**LeavenworthReview**](LeavenworthReview.md)| Review to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsSkillsNightGet"></a>
# **reviewsSkillsNightGet**
> [SkillsNightReview] reviewsSkillsNightGet(opts)

returns a list of skills night reviews matching the criteria

Returns a list of skills night reviews for the specified student or instructor.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'student': 56, // Number | id of a student
  'instructor': 56 // Number | id of a Django User of type Instructor
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsSkillsNightGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | **Number**| id of a student | [optional] 
 **instructor** | **Number**| id of a Django User of type Instructor | [optional] 

### Return type

[**[SkillsNightReview]**](SkillsNightReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsSkillsNightIdGet"></a>
# **reviewsSkillsNightIdGet**
> Object reviewsSkillsNightIdGet(id)

returns the skills night review with the specified id

Returns the skills night review with the specified id.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to retrieve


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsSkillsNightIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to retrieve | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsSkillsNightIdPut"></a>
# **reviewsSkillsNightIdPut**
> reviewsSkillsNightIdPut(id, review)

updates an existing skills night review

Updates an existing review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to be modified

var review = new BrcApi.SkillsNightReview(); // SkillsNightReview | Review to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsSkillsNightIdPut(id, review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to be modified | 
 **review** | [**SkillsNightReview**](SkillsNightReview.md)| Review to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsSkillsNightPost"></a>
# **reviewsSkillsNightPost**
> reviewsSkillsNightPost(review)

creates a new skills night review

Creates a new review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var review = new BrcApi.SkillsNightReview(); // SkillsNightReview | Review to add


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsSkillsNightPost(review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**SkillsNightReview**](SkillsNightReview.md)| Review to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsSquamish1Get"></a>
# **reviewsSquamish1Get**
> [Squamish1Review] reviewsSquamish1Get(opts)

returns a list of squamish1 reviews matching the criteria

Returns a list of squamish1 reviews for the specified student and/or instructor.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'student': 56, // Number | id of a student
  'instructor': 56 // Number | id of a Django User of type Instructor
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsSquamish1Get(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | **Number**| id of a student | [optional] 
 **instructor** | **Number**| id of a Django User of type Instructor | [optional] 

### Return type

[**[Squamish1Review]**](Squamish1Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsSquamish1IdGet"></a>
# **reviewsSquamish1IdGet**
> Object reviewsSquamish1IdGet(id)

returns the squamish1 review with the specified id

Returns the squamish1 review object with the specified id.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to get


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsSquamish1IdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to get | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsSquamish1IdPut"></a>
# **reviewsSquamish1IdPut**
> reviewsSquamish1IdPut(id, review)

updates an existing squamish1 review

Updates an existing review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to update

var review = new BrcApi.Squamish1Review(); // Squamish1Review | Review to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsSquamish1IdPut(id, review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to update | 
 **review** | [**Squamish1Review**](Squamish1Review.md)| Review to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsSquamish1Post"></a>
# **reviewsSquamish1Post**
> reviewsSquamish1Post(review)

creates a new squamish1 review

Creates a new review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var review = new BrcApi.Squamish1Review(); // Squamish1Review | Review to add


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsSquamish1Post(review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**Squamish1Review**](Squamish1Review.md)| Review to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsSquamish2Get"></a>
# **reviewsSquamish2Get**
> [Squamish2Review] reviewsSquamish2Get(opts)

returns a list of squamish2 reviews matching the criteria

Returns a list of squamish2 reviews for the specified student and/or instructor.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'student': 56, // Number | id of a student
  'instructor': 56 // Number | id of a Django User of type Instructor
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsSquamish2Get(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **student** | **Number**| id of a student | [optional] 
 **instructor** | **Number**| id of a Django User of type Instructor | [optional] 

### Return type

[**[Squamish2Review]**](Squamish2Review.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsSquamish2IdGet"></a>
# **reviewsSquamish2IdGet**
> Object reviewsSquamish2IdGet(id)

returns the squamish2 review with the specified id

Returns the squamish2 review object with the specified id.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to retrieve


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.reviewsSquamish2IdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to retrieve | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="reviewsSquamish2IdPut"></a>
# **reviewsSquamish2IdPut**
> reviewsSquamish2IdPut(id, review)

updates an existing squamish2 review

Updates an existing review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of review to update

var review = new BrcApi.Squamish2Review(); // Squamish2Review | Review to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsSquamish2IdPut(id, review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of review to update | 
 **review** | [**Squamish2Review**](Squamish2Review.md)| Review to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="reviewsSquamish2Post"></a>
# **reviewsSquamish2Post**
> reviewsSquamish2Post(review)

creates a new squamish2 review

Creates a new review.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var review = new BrcApi.Squamish2Review(); // Squamish2Review | Review to add


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.reviewsSquamish2Post(review, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**Squamish2Review**](Squamish2Review.md)| Review to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="studentsGet"></a>
# **studentsGet**
> [Student] studentsGet(opts)

returns all students matching criteria

When called with no parameters, returns all students.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var opts = { 
  'lastName': "lastName_example", // String | pass an optional search string for looking up a student by last name
  'firstName': "firstName_example" // String | pass an optional search string for looking up a student by first name
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.studentsGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lastName** | **String**| pass an optional search string for looking up a student by last name | [optional] 
 **firstName** | **String**| pass an optional search string for looking up a student by first name | [optional] 

### Return type

[**[Student]**](Student.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="studentsIdGet"></a>
# **studentsIdGet**
> Object studentsIdGet(id)

returns the student with the specified id

When called with no parameters, returns all students.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of student to get


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.studentsIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of student to get | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="studentsIdPut"></a>
# **studentsIdPut**
> studentsIdPut(id, student)

updates an existing student's profile

Updates the profile of an existing student.

### Example
```javascript
var BrcApi = require('brc_api');

var apiInstance = new BrcApi.DefaultApi();

var id = 56; // Number | id of student to get

var student = new BrcApi.Student(); // Student | Student to update


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.studentsIdPut(id, student, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of student to get | 
 **student** | [**Student**](Student.md)| Student to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

