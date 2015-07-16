import csv

class Data:
	'''
	Set up all data
	'''

	def __init__(self):
		self.split_number = 0.8
		self.feature_train = []
		self.labels_train = []

		self.feature_test = []
		self.labels_test = []

		self.data = csv.reader(open('data.csv'))

		total_features = []
		total_labels = []

		# Set up total dataset 
		for row in self.data:
			total_features.append(row[:-2])
			total_labels.append(row[-1])
		del total_features[0]
		del total_labels[0]

		total_features = [list(map(float, i)) for i in total_features]
		total_labels = map(float, total_labels)

		# Set up training and testing sets
		for i in range(int(len(total_features) * self.split_number)):
			self.feature_train.append(total_features[i])
			self.labels_train.append(total_labels[i])

		for i in range(int(len(total_features) * self.split_number), len(total_features)):
			self.feature_test.append(total_features[i])
			self.labels_test.append(total_labels[i])