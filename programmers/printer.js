function solution(priorities, location) {
    let result = 0;
    let nowLocation = location;

    let highPriority = Math.max(...priorities);

    while (true) {
        const headPriority = priorities.shift();

        if (headPriority === highPriority) {
            result++;

            if (nowLocation === 0) {
                break;
            }

            highPriority = Math.max(...priorities);
        } else {
            priorities.push(headPriority);

            if (nowLocation === 0) {
                nowLocation = priorities.length;
            }
        }

        nowLocation--;
    }

    return result;
}
