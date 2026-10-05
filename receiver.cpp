#include<bits/stdc++.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include <arpa/inet.h>
using namespace std;

#define SENDER_PORT 6000
#define RECEIVER_PORT 6001

int main(){
    int socketfd=socket(PF_INET,SOCK_DGRAM,0);

    sockaddr_in sender_addr;
    sender_addr.sin_family=AF_INET;
    sender_addr.sin_port=htons(SENDER_PORT);
    inet_aton("127.0.0.1",&(sender_addr.sin_addr));
    memset(&(sender_addr.sin_zero),'\0',8);

    sockaddr_in receiver_addr;
    receiver_addr.sin_family=AF_INET;
    receiver_addr.sin_port=htons(RECEIVER_PORT);
    inet_aton("127.0.0.1",&(receiver_addr.sin_addr));
    memset(&(receiver_addr.sin_zero),'\0',8);

    if(bind(socketfd,(sockaddr *)&receiver_addr,sizeof(sockaddr))==-1){
        cout<<"Receiver Binding Failed\n";
    }

    char buf[64];
    int x=sizeof(sockaddr);
    recvfrom(socketfd,(void *)&buf,64,0,(sockaddr*)&sender_addr,(socklen_t*)&x);
    int i=0;
    while(buf[i]!='\0'){
        cout<<buf[i++];
    }
    cout<<'\n';

}