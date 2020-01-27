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
    root.BrcApi.Outing = factory(root.BrcApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';

  /**
   * The Outing model module.
   * @module model/Outing
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>Outing</code>.
   * @alias module:model/Outing
   * @class
   * @param id {Number} 
   * @param title {String} 
   * @param location {String} 
   * @param startDate {String} 
   * @param endDate {String} 
   * @param objectives {String} 
   * @param description {String} 
   * @param itinerary {String} 
   */
  var exports = function(id, title, location, startDate, endDate, objectives, description, itinerary) {
    this.id = id;
    this.title = title;
    this.location = location;
    this.startDate = startDate;
    this.endDate = endDate;
    this.objectives = objectives;
    this.description = description;
    this.itinerary = itinerary;
  };

  /**
   * Constructs a <code>Outing</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Outing} obj Optional instance to populate.
   * @return {module:model/Outing} The populated <code>Outing</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'Number');
      if (data.hasOwnProperty('title'))
        obj.title = ApiClient.convertToType(data['title'], 'String');
      if (data.hasOwnProperty('location'))
        obj.location = ApiClient.convertToType(data['location'], 'String');
      if (data.hasOwnProperty('startDate'))
        obj.startDate = ApiClient.convertToType(data['startDate'], 'String');
      if (data.hasOwnProperty('endDate'))
        obj.endDate = ApiClient.convertToType(data['endDate'], 'String');
      if (data.hasOwnProperty('objectives'))
        obj.objectives = ApiClient.convertToType(data['objectives'], 'String');
      if (data.hasOwnProperty('description'))
        obj.description = ApiClient.convertToType(data['description'], 'String');
      if (data.hasOwnProperty('itinerary'))
        obj.itinerary = ApiClient.convertToType(data['itinerary'], 'String');
      if (data.hasOwnProperty('campground'))
        obj.campground = ApiClient.convertToType(data['campground'], 'String');
      if (data.hasOwnProperty('campsite'))
        obj.campsite = ApiClient.convertToType(data['campsite'], 'String');
      if (data.hasOwnProperty('campingLocation'))
        obj.campingLocation = ApiClient.convertToType(data['campingLocation'], 'String');
      if (data.hasOwnProperty('campingCheckin'))
        obj.campingCheckin = ApiClient.convertToType(data['campingCheckin'], 'String');
    }
    return obj;
  }

  /**
   * @member {Number} id
   */
  exports.prototype.id = undefined;

  /**
   * @member {String} title
   */
  exports.prototype.title = undefined;

  /**
   * @member {String} location
   */
  exports.prototype.location = undefined;

  /**
   * @member {String} startDate
   */
  exports.prototype.startDate = undefined;

  /**
   * @member {String} endDate
   */
  exports.prototype.endDate = undefined;

  /**
   * @member {String} objectives
   */
  exports.prototype.objectives = undefined;

  /**
   * @member {String} description
   */
  exports.prototype.description = undefined;

  /**
   * @member {String} itinerary
   */
  exports.prototype.itinerary = undefined;

  /**
   * @member {String} campground
   */
  exports.prototype.campground = undefined;

  /**
   * @member {String} campsite
   */
  exports.prototype.campsite = undefined;

  /**
   * @member {String} campingLocation
   */
  exports.prototype.campingLocation = undefined;

  /**
   * @member {String} campingCheckin
   */
  exports.prototype.campingCheckin = undefined;

  return exports;

}));
