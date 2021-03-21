function solution(clothes) {
    const clothMap = clothes.reduce((prev, cloth) => {
        const clothType = cloth[1];

        if (prev[clothType]) {
            prev[clothType]++;
        } else {
            prev[clothType] = 1;
        }

        return prev;
    }, {});

    return Object.values(clothMap).reduce((acc, clothCount) => acc * (clothCount + 1), 1) - 1;
}
