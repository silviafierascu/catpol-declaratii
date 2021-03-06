from django import forms
from django.utils.translation import ugettext_lazy as _
from project_template import constants

YEAR_CHOICES = ('2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019')


class TranscribeInitialInformation(forms.Form):
    name = forms.CharField(label=_("What is the name of the current politician?"))
    surname = forms.CharField(label=_("What is the surname of the current politician?"))
    position = forms.CharField(label=_("What is the position of the current politician?"))
    date = forms.CharField(label=_("Date"), widget=forms.SelectDateWidget(years=YEAR_CHOICES))


class TranscribeDebtsTableRowsCount(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['debts']))


class TranscribeOwnedGoodsOrServicesPerSpouse(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['gifts_spouse']))


class TranscribeOwnedIncomeFromOtherSourcesTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['other_sources']))


class TranscribeOwnedInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['bank_accounts']))


class TranscribeOwnedJewelry(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['jewelry']))


class TranscribeOwnedAutomobile(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['automobiles']))


class TranscribeOwnedIncomeFromSalaries(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['salaries']))


class TranscribeOwnedIncomeFromGamblingTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['gambling']))


class TranscribeOwnedIncomeFromAgriculturalActivitiesTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['agriculture']))


class TranscribeIndependentActivities(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['independent_activities']))


class TranscribeOwnedIncomeFromDeferredUseOfGoods(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['deferred_use']))


class TranscribeOwnedIncomeFromPensionsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['pensions']))


class TranscribeOwnedIncomeFromInvestmentsTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['income_investments']))


class TranscribeOwnedGoodsOrServicesPerChildTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['gifts_kids']))


class TranscribeOwnedGoodsOrServicesPerOwnerTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['goods']))


class TranscribeOwnedLandTable(forms.Form):
    count = forms.IntegerField(label="How many filled rows are there in the table {}?".format(constants.DECLARATION_TABLES['land']))


class TranscribeOwnedBuildingsTable(forms.Form):
    address = forms.CharField(
        label="What is the address of the building?"
    )
    category = forms.CharField(
        label="What is the category of the building?"
    )
    attainment_year = forms.CharField(
        label="What is the attainment year of the building?"
    )
    surface = forms.CharField(
        label="What is the surface of the building?"
    )
    share = forms.CharField(
        label="What is the share in the building?"
    )
    attainment_type = forms.CharField(
        label="What is the way the building was attained?"
    )
    holder = forms.CharField(
        label="Who is the holder of the building?"
    )