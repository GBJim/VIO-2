import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def read_imu_motions(file_path):
    imu_motions = []
    with open(file_path) as f:
        for line in f:
            imu_motions.append([float(value) for value in  line.strip().split(" ")[-6:]])
    return imu_motions

def compute_allan(imu_motions, window_size = 3):
    allan_dev = []
    allan_window = list(imu_motions[:window_size-1])
    for imu_motion in imu_motions[window_size:]:
        allan_window.append(imu_motion)
        allan_dev.append(np.std(allan_window, axis=0))
        allan_window.pop(0)
    return allan_dev

def plot_allan(allan_dev):
    gyro_x = allan_dev[:,0]
    gyro_y = allan_dev[:,1]
    gyro_z = allan_dev[:,2]
    acc_x = allan_dev[:,3]
    acc_y = allan_dev[:,4]
    acc_z = allan_dev[:,5]

    times = np.arange(acc.shape[1])
    plt.subplots_adjust(hspace=0.4)

    plt.subplot(121)
    plt.xlabel('Time(sec)')
    plt.ylabel('Message length --->')
    plt.title('Accleration: Allan Deviation')
    plt.loglog(acc, times)

    plt.subplot(122)
    plt.xlabel('Time(sec)')
    plt.ylabel('Message length --->')
    plt.title('Gyrometer: Allan Deviation')
    plt.loglog(gyro, times)

def main(file_path="../bin/imu_pose_noise.txt"):
    imu_motions = read_imu_motions(file_path)
    allan_dev = compute_allan(imu_motions)
    plot_allan(allan_dev);
    return allan_dev

if __name__  == "__main__":
    allan_dev = main()