#include <ros/ros.h>
#include <wiringPiI2C.h>
#include "std_msgs/String.h"

using namespace std;

int main(int argc, char **argv) {
	
	wiringPiI2CSetup(1);

	ros::init(argc, argv, "i2c_node");
	ros::NodeHandle nh;

	ros::Publisher i2c_comm_pub = nh.advertise<std_msgs::String>("sensor_data", 100);

	ros::Rate loop_rate(10);


	while (ros::ok()) {
		std_msgs::String msg;
		
		i2c_comm_pub.publish(msg);

		ros::spinOnce();
		loop_rate.sleep();
	}


	return 0;
}
