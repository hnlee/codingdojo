import vanity

DEFAULT_NUMBER = '1-617-777-7777'

def test_empty_number():
	name = ''
	result = vanity.phone_number(name)

	assert result != name
	assert result == DEFAULT_NUMBER

def test_short_name():
	name = 'ben'
	result = vanity.phone_number(name)

	assert result != DEFAULT_NUMBER
	assert result == '1-617-777-7236'

def test_capitalize_short_name():
	name = 'JOE'
	result = vanity.phone_number(name)

	assert result != DEFAULT_NUMBER
	assert result == '1-617-777-7563'

def test_long_name():
	name = 'GERTELUYA'
	adjusted_name = 'GERTLYA' 
	result = vanity.phone_number(name)

	assert result != DEFAULT_NUMBER
	assert result == '1-617-437-8592', result

def test_super_long_name():
	name = 'thisisareallylongnamethatnoonewouldhavebutiwouldliketohavesomeday'
	adjusted_name = 'thieday'
	result = vanity.phone_number(name)

	assert result != DEFAULT_NUMBER
	assert result == '1-617-844-3329'

def test_seven_character_name():
	name = 'paulina'
	result = vanity.phone_number(name)

	assert result != DEFAULT_NUMBER
	assert result == '1-617-728-5462'

def test_name_with_number():
	name = 'seven7'
	result = vanity.phone_number(name)

	assert result != DEFAULT_NUMBER
	assert result == '1-617-773-8367'
