export function stack(stackOperation, stackValue) {
    var stackHolder = {
        count: 3,
        storage: [
            1,
            '{id: 1,value: "obj"}',
            "stringHolder",
            46
        ]
    };

    var push = function (value) {
        stackHolder.storage[stackHolder.count] = value;
        return stackHolder.storage;
    }

    var pop = function () {
        if (stackHolder.count === 0) {
            return [];
        }

        var poppedItem = stackHolder.storage[stackHolder.count];
        delete stackHolder.storage[stackHolder.count];
        stackHolder.count--;
        return poppedItem;
    }

    var peek = function () {
        return [stackHolder.storage[0]];
    }

    var swap = function () {
        return stackHolder.storage;
    }

    switch (stackOperation) {
        case 'push':
            push(stackValue);
            break;
        case 'pop':
            pop();
            break;
        case 'swap':
            swap();
            break;
        case 'peek':
            peek();
            break;
        default:
            return stackHolder.storage;
    }
}
