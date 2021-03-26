function solution(participant, completion) {
    const completionMap = completion.reduce((prev, person) => {
        const personCount = prev.get(person);

        if (personCount) {
            prev.set(person, personCount + 1);
        } else {
            prev.set(person, 1);
        }

        return prev;
    }, new Map());

    for (let i = 0; i < participant.length; i++) {
        const person = participant[i];

        const targetPerson = completionMap.get(person);

        if (!targetPerson) {
            return person;
        }

        completionMap.set(person, targetPerson - 1)
    }
}
