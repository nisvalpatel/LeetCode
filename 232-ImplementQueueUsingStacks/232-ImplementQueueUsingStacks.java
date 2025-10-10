// Last updated: 10/9/2025, 8:10:44 PM
import java.util.Stack;

class MyQueue {

/* 
Stack<Integer> stack = new Stack<>();

stack.push(69);       // shoves 69 on top
int top = stack.pop(); // yeets the top off and returns it
int peek = stack.peek(); // looks at the top without removing it
boolean empty = stack.isEmpty(); // true if it’s empty, false if not
*/
    Stack<Integer> StackOne = new Stack<>();
    Stack<Integer> StackTwo = new Stack<>();
    public MyQueue() {

    }
    
    public void push(int x) {
        StackOne.push(x);
    }

    
    public int pop() {
        if (this.empty()){
            return 0;
        } else if (StackTwo.isEmpty()){
            while(!StackOne.isEmpty()){
                StackTwo.push(StackOne.pop());
            }
        }
        return StackTwo.pop();
    }
    
    public int peek() {

        if (this.empty()){
            return 0;
        } else if (StackTwo.isEmpty()){
            while(!StackOne.isEmpty()){
                StackTwo.push(StackOne.pop());
            }
        }
        return StackTwo.peek();
    }
    
    public boolean empty() {
        if (StackTwo.isEmpty() && StackOne.isEmpty()){
            return true;
        }
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */