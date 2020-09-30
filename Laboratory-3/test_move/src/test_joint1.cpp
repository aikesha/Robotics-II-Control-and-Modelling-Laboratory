#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include <math.h>   //for sin()

float X;


void joint1angleCallback(const std_msgs::Float64 msg)
{     
        if (X < msg.data)
        {
              X = msg.data;
        }
        ROS_INFO("X: %f", X);
        //ROS_INFO("  ");
}

int main(int argc, char **argv){
    ros::init(argc, argv, "joint1moving");
    X = 0;
    //float i = 0.00;

    ros::NodeHandle nh;

    ros::Publisher pub1 = nh.advertise<std_msgs::Float64>("/robot/joint1_position_controller/command", 100);
    ros::Subscriber sub1 = nh.subscribe("Aigerim_joint1_angle", 1, joint1angleCallback);

    ros::Rate loop_rate(1);
    ros::Time startTime = ros::Time::now();

    while (ros::ok()) {
                //  X = sin(i);
                  //if (X > 0)
                //  {
                //      X = 1;
               //   } else {
                //      X = 1;
                 // }
                   
                  std_msgs::Float64 msg_to_send;
                  msg_to_send.data = X;
                  pub1.publish(msg_to_send);
                  ROS_INFO("Moving joint 1 to position %f", X);
                  //i = i + 0.01;
                  ros::spinOnce();
                  loop_rate.sleep();
    }
   // return 0;
}
