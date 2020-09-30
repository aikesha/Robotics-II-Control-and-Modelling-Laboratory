#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include <math.h>   //for sin()

int main(int argc, char **argv){
    ros::init(argc, argv, "joint1sine");
    //X = 0;
    float t = 0.00;

    ros::NodeHandle nh;

    ros::Publisher pub1 = nh.advertise<std_msgs::Float64>("/robot/joint1_position_controller/command", 100);

    ros::Rate loop_rate(10);
    ros::Time startTime = ros::Time::now();

    while (ros::ok()) {
                  t = ros::Time::now().toSec();
                  std_msgs::Float64 msg_to_send;
                  msg_to_send.data = sin(t);
                  pub1.publish(msg_to_send);
                  ROS_INFO("Moving joint 1 to position %f", msg_to_send.data);
                  //i = i + 0.01;
                  ros::spinOnce();
                  loop_rate.sleep();
    }
   // return 0;
}
