from rest_framework import serializers

from .models import SkillsNightReview, LeavenworthReview, Squamish1Review, Squamish2Review, GradClimbReview, InstructorReview


class SkillsNightReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsNightReview
        fields = ['id', 'student', 'time', 'outing', 'rewoven_figure_8', 'figure_8_bight', 'prusik',
                  'bachmann', 'double_fisherman', 'water_knot', 'clove_hitch', 'munter_hitch', 'butterfly',
                  'euro_death_knot', 'rope_coiling', 'lead_belay', 'lead_fall', 'escape_belay',
                  'mechanical_autoblock', 'munter_rappel', 'clean_rappel_bolts', 'setting_bolted_anchor',
                  'ascending_rope', 'comments']


class LeavenworthReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeavenworthReview
        fields = ['id', 'student', 'instructor', 'time', 'outing', 'knots', 'belay', 'rappel', 'systems',
                  'anchor_safety',
                  'gear_placement', 'anchor_building', 'safety', 'efficiency', 'gear_cleaning', 'technique',
                  'routefinding', 'areas', 'current_comfort_grade', 'current_limit_grade', 'recommendation',
                  'comments', 'leavenworth_clean_and_rappel_bolts', 'guide_mode']


class Squamish1ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squamish1Review
        fields = ['id', 'student', 'instructor', 'time', 'outing', 'knots', 'belay', 'rappel', 'systems',
                  'anchor_safety',
                  'gear_placement', 'anchor_building', 'safety', 'efficiency', 'gear_cleaning', 'technique',
                  'routefinding', 'areas', 'current_comfort_grade', 'current_limit_grade', 'recommendation',
                  'comments', 'clean_and_rappel']


class Squamish2ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squamish2Review
        fields = ['id', 'student', 'instructor', 'time', 'outing', 'knots', 'belay', 'rappel', 'systems',
                  'anchor_safety',
                  'gear_placement', 'anchor_building', 'safety', 'efficiency', 'gear_cleaning', 'technique',
                  'routefinding', 'areas', 'current_comfort_grade', 'current_limit_grade', 'recommendation',
                  'comments', 'squamish2_transitions', 'squamish2_communication']


class GradClimbReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradClimbReview
        fields = ['id', 'student', 'instructor', 'time', 'outing', 'knots', 'belay', 'rappel', 'systems',
                  'anchor_safety',
                  'gear_placement', 'anchor_building', 'safety', 'efficiency', 'gear_cleaning', 'technique',
                  'routefinding', 'areas', 'current_comfort_grade', 'current_limit_grade', 'recommendation',
                  'comments', 'trip_planning', 'beta_sheet', 'transitions', 'communication']


class InstructorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorReview
        fields = ['id', 'instructor', 'author', 'outing', 'learning_style', 'explanations', 'demos', 'patience',
                  'did_well', 'did_bad', 'safety', 'comments']
