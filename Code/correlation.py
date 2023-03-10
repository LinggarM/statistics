import numpy as np
import math

feature_1 = np.arange(10)
feature_2 = np.arange(9, -1, -1)

def variance(feature):
	# Calculate the mean
	mean = sum(feature)/len(feature)

	# Calculate the variance
	try :
		total = 0
		for i in range(len(feature)):
			substracted = (feature[i] - mean)
			total += substracted * substracted
		var = total/len(feature)
		return var
	except :
		print("Variance uncalculated")


def covariance(feature_1, feature_2):
	# Check the length of 2 variables
	if len(feature_1) != len(feature_2):
		print("The variables should have the same length")
		return 0

	# Calculate the mean of 2 variables
	mean_1 = sum(feature_1)/len(feature_1)
	mean_2 = sum(feature_2)/len(feature_2)

	# Calculate the covariance
	try :
		total = 0
		for i in range(len(feature_1)):
			total += (feature_1[i] - mean_1) * (feature_2[i] - mean_2)
		cov = total/len(feature_1)
		return cov
	except :
		print("Covariance uncalculated")

def pearson_corr(feature_1, feature_2):
	# Calculate the Pearson Correlation Coefficient
	try :
		return covariance(feature_1, feature_2) / (math.sqrt(variance(feature_1)) * math.sqrt(variance(feature_2)))
	except :
		print("Pearson Correlation Coefficient uncalculated")

print(f"Variance x: {variance(feature_1)}")
print(f"Variance x (Covariance x & x): {covariance(feature_1, feature_1)}")
print(f"Covariance x & y: {covariance(feature_1, feature_2)}")
print(f"Pearson Correlation Coefficient x & y: {pearson_corr(feature_1, feature_2)}")