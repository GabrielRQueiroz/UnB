import prompts, { Answers, PromptObject } from 'prompts';
import Mean from './funcs/mean';
import StandardDeviation from './funcs/stdev';

const questions: Array<PromptObject> = [
	{
		type: 'select',
		name: 'separator',
		message: 'Which separator would you like to consider for the list?',
		choices: [
			{ title: '(,)', description: 'Comma', value: ',' },
			{ title: '(/)', description: 'Forward slash', value: '/' },
			{ title: '( )', description: 'Whitespace', value: ' ' },
		],
	},
	{
		type: 'list',
		name: 'values',
		message: 'Enter the values to be used in the calculation',
		separator: (prev) => prev,
		format: (value: string[]) => value.map((value: string) => parseFloat(value)),
		validate: (value: string) => {
			if (value.split(' ').length > 0) {
				if (value.split(' ').every((value: string) => !isNaN(parseFloat(value)))) {
					return true;
				}

				return 'All values must be numbers';
			} else {
				return 'You must enter at least one value';
			}
		},
	},
	// {
	// 	type: 'confirm',
	// 	name: 'shouldProceed',
	// 	message: (prev: number[]) => `Do you want to proceed with these values:\n${prev.join(', ')}?`,
	// 	initial: true,
	// 	onState: ({ value }) => {
	// 		if (value == false) {
	// 			process.exit();
	// 		}
	// 	},
	// },
	{
		type: 'toggle',
		name: 'shouldProceed',
		message: (prev: number[]) => `Do you want to proceed with these values:\n${prev.join(', ')}?`,
		initial: true,
		active: 'Ok',
		inactive: 'Cancel',
		onState: ({ value }) => {
			if (value == false) {
				process.exit();
			}

			return 'All values must be numbers';
		} else {
			return 'You must enter at least one value';
		}
	},
};

const confirmValues: PromptObject = {
	type: 'toggle',
	name: 'shouldProceed',
	message: (prev: number[]) => `Do you want to proceed with these values:\n${prev.join(', ')}?`,
	initial: true,
	active: 'Ok',
	inactive: 'Cancel',
	onState: ({ value }) => {
		if (value === false) {
			process.exit();
		}
	},
};

const selectFunctions: PromptObject = {
	type: 'multiselect',
	name: 'functions',
	message: 'Select the functions to be used in the calculation',
	choices: [
		{ title: 'Mean', value: 'mean' },
		{ title: 'Standard Deviation', value: 'stdev' },
	],
	min: 1,
};

const questions: Array<PromptObject> = [askValues, confirmValues, selectFunctions];

const onSubmit = (answers: Answers<string>) => {
	const { values, functions } = answers;

	console.log('~> Your entry:', values.join(', '));

	let mean: number;
	let stdev: number;

	functions.map((func: string) => {
		switch (func) {
			case 'mean':
				mean = Mean(values);
				console.log('> Mean: ', mean);
				break;
			case 'stdev':
				stdev = StandardDeviation(values, mean ? mean : undefined);
				console.log('> Standard Deviation: ', stdev);
				break;
		}
	});
};

const main = async () => await prompts(questions).then((response) => onSubmit(response));

main();
