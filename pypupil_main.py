#################################################################################
# AUTHOR : Suyeon Choi
# DATE : August 1, 2018
#
# Command line interface for pypupil
#################################################################################
import time
import sys
from pupil import Pupil

if __name__ == "__main__" :
    print("start eye tracker")

tracker = Pupil('9289');

while True:
    time.sleep(1)
    command = input('=' * 60 +
                    '\nPossible commands \n' +
                    '\t\t c (calibrate) \n' +
                    '\t\t g (get_data) \n' +
                    '\t\t exit \n' +
                    '=' * 60 +
                    '\nInput command : ')
    print('\n')

    
    if command == "c" or command == "calibrate":
        eyes = []
        cmd_eye = input('=' * 60 +
                        '\nSelect eyes to calibrate \n' +
                        '\t\t l (left) \n' +
                        '\t\t r (right) \n' +
                        '\t\t b (binocular) \n' +
                        '=' * 60 +
                        '\nInput command : ')
        if cmd_eye == "l" or cmd_eye == "left":
            eyes.append(1)
        elif cmd_eye == "r" or cmd_eye == "right":
            eyes.append(0)
        elif cmd_eye == "b" or cmd_eye == "binocular":
            eyes.append(0)
            eyes.append(1)
        else:
            continue

        cmd_dummy = input('=' * 60 +
                        '\nDummy?\n' +
                        '\t\t y (Use dummy) \n' +
                        '\t\t n (Do not use dummy) \n' +
                        '\nInput command : ')
        dummy = True if cmd_dummy == 'y' else False

        tracker.calibrate(eyes, dummy)


    elif command == "g" or command == "get_data":
        sync = False
        cmd_sync = input('=' * 60 +
                        '\nDo you want to synchronize? \n' +
                        '\t\t y (yes) \n' +
                        '\t\t n (no) \n' +
                        '=' * 60 +
                        '\nInput command : ')
        if cmd_sync == "y" or cmd_sync == "yes":
            sync = True
        elif cmd_sync == "n" or cmd_sync == "no":
            pass
        else:
            continue
        tracker._record(sync)


    elif command == "exit":
        sys.exit(1)


    elif command == "p":
        tracker._plot_graph()


    elif command == "t":
        tracker.calibrate([0, 1], True)
        tracker._record(True)


    elif command == "r":
        sync = True
        data = tracker.record(sync)
        data_processed = np.column_stack( (data['timestamp'], data['x'], data['y']) )

        curr_time = str(datetime.datetime.now().strftime('%y%m%d_%H%M%S'))
        file_name_prefix = 'eye_track_gaze_processed_data_'
        self._save_file(file_name_prefix + curr_time + '.mat', data_processed)
        self._save_file(file_name_prefix + curr_time + '_latest.mat', data_processed)
        print("Processed data saving...")
