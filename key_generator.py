import random,json,requests

class Key:

	def __init__(self, key=''):
		if key == '':
			self.key= self.generate()
		else:
			self.key = key.lower()

	def verify(self):
		score = 0
		check_digit = self.key[0]
		check_digit_count = 0
		chunks = self.key.split('-')
		for chunk in chunks:
			if len(chunk) != 4:
				return False
			for char in chunk:
				if char == check_digit:
					check_digit_count += 1
				score += ord(char)
		if score == 1772 and check_digit_count == 3:
			return True
		return False

	def generate(self):
		key = ''
		chunk = ''
		check_digit_count = 0
		alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
		while True:
			while len(key) < 25:
				char = random.choice(alphabet)
				key += char
				chunk += char
				if len(chunk) == 4:
					key += '-'
					chunk = ''
			key = key[:-1]
			if Key(key).verify():
				if Key(key).check_availability():
					key = ''
				else:
					return key
			else:
				key = ''

	def check_availability(self):
		with open('generated_keys.json') as f:
  			data = json.load(f)
			if self.key in data['generated_keys'].keys():
				return True
			else:
				return False

	def get_license_time_from_amount(self):
		def enter_amount():
			print("*"*80)
			print("Enter Amount below:")
			# ask user to enter amount paid
			raw_input_amount = raw_input()
			try:
				input_amount = int(raw_input_amount)
				# check if amount if given
				if input_amount:
					# check if amount is in the rates
					with open("license_rates.json", "r") as file:
						license_rates = json.load(file)
						if input_amount in license_rates['periods_n_amount'].values():
							# get the license time period
							for licence_period,license_amount in license_rates['periods_n_amount'].items():
								if input_amount == license_amount:
									# if license time in seconds
									license_time = license_rates['period_n_time_in_seconds'][licence_period]
									return {'period_name':licence_period,'time_in_seconds':license_time}
						else:
							print("Entered amount does not match any license period n\
								The rates are as follows:")
							for license_period in license_rates['periods_n_amount'].keys():
								print("{} => {}".format(license_period,\
									license_rates['periods_n_amount'][license_period]))
							# call the function again
							enter_amount() 					
				else:
					print('You did not enter an amount')
					enter_amount()
			except:
				print("Amounts are only accepted as number/integers")
				# call the function again
				enter_amount() 

			
		# get license period and amount
		licence_period_n_time =  enter_amount()
		# return the license times from amount
		return licence_period_n_time

	def add_generated_key(self,license_key_dict):
		if self.check_availability():
			print("This license key has already been saved")
		else:
			with open("generated_keys.json", "r+") as file:
				data = json.load(file)
				data["generated_keys"][license_key_dict['unique_license_key']] = license_key_dict
				file.seek(0)  # rewind
				json.dump(data, file)
				file.truncate()

	def __str__(self):
		valid = 'Invalid'
		if self.verify():
			valid = 'Valid'
		return self.key.upper() + ':' + valid

	def main(self):
		# get license time from amount
		license_from_amount =  self.get_license_time_from_amount()
		# get unique license key
		unique_license_key = self.generate()
		# combine license key and time as key and value
		license_key_n_time_in_secs = {'unique_license_key':unique_license_key,\
			'time':license_from_amount['time_in_seconds'],
			'period_name':license_from_amount['period_name']
			}
		# now save the generated key
		self.add_generated_key(license_key_n_time_in_secs)
		print("Sucessfully generated and saved a {} licence.Please commit the changes and push the changes online\
			".format(license_from_amount['period_name']))
		print("#"*80)
		print("Send below License Details to Client")
		print(license_key_n_time_in_secs)
		print("#"*80)

		




	

	