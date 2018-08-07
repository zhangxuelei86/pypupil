% best data is 172530
close all;

load('C:\Users\User\Desktop\pypupil\data\eye_track_before_calib_data_latest.mat')
x = data(:, 2);
y = data(:, 3);
%c = linspace(1, 10, length(x));
c = data(:, 4);
fig1 = figure;
subplot(2,1,1);
scatter(x, y, 5, c, 'filled')
title('Before transform (Both eyes)'); xlabel('[relative unit]'); ylabel('[relative unit]'); 

load('C:\Users\User\Desktop\pypupil\data\eye_track_after_calib_data_latest.mat')
x = data(:, 2);
y = data(:, 3);
%c = linspace(1, 10, length(x));
c = data(:, 4);
subplot(2,1,2);
scatter(x, y, 5, c, 'filled')
xlim ([-2.5 2.5])
ylim ([-1.5 1.5])
title('After transform (Both eyes)'); xlabel('[relative unit]'); ylabel('[relative unit]'); 

%%%% Before Average
load('C:\Users\User\Desktop\pypupil\data\eye_track_gaze_raw_data_latest.mat')
x = data(:, 2);
y = data(:, 3);

i_left = data(:, 4) == 1;
i_right = data(:, 4) == 0;
data_left = data(i_left,:);
data_right = data(i_right,:);

x_left = data_left(:, 2);
y_left = data_left(:, 3);
x_right = data_right(:, 2);
y_right = data_right(:, 3);

%c = linspace(1, 10, length(x));
c = data_left(:, 4);


%%%%% PLOT GRAPH
fig2 = figure;

subplot(2,1,1);
scatter(x_left, y_left, 5, 'y', 'filled')
axis tight;
xlim ([-2.5 2.5])
ylim ([-1.5 1.5])
title('Own gaze data (Left eye)'); xlabel('[relative unit]'); ylabel('[relative unit]'); 

subplot(2,1,2);
scatter(x_right, y_right, 5, 'b', 'filled')
xlim ([-2.5 2.5])
ylim ([-1.5 1.5])
title('Own gaze data (Right eye)'); xlabel('[relative unit]'); ylabel('[relative unit]'); 
set(fig1,'Position',[400 0 500 1000])
set(fig2,'Position',[900 0 500 1000])






%%%% After Average (Synchronization)
load('C:\Users\User\Desktop\pypupil\data\eye_track_gaze_processed_data_latest.mat')
x = data(:, 2);
y = data(:, 3);
%c = data(:, 1);

fig3 = figure;
scatter(x, y, 5, [0 0 0], 'filled')
xlim ([-2.5 2.5])
ylim ([-1.5 1.5])
title('After Synchonization (Both eyes)'); xlabel('[relative unit]'); ylabel('[relative unit]'); 
