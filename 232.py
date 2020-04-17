# Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbox.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                temp = self.inbox.pop()
                self.outbox.append(temp)
        return self.outbox.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                temp = self.inbox.pop()
                self.outbox.append(temp)
        temp = self.outbox.pop()
        self.outbox.append(temp)
        return temp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inbox) == 0 and len(self.outbox) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
