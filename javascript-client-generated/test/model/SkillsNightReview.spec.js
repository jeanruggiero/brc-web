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
    describe('SkillsNightReview', function() {
      beforeEach(function() {
        instance = new BrcApi.SkillsNightReview();
      });

      it('should create an instance of SkillsNightReview', function() {
        // TODO: update the code to test SkillsNightReview
        expect(instance).to.be.a(BrcApi.SkillsNightReview);
      });

      it('should have the property student (base name: "student")', function() {
        // TODO: update the code to test the property student
        expect(instance).to.have.property('student');
        // expect(instance.student).to.be(expectedValueLiteral);
      });

      it('should have the property time (base name: "time")', function() {
        // TODO: update the code to test the property time
        expect(instance).to.have.property('time');
        // expect(instance.time).to.be(expectedValueLiteral);
      });

      it('should have the property outing (base name: "outing")', function() {
        // TODO: update the code to test the property outing
        expect(instance).to.have.property('outing');
        // expect(instance.outing).to.be(expectedValueLiteral);
      });

      it('should have the property rewovenFigure8 (base name: "rewoven_figure_8")', function() {
        // TODO: update the code to test the property rewovenFigure8
        expect(instance).to.have.property('rewovenFigure8');
        // expect(instance.rewovenFigure8).to.be(expectedValueLiteral);
      });

      it('should have the property figure8Bight (base name: "figure_8_bight")', function() {
        // TODO: update the code to test the property figure8Bight
        expect(instance).to.have.property('figure8Bight');
        // expect(instance.figure8Bight).to.be(expectedValueLiteral);
      });

      it('should have the property prusik (base name: "prusik")', function() {
        // TODO: update the code to test the property prusik
        expect(instance).to.have.property('prusik');
        // expect(instance.prusik).to.be(expectedValueLiteral);
      });

      it('should have the property bachmann (base name: "bachmann")', function() {
        // TODO: update the code to test the property bachmann
        expect(instance).to.have.property('bachmann');
        // expect(instance.bachmann).to.be(expectedValueLiteral);
      });

      it('should have the property doubleFisherman (base name: "double_fisherman")', function() {
        // TODO: update the code to test the property doubleFisherman
        expect(instance).to.have.property('doubleFisherman');
        // expect(instance.doubleFisherman).to.be(expectedValueLiteral);
      });

      it('should have the property waterKnot (base name: "water_knot")', function() {
        // TODO: update the code to test the property waterKnot
        expect(instance).to.have.property('waterKnot');
        // expect(instance.waterKnot).to.be(expectedValueLiteral);
      });

      it('should have the property cloveHitch (base name: "clove_hitch")', function() {
        // TODO: update the code to test the property cloveHitch
        expect(instance).to.have.property('cloveHitch');
        // expect(instance.cloveHitch).to.be(expectedValueLiteral);
      });

      it('should have the property munterHitch (base name: "munter_hitch")', function() {
        // TODO: update the code to test the property munterHitch
        expect(instance).to.have.property('munterHitch');
        // expect(instance.munterHitch).to.be(expectedValueLiteral);
      });

      it('should have the property butterfly (base name: "butterfly")', function() {
        // TODO: update the code to test the property butterfly
        expect(instance).to.have.property('butterfly');
        // expect(instance.butterfly).to.be(expectedValueLiteral);
      });

      it('should have the property euroDeathKnot (base name: "euro_death_knot")', function() {
        // TODO: update the code to test the property euroDeathKnot
        expect(instance).to.have.property('euroDeathKnot');
        // expect(instance.euroDeathKnot).to.be(expectedValueLiteral);
      });

      it('should have the property ropeCoiling (base name: "rope_coiling")', function() {
        // TODO: update the code to test the property ropeCoiling
        expect(instance).to.have.property('ropeCoiling');
        // expect(instance.ropeCoiling).to.be(expectedValueLiteral);
      });

      it('should have the property leadBelay (base name: "lead_belay")', function() {
        // TODO: update the code to test the property leadBelay
        expect(instance).to.have.property('leadBelay');
        // expect(instance.leadBelay).to.be(expectedValueLiteral);
      });

      it('should have the property leadFall (base name: "lead_fall")', function() {
        // TODO: update the code to test the property leadFall
        expect(instance).to.have.property('leadFall');
        // expect(instance.leadFall).to.be(expectedValueLiteral);
      });

      it('should have the property escapeBelay (base name: "escape_belay")', function() {
        // TODO: update the code to test the property escapeBelay
        expect(instance).to.have.property('escapeBelay');
        // expect(instance.escapeBelay).to.be(expectedValueLiteral);
      });

      it('should have the property mechanicalAutoblock (base name: "mechanical_autoblock")', function() {
        // TODO: update the code to test the property mechanicalAutoblock
        expect(instance).to.have.property('mechanicalAutoblock');
        // expect(instance.mechanicalAutoblock).to.be(expectedValueLiteral);
      });

      it('should have the property munterRappel (base name: "munter_rappel")', function() {
        // TODO: update the code to test the property munterRappel
        expect(instance).to.have.property('munterRappel');
        // expect(instance.munterRappel).to.be(expectedValueLiteral);
      });

      it('should have the property cleanRappelBolts (base name: "clean_rappel_bolts")', function() {
        // TODO: update the code to test the property cleanRappelBolts
        expect(instance).to.have.property('cleanRappelBolts');
        // expect(instance.cleanRappelBolts).to.be(expectedValueLiteral);
      });

      it('should have the property settingBoltedAnchor (base name: "setting_bolted_anchor")', function() {
        // TODO: update the code to test the property settingBoltedAnchor
        expect(instance).to.have.property('settingBoltedAnchor');
        // expect(instance.settingBoltedAnchor).to.be(expectedValueLiteral);
      });

      it('should have the property ascendingRope (base name: "ascending_rope")', function() {
        // TODO: update the code to test the property ascendingRope
        expect(instance).to.have.property('ascendingRope');
        // expect(instance.ascendingRope).to.be(expectedValueLiteral);
      });

      it('should have the property comments (base name: "comments")', function() {
        // TODO: update the code to test the property comments
        expect(instance).to.have.property('comments');
        // expect(instance.comments).to.be(expectedValueLiteral);
      });

    });
  });

}));