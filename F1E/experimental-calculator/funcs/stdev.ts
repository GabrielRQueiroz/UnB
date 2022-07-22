import Mean from './mean';

function StandardDeviation(values: number[], mean?: number) {
	!mean && (mean = Mean(values));

	let sum = 0;
	for (let i = 0; i < values.length; i++) {
		sum += Math.pow(values[i] - mean, 2);
	}
	return Math.sqrt(sum / (values.length * (values.length - 1)));
}

export default StandardDeviation;
