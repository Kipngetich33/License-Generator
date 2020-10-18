import random
import json

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

	def __str__(self):
		valid = 'Invalid'
		if self.verify():
			valid = 'Valid'
		return self.key.upper() + ':' + valid

	def check_availability(self):
		with open('generated_keys.json') as f:
  			data = json.load(f)
			if self.key in data['generated_keys']:
				return True
			else:
				return False

	def add_generated_key(self):
		if self.check_availability():
			print("Key already available try again")
		else:
			with open("generated_keys.json", "r+") as file:
				data = json.load(file)
				data["generated_keys"].append(self.key)
				file.seek(0)  # rewind
				json.dump(data, file)
				file.truncate()

	

	