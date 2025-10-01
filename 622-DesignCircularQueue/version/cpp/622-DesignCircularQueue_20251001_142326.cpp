// Last updated: 10/1/2025, 2:23:26 PM
#include <vector>
#include <algorithm>
class MyCircularQueue {
public:
    int front;
    int back;
    std::vector<int> _data;
    int size;
    int empty; 
    //empty = 1, full
    //empty = 0, not full
    //empty = -1, empty

    MyCircularQueue(int k) {
        back = 0;
        front = 0;
        _data.resize(k);
        size = k;
        empty = -1;
    }
    
    bool enQueue(int value) {
        if (isFull()){
            return false;
        }
        _data[back] = value;

        back += 1;
        back %= size;

        if (back == front){
            empty = 1;
        }else{
            empty = 0;
        }
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()){
            return false;
        }

        front += 1;
        front %= size;

        if (back == front){
            empty = -1;
        }else{
            empty = 0;
        }
        return true;

    }
    
    int Front() {
        if(isEmpty()){
            return -1;
        }
        return _data[front];
    }
    
    int Rear() {
        if(isEmpty()){
            return -1;
        }
        int temp = back - 1;
        if (temp < 0){
            return _data[size - 1];
        }
        return _data[temp];
    }
    
    bool isEmpty() {
        if (empty == -1){
            return true;
        }
        return false;

    }
    
    bool isFull() {
        if (empty == 1){
            return true;
        }
        return false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */