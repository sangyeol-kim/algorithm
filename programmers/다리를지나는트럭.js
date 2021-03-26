function solution(bridge_length, weight, truck_weights) {
    let result = 0;
    let nowWeight = 0;

    if (truck_weights.length === 0) {
        return result;
    }

    const queue = [];

    for (let i = 1; i < bridge_length; i++) {
        queue.push(0);
    }

    const firstTruck = truck_weights.shift();
    nowWeight = firstTruck;
    queue.push(firstTruck);
    result++;

    while (nowWeight !== 0) {
        result++;

        const prev = queue.shift();

        if (prev !== 0) {
            nowWeight -= prev;
        }

        let next = 0;

        if (truck_weights[0] && nowWeight + truck_weights[0] <= weight) {
            next = truck_weights.shift();

            nowWeight += next;
        }

        queue.push(next);
    }

    return result;
}
