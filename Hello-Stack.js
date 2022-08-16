var stackHolder = {
    count: 3,
    storage: [
        1,
        '{id: 1,value: "obj"}',
        "stringHolder",
        46
    ]
};

/**
 *
 * @param stackOperation (string): The operation to be performed on the stack
 * @param stackValue (any): The value to be used in the operation
 * @returns [] : Array
 */
function stack(stackOperation = "print", stackValue = undefined) {
    this.push = function (value) {
        if (value !== undefined) {
            stackHolder.count++;
            stackHolder.storage.push(value);
        }
        return stackHolder.storage;
    }

    this.pop = function () {
        if (stackHolder.count < 0) {
            return [];
        }

        stackHolder.count--;
        return [stackHolder.storage.pop()];
    }

    this.peek = function () {
        return [stackHolder.storage[stackHolder.count]];
    }

    this.swap = function () {
        if (stackHolder.count < 1) return stackHolder.storage;

        let temp = stackHolder.storage[stackHolder.count];
        stackHolder.storage[stackHolder.count] = stackHolder.storage[stackHolder.count - 1];
        stackHolder.storage[stackHolder.count - 1] = temp;
        return stackHolder.storage;
    }

    switch (stackOperation) {
        case 'push':
            return this.push(stackValue);
        case 'pop':
            return this.pop();
        case 'swap':
            return this.swap();
        case 'peek':
            return this.peek();
        default:
            return stackHolder.storage;
    }
}
