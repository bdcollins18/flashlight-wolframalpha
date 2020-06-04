def results(fields, original_query):
	input = fields['~input']
	return {
		"title": "TEST input='{0}'".format(input),
		"run_args": [input]
	}