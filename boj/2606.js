// const fs = require('fs');
//
// const input = fs
//     .readFileSync("/dev/stdin", "utf8")
//     .toString()
//     .trim()
//     .split('\n');

const input = [7, 6, '1 2', '2 3', '3 4', '5 6', '7 8', '8 9', '9 1'];

const edges = input.slice(2, input.length).reduce((prev, i) => {
    const [n1, n2] = i.split(' ').map((s) => parseInt(s, 10));



    return prev;
}, new Map());

console.log(edges);

const dfs = (startNode) => {
    const visited = [];
    const needVisit = [startNode];

    while (needVisit.length !== 0) {
        const node = needVisit.pop();

        if (!visited.includes(node)) {
            visited.push(node);

            if (edges[node]) {
                needVisit.push(...edges[node]);
            }
        }
    }

    return visited;
}

console.log(dfs(1));
