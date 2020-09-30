#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include <math.h>   //for sin()

float X;


void joint5angleCallback(const std_msgs::Float64 msg)
{     
        if (X < msg.data)
        {
              X = msg.data;
        }
        ROS_INFO("X: %f", X);
        //ROS_INFO("  ");
}

int main(int argc, char **argv){
    ros::init(argc, argv, "joint5moving");
    X = 0;
    //float i = 0.00;

    ros::NodeHandle nh;

    ros::Publisher pub2 = nh.advertise<std_msgs::Float64>("/robot/joint5_position_controller/command", 100);
    ros::Subscriber sub2 = nh.subscribe("Aigerim_joint5_angle", 1, joint5angleCallback);

    ros::Rate loop_rate(10);
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
                  pub2.publish(msg_to_send);
                  ROS_INFO("Moving joint 5");
                  //i = i + 0.01;
                  ros::spinOnce();
                  loop_rate.sleep();
    }
   // return 0;
}
