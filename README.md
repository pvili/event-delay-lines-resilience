# event-delay-lines-resilience
Code to investigate how to provide performance guarantees in delay-based spike pattern detectors
Launch from detectPositionsByDelayMatch

**#Data (positions/synthetic/times)**
Scorpion inspired neuromorphic touch sensor array to detect surface vibrations
Synthetic data

We provide synthetic data in the data/synthetic folder. There are taps arranged within two circles (resp. 0.5 & 1m radius), 1 tap per degree (720 taps in total).

    'positions.npy' [2,720] array, containing the positions [u,v] of the taps
    'times.npy' [8,720] array containing the spike times for each sensor.

Structure of the dataset

For brian2 simulation we provide a .npy file with size [2, N], where N is the number of spikes. The first row are the sensor ID's and the second row are the respective time stamps. The training data are spit according to location of taps. Location of real data: [ 0. 22.5 45. 67.5 90. 112.5 135. 157.5 180. 202.5 225. 247.5 270. 292.5 315. 337.5]
Dimensions of the sensor array

In total we have eight different sensors place on a octagon. The sensors are placed at: [ 0. 45. 90. 135. 180. 225. 270. 315.] degrees.

The maximum distance of any two orthogonal sensors is 30 cm.
