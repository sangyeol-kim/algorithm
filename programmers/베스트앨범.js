function solution(genres, plays) {
    const map = genres.reduce((prev, gen, index) => {
        if (prev[gen]) {
            prev[gen].playSum += plays[index];
            prev[gen].list.push([index, plays[index]]);
        } else {
            prev[gen] = {
                playSum: plays[index],
                list: [[index, plays[index]]],
            }
        }

        return prev;
    }, {});

    const values = Object.values(map);

    values.sort((a, b) => b.playSum - a.playSum);

    for (let i = 0; i < values.length; i++) {
        const value = values[i];

        // value.list.sort((a, b) => b[1] - a[1]);
        value.list.sort((a, b) => {
            if (b[1] > a[1]) {
                return 1;
            } else if (b[1] < a[1]) {
                return -1;
            } else {
                return a[0] - b[0];
            }
        });
    }

    return values.reduce((prev, item) => {
        prev.push(item.list[0][0]);

        if (item.list.length > 1) {
            prev.push(item.list[1][0]);
        }

        return prev;
    }, []);
}
