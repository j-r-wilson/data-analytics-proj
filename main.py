import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import os

discrim_eval_df = pd.read_csv("discrim-eval-trimmed.csv").replace({True: 'True', False: 'False'})
winobias_df = pd.read_excel("winobias-trimmed.xlsx").replace({True: 'True', False: 'False'})

print(winobias_df['social inclination'] == 'pro')

winobias_correct_responses = [np.sum(winobias_df['base correct response'] == 'True'), 
                              np.sum(winobias_df['sbs correct response'] == 'True'), 
                              np.sum(winobias_df['cognitive correct response'] == 'True'), 
                              np.sum(winobias_df['sbs cognitive correct response'] == 'True'), 
                              np.sum(winobias_df['all correct responses'] == 'True')]

winobias_incorrect_responses = [np.sum(winobias_df['base correct response'] == 'False'), 
                                np.sum(winobias_df['sbs correct response'] == 'False'), 
                                np.sum(winobias_df['cognitive correct response'] == 'False'), 
                                np.sum(winobias_df['sbs cognitive correct response'] == 'False'), 
                                np.sum(winobias_df['all incorrect responses'] == 'True')]

winobias_response_totals = [winobias_correct_responses[-1], 
                            winobias_incorrect_responses[-1], 
                            len(winobias_df) - winobias_correct_responses[-1] - winobias_incorrect_responses[-1]]

socially_expected_winobias_correct_responses = [np.sum((winobias_df['base correct response'] == 'True') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['sbs correct response'] == 'True') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['cognitive correct response'] == 'True') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'True') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['all correct responses'] == 'True') & (winobias_df['social inclination'] == 'pro'))]

socially_non_expected_winobias_correct_responses = [np.sum((winobias_df['base correct response'] == 'True') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['sbs correct response'] == 'True') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['cognitive correct response'] == 'True') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'True') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['all correct responses'] == 'True') & (winobias_df['social inclination'] == 'anti'))]

socially_expected_winobias_incorrect_responses = [np.sum((winobias_df['base correct response'] == 'False') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['sbs correct response'] == 'False') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['cognitive correct response'] == 'False') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'False') & (winobias_df['social inclination'] == 'pro')), 
                              np.sum((winobias_df['all incorrect responses'] == 'True') & (winobias_df['social inclination'] == 'pro'))]

socially_non_expected_winobias_incorrect_responses = [np.sum((winobias_df['base correct response'] == 'False') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['sbs correct response'] == 'False') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['cognitive correct response'] == 'False') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'False') & (winobias_df['social inclination'] == 'anti')), 
                              np.sum((winobias_df['all incorrect responses'] == 'True') & (winobias_df['social inclination'] == 'anti'))]

male_winobias_correct_responses = [np.sum((winobias_df['base correct response'] == 'True') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['sbs correct response'] == 'True') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['cognitive correct response'] == 'True') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'True') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['all correct responses'] == 'True') & (winobias_df['answer gender'] == 'male'))]

female_winobias_correct_responses = [np.sum((winobias_df['base correct response'] == 'True') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['sbs correct response'] == 'True') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['cognitive correct response'] == 'True') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'True') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['all correct responses'] == 'True') & (winobias_df['answer gender'] == 'female'))]

male_winobias_incorrect_responses = [np.sum((winobias_df['base correct response'] == 'False') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['sbs correct response'] == 'False') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['cognitive correct response'] == 'False') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'False') & (winobias_df['answer gender'] == 'male')), 
                              np.sum((winobias_df['all incorrect responses'] == 'True') & (winobias_df['answer gender'] == 'male'))]

female_winobias_incorrect_responses = [np.sum((winobias_df['base correct response'] == 'False') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['sbs correct response'] == 'False') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['cognitive correct response'] == 'False') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['sbs cognitive correct response'] == 'False') & (winobias_df['answer gender'] == 'female')), 
                              np.sum((winobias_df['all incorrect responses'] == 'True') & (winobias_df['answer gender'] == 'female'))]


response_labels = ['Base Correct Response', 'SBS Correct Response', 'Cognitive Correct Response', 'SBS Cognitive Correct Response']
all_result_labels = ['All Correct', 'All Incorrect', 'Mixed Responses']

print(male_winobias_correct_responses)

colors = sns.color_palette('pastel')

overall_pie = plt.pie(winobias_response_totals, labels = all_result_labels, colors = colors, autopct='%.0f%%')
plt.show()

male_correct_hist = sns.barplot(y = male_winobias_correct_responses[0:4], x = response_labels, color=colors)
plt.show()

# fig, ax1 = plt.subplots()

# ax2 = ax1.twinx() 

# sns.histplot(winobias_df['base correct response'], ax=ax1, legend=True)
# sns.histplot(winobias_df['sbs correct response'], ax=ax2, legend=True)

# plt.show()

# # sns.histplot(data=winobias_df[], x="all correct responses", col="")

# # plt.show()