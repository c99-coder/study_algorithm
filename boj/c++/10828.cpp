#include<iostream>
#include<string>
using namespace std;

int stack[10000];
int length=0;
string cmd;

int empty(){
    if (length == 0)
        return 1;
    return 0;
}

void push(int num){
    stack[length++]=num;
}

int pop(){
    if (empty())
        return -1;
    return stack[--length];
}

int size(){
    return length;
}

int top(){
    if (empty())
        return -1;
    return stack[length - 1];
}

int main(){
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        cin >> cmd;
        if (cmd == "push"){
            int num;
            cin >> num;
            push(num);
        }
        else if (cmd == "pop"){
            printf("%d\n", pop());
        }
        else if (cmd == "size"){
            printf("%d\n", size());
        }
        else if (cmd == "empty"){
            printf("%d\n", empty());
        }
        else if (cmd == "top"){
            printf("%d\n", top());
        }
    }
}