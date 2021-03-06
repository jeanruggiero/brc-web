/*
 * BRC API
 * This is an API that allows access to Boealps BRC course and participant data.
 *
 * OpenAPI spec version: 1.0.0
 * Contact: jeanruggiero@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.10
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.BrcApi) {
      root.BrcApi = {};
    }
    root.BrcApi.Student = factory(root.BrcApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The Student model module.
   * @module model/Student
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>Student</code>.
   * @alias module:model/Student
   * @class
   * @param id {Number} 
   * @param lastName {String} 
   * @param firstName {String} 
   * @param email {String} 
   * @param phone {Number} 
   * @param streetAddress {String} 
   * @param city {String} 
   * @param state {String} 
   * @param zip {Number} 
   * @param insuranceCarrier {String} 
   * @param emergencyContact {String} 
   * @param emergencyContactPhone {Number} 
   */
  var exports = function(id, lastName, firstName, email, phone, streetAddress, city, state, zip, insuranceCarrier, emergencyContact, emergencyContactPhone) {
    this.id = id;
    this.lastName = lastName;
    this.firstName = firstName;
    this.email = email;
    this.phone = phone;
    this.streetAddress = streetAddress;
    this.city = city;
    this.state = state;
    this.zip = zip;
    this.insuranceCarrier = insuranceCarrier;
    this.emergencyContact = emergencyContact;
    this.emergencyContactPhone = emergencyContactPhone;
  };

  /**
   * Constructs a <code>Student</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Student} obj Optional instance to populate.
   * @return {module:model/Student} The populated <code>Student</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'Number');
      if (data.hasOwnProperty('lastName'))
        obj.lastName = ApiClient.convertToType(data['lastName'], 'String');
      if (data.hasOwnProperty('firstName'))
        obj.firstName = ApiClient.convertToType(data['firstName'], 'String');
      if (data.hasOwnProperty('nickname'))
        obj.nickname = ApiClient.convertToType(data['nickname'], 'String');
      if (data.hasOwnProperty('pronouns'))
        obj.pronouns = ApiClient.convertToType(data['pronouns'], 'String');
      if (data.hasOwnProperty('aboutMe'))
        obj.aboutMe = ApiClient.convertToType(data['aboutMe'], 'String');
      if (data.hasOwnProperty('favoriteClimb'))
        obj.favoriteClimb = ApiClient.convertToType(data['favoriteClimb'], 'String');
      if (data.hasOwnProperty('goalClimb'))
        obj.goalClimb = ApiClient.convertToType(data['goalClimb'], 'String');
      if (data.hasOwnProperty('funFact'))
        obj.funFact = ApiClient.convertToType(data['funFact'], 'String');
      if (data.hasOwnProperty('email'))
        obj.email = ApiClient.convertToType(data['email'], 'String');
      if (data.hasOwnProperty('phone'))
        obj.phone = ApiClient.convertToType(data['phone'], 'Number');
      if (data.hasOwnProperty('streetAddress'))
        obj.streetAddress = ApiClient.convertToType(data['streetAddress'], 'String');
      if (data.hasOwnProperty('city'))
        obj.city = ApiClient.convertToType(data['city'], 'String');
      if (data.hasOwnProperty('state'))
        obj.state = ApiClient.convertToType(data['state'], 'String');
      if (data.hasOwnProperty('zip'))
        obj.zip = ApiClient.convertToType(data['zip'], 'Number');
      if (data.hasOwnProperty('insuranceCarrier'))
        obj.insuranceCarrier = ApiClient.convertToType(data['insuranceCarrier'], 'String');
      if (data.hasOwnProperty('emergencyContact'))
        obj.emergencyContact = ApiClient.convertToType(data['emergencyContact'], 'String');
      if (data.hasOwnProperty('emergencyContactPhone'))
        obj.emergencyContactPhone = ApiClient.convertToType(data['emergencyContactPhone'], 'Number');
    }
    return obj;
  }

  /**
   * @member {Number} id
   */
  exports.prototype.id = undefined;

  /**
   * @member {String} lastName
   */
  exports.prototype.lastName = undefined;

  /**
   * @member {String} firstName
   */
  exports.prototype.firstName = undefined;

  /**
   * @member {String} nickname
   */
  exports.prototype.nickname = undefined;

  /**
   * @member {String} pronouns
   */
  exports.prototype.pronouns = undefined;

  /**
   * @member {String} aboutMe
   */
  exports.prototype.aboutMe = undefined;

  /**
   * @member {String} favoriteClimb
   */
  exports.prototype.favoriteClimb = undefined;

  /**
   * @member {String} goalClimb
   */
  exports.prototype.goalClimb = undefined;

  /**
   * @member {String} funFact
   */
  exports.prototype.funFact = undefined;

  /**
   * @member {String} email
   */
  exports.prototype.email = undefined;

  /**
   * @member {Number} phone
   */
  exports.prototype.phone = undefined;

  /**
   * @member {String} streetAddress
   */
  exports.prototype.streetAddress = undefined;

  /**
   * @member {String} city
   */
  exports.prototype.city = undefined;

  /**
   * @member {String} state
   */
  exports.prototype.state = undefined;

  /**
   * @member {Number} zip
   */
  exports.prototype.zip = undefined;

  /**
   * @member {String} insuranceCarrier
   */
  exports.prototype.insuranceCarrier = undefined;

  /**
   * @member {String} emergencyContact
   */
  exports.prototype.emergencyContact = undefined;

  /**
   * @member {Number} emergencyContactPhone
   */
  exports.prototype.emergencyContactPhone = undefined;

  return exports;

}));
