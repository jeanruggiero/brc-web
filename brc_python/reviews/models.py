from django.db import models
from django.contrib.auth.models import User
import statistics


class Review(models.Model):
    student = models.ForeignKey('students.Student', models.SET_NULL, null=True)
    instructor = models.ForeignKey(User, models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now=True)
    outing = models.ForeignKey('meetings.Outing', models.SET_NULL, null=True)
    knots = models.IntegerField(null=True, blank=True)
    belay = models.IntegerField(null=True, blank=True)
    rappel = models.IntegerField(null=True, blank=True)
    systems = models.IntegerField(null=True, blank=True)
    anchor_safety = models.IntegerField(null=True, blank=True)
    gear_placement = models.IntegerField(null=True, blank=True)
    anchor_building = models.IntegerField(null=True, blank=True)
    safety = models.IntegerField(null=True, blank=True)
    efficiency = models.IntegerField(null=True, blank=True)
    gear_cleaning = models.IntegerField(null=True, blank=True)

    technique = models.IntegerField(null=True, blank=True)
    routefinding = models.IntegerField(null=True, blank=True)
    areas = models.TextField()
    current_comfort_grade = models.CharField(max_length=128)
    current_limit_grade = models.CharField(max_length=128)
    recommendation = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    # def __repr__(self):
    #     return self.student.name + ' | ' + str(self.outing) + ' | ' + \
    #            ' '.join([self.instructor.first_name, self.instructor.last_name])
    #
    def __str__(self):
        return '{} | {} | {} {}'.format(self.student, self.outing,
            self.instructor.first_name, self.instructor.last_name)


class SkillsNightReview(models.Model):
    student = models.ForeignKey('students.Student', models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now=True)
    outing = models.ForeignKey('meetings.Outing', models.SET_NULL, null=True)

    rewoven_figure_8 = models.IntegerField(null=True, blank=True)
    figure_8_bight = models.IntegerField(null=True, blank=True)
    prusik = models.IntegerField(null=True, blank=True)
    bachmann = models.IntegerField(null=True, blank=True)
    double_fisherman = models.IntegerField(null=True, blank=True)
    water_knot = models.IntegerField(null=True, blank=True)
    clove_hitch = models.IntegerField(null=True, blank=True)
    munter_hitch = models.IntegerField(null=True, blank=True)
    butterfly = models.IntegerField(null=True, blank=True)
    euro_death_knot = models.IntegerField(null=True, blank=True)
    rope_coiling = models.IntegerField(null=True, blank=True)

    lead_belay = models.IntegerField(null=True, blank=True)
    lead_fall = models.IntegerField(null=True, blank=True)
    escape_belay = models.IntegerField(null=True, blank=True)

    mechanical_autoblock = models.IntegerField(null=True, blank=True)
    munter_rappel = models.IntegerField(null=True, blank=True)
    clean_rappel_bolts = models.IntegerField(null=True, blank=True)

    setting_bolted_anchor = models.IntegerField(null=True, blank=True)
    ascending_rope = models.IntegerField(null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    @property
    def knots(self):
        return statistics.mean([self.rewoven_figure_8, self.figure_8_bight, self.prusik,
                                self.bachmann, self.double_fisherman, self.water_knot,
                                self.clove_hitch, self.munter_hitch, self.butterfly,
                                self.euro_death_knot, self.rope_coiling])

    @property
    def belay(self):
        return statistics.mean([self.lead_belay, self.lead_fall])

    @property
    def rappel(self):
        return statistics.mean([self.mechanical_autoblock, self.munter_rappel, self.clean_rappel_bolts])

    @property
    def systems(self):
        return statistics.mean([self.escape_belay, self.ascending_rope])


class LeavenworthReview(Review):
    leavenworth_clean_and_rappel_bolts = models.IntegerField(null=True, blank=True)
    guide_mode = models.IntegerField(null=True, blank=True)


class Squamish1Review(Review):
    clean_and_rappel = models.IntegerField(null=True, blank=True)


class Squamish2Review(Review):
    squamish2_transitions = models.IntegerField(null=True, blank=True)
    squamish2_communication = models.IntegerField(null=True, blank=True)


class GradClimbReview(Review):
    trip_planning = models.IntegerField(null=True, blank=True)
    beta_sheet = models.IntegerField(null=True, blank=True)
    transitions = models.IntegerField(null=True, blank=True)
    communication = models.IntegerField(null=True, blank=True)


class InstructorReview(models.Model):
    instructor = models.ForeignKey(User, models.SET_NULL, null=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True, related_name='reviews_authored')
    outing = models.ForeignKey('meetings.Outing', models.SET_NULL, null=True)
    learning_style = models.IntegerField(null=True, blank=True)
    explanations = models.IntegerField(null=True, blank=True)
    demos = models.IntegerField(null=True, blank=True)
    patience = models.IntegerField(null=True, blank=True)
    did_well = models.TextField(null=True, blank=True)
    did_bad = models.TextField(null=True, blank=True)
    safety = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __repr__(self):
        return '{} | {}'.format(self.instructor, self.outing)

    def __str__(self):
        return '{} | {}'.format(self.instructor, self.outing)
