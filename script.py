sheets = {}
departments = {}
faculty = {}
training = {}
research = {} 	
newsFormat = {}

# generic function
def read_sheet(url):
	return 

def read_all_faculty_urls():
	return {
		"departments": string,
		"faculties": [] # array of string urls
	}

def read_faculty(url):
	return {
		"name": "",
		"introduction": "",
		"photo-link": "",
		"position": "",
		"research": [], # read_research function
		"training": [], # read_training function
	}

def read_training():
	return {
		"title": "",
		"date": "",
		"description": ""
	}

def read_research():
	return {
		"title": "",
		"pdf-link": "",
		"abstract": "",
		"year-published": 0,
		"authors": []
	}

def read_news():
	return {
		"title": "",
		"date-published": "",
		"author": "",
		"content": "",
		"tags": [],
		"cover-photo-link": ""
	}

training = read_training()
research = read_research()
news = read_news()
faculty = read_faculty(url)
