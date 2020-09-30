#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include <math.h>   //for sin()

float X = 0;

void joint5angleCallback(const std_msgs::Float64 msg)
{
                      X = msg.data;
	ROS_INFO("X: %f", X);
}

int main(int argc, char **argv){
    float i = 0.0;
    float k; 
    ros::init(argc, argv, "joint5moving");

    ros::NodeHandle nh;

    ros::Publisher pub2 = nh.advertise<std_msgs::Float64>("/robot/joint5_position_controller/command", 10);
     ros::Subscriber sub2 = nh.subscribe("Aigerim_joint5_angle", 10, joint5angleCallback);
    ros::Rate loop_rate(10);
    ros::Time startTime = ros::Time::now();

    while (ros::ok()) {
			
                 k = sin(i);
                 if (k > 0) {
	k = 1;			
                  } else {
	k = 0;
                  }
                  std_msgs::Float64 msg_to_send;
                  msg_to_send.data = k;
                  pub2.publish(msg_to_send);
                  ROS_INFO("Moving joint 5 to position %f", msg_to_send.data);
                  i = i + 0.1;
                  ros::spinOnce();
                  loop_rate.sleep();
    }
   return 0;
}

