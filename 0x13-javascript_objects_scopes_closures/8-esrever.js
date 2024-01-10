#!/usr/bin/node
exports.esrever = function (list) {
	const arg = [];

	for (let i = list.length - 1; i >= 0; i--) {
		arg.push(list[i]);
	}
	return arg;
}
