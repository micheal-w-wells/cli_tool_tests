# tests for wikipedia cli app
import wikipedia_cli


def test_can_call_wikipedia_api():
	assert False

def test_can_text_for_location():
	assert False

def test_can_get_population_from_text():
	input_string = 'some tesst input population is 123123123'
	population_ouput = wikipedia_cli.get_population_from_text(input_string)
	assert population_ouput == 123123123


def test_can_accept_command_line_args():
	assert False
