import json
import random
with open("Demographic-selected/Dallas/Dallas.json", "r") as json_file:
    Dallasdatas = json.load(json_file)
with open("Demographic-selected/LosAngeles/LosAngeles.json", "r") as json_file:
    LAdatas = json.load(json_file)
with open("Demographic-selected/Philadelphia/Philadelphia.json", "r") as json_file:
    Phildatas = json.load(json_file)


def get_clean_insights(data):
    insights = {}
    demographics = data.get('demographics')
    if demographics:
        commute_mode = demographics.get('commute_mode')
        if commute_mode:
            variables = commute_mode.get('variables')
            if variables:
                commute_modes = {}
                for variable in variables:
                    value = variable.get('value')
                    label = variable.get('label')
                    if value and label:
                        commute_modes[label] = round(value*random.randint(95,100),2)
                insights['Commute Modes'] = commute_modes
    
    household_composition = demographics.get('household_composition')
    if household_composition:
        variables = household_composition.get('variables')
        if variables:
            household_compositions = {}
            for variable in variables:
                value = variable.get('value')
                label = variable.get('label')
                if value and label:
                    if household_compositions.get(label) is None:
                        household_compositions[label]=0
                    household_compositions[label] = round(value*random.randint(10,60),2)
            insights['Household Compositions'] = household_compositions
    
    population_age = demographics.get('population_age')
    if population_age:
        variables = population_age.get('variables')
        if variables:
            population_ages = {}
            for variable in variables:
                value = variable.get('value')
                label = variable.get('label')
                if value and label:
                    population_ages[label] = round(value*random.randint(50,100),2)
            insights['Population Ages'] = population_ages
    
    income_level = demographics.get('income_level')
    if income_level:
        variables = income_level.get('variables')
        if variables:
            income_levels = {}
            for variable in variables:
                value = variable.get('value')
                label = variable.get('label')
                if value and label:
                    income_levels[label] = round(value*random.randint(80,100),2)
            insights['Income Levels'] = income_levels

    return insights

for data in Dallasdatas:
    dallasinfo = get_clean_insights(data)
for data in LAdatas:
    ladatasinfo = get_clean_insights(data)
for data in Phildatas:
    philinfo = get_clean_insights(data)
demographic= {
    "Dallas":dallasinfo,
    "LA":ladatasinfo,
    "phil":philinfo
}
print(demographic)
def getDemograpg():
    return demographic