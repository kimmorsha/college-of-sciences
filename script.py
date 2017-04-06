sheets = {}
departments = {}
faculty = {}
training = {}
research = {}
newsFormat = {}

# generic function
def read_sheet(url):
	return read_faculty, read_all_faculty_url

def read_all_faculty_urls():
	return {
		"departments": []
		"faculties": [],
	}

def read_faculty_by_department():
	return {

	}

def read_faculty(url):
	return {
		"name": "",
		"introduction": "",
		"photo-link": "",
		"position": "",
		"research": [],
		"training": [],
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
