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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.BrcApi);
  }
}(this, function(expect, BrcApi) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('Outing', function() {
      beforeEach(function() {
        instance = new BrcApi.Outing();
      });

      it('should create an instance of Outing', function() {
        // TODO: update the code to test Outing
        expect(instance).to.be.a(BrcApi.Outing);
      });

      it('should have the property id (base name: "id")', function() {
        // TODO: update the code to test the property id
        expect(instance).to.have.property('id');
        // expect(instance.id).to.be(expectedValueLiteral);
      });

      it('should have the property title (base name: "title")', function() {
        // TODO: update the code to test the property title
        expect(instance).to.have.property('title');
        // expect(instance.title).to.be(expectedValueLiteral);
      });

      it('should have the property location (base name: "location")', function() {
        // TODO: update the code to test the property location
        expect(instance).to.have.property('location');
        // expect(instance.location).to.be(expectedValueLiteral);
      });

      it('should have the property startDate (base name: "startDate")', function() {
        // TODO: update the code to test the property startDate
        expect(instance).to.have.property('startDate');
        // expect(instance.startDate).to.be(expectedValueLiteral);
      });

      it('should have the property endDate (base name: "endDate")', function() {
        // TODO: update the code to test the property endDate
        expect(instance).to.have.property('endDate');
        // expect(instance.endDate).to.be(expectedValueLiteral);
      });

      it('should have the property objectives (base name: "objectives")', function() {
        // TODO: update the code to test the property objectives
        expect(instance).to.have.property('objectives');
        // expect(instance.objectives).to.be(expectedValueLiteral);
      });

      it('should have the property description (base name: "description")', function() {
        // TODO: update the code to test the property description
        expect(instance).to.have.property('description');
        // expect(instance.description).to.be(expectedValueLiteral);
      });

      it('should have the property itinerary (base name: "itinerary")', function() {
        // TODO: update the code to test the property itinerary
        expect(instance).to.have.property('itinerary');
        // expect(instance.itinerary).to.be(expectedValueLiteral);
      });

      it('should have the property campground (base name: "campground")', function() {
        // TODO: update the code to test the property campground
        expect(instance).to.have.property('campground');
        // expect(instance.campground).to.be(expectedValueLiteral);
      });

      it('should have the property campsite (base name: "campsite")', function() {
        // TODO: update the code to test the property campsite
        expect(instance).to.have.property('campsite');
        // expect(instance.campsite).to.be(expectedValueLiteral);
      });

      it('should have the property campingLocation (base name: "campingLocation")', function() {
        // TODO: update the code to test the property campingLocation
        expect(instance).to.have.property('campingLocation');
        // expect(instance.campingLocation).to.be(expectedValueLiteral);
      });

      it('should have the property campingCheckin (base name: "campingCheckin")', function() {
        // TODO: update the code to test the property campingCheckin
        expect(instance).to.have.property('campingCheckin');
        // expect(instance.campingCheckin).to.be(expectedValueLiteral);
      });

    });
  });

}));