% input - length of dataset or length of feature-label pairs

function [feature, label] = create_dataset(data_size)

planarrobot_student;

% just take a random value of q --> feature
% calculate the IK --> label
% return

% https://www.mathworks.com/help/matlab/math/floating-point-numbers-within-specific-range.html

rng(0,'twister');

% q1
q_min = -114;
q_max = 114;
q1 = (q_max-q_min).*rand(data_size,1) + q_min;

% q2
q_min = -60;
q_max = 60;
q2 = (q_max-q_min).*rand(data_size,1) + q_min;

% q3
q_min = -100;
q_max = 100;
q3 = (q_max-q_min).*rand(data_size,1) + q_min;

% q4
q_min = -50;
q_max = 50;
q4 = (q_max-q_min).*rand(data_size,1) + q_min;

% q5
q_min = -50;
q_max = 50;
q5 = (q_max-q_min).*rand(data_size,1) + q_min;
% 
q = [q1, q2, q3, q4, q5]*deg;
pose_robot = zeros(data_size,3);
ang_robot = zeros(data_size, 5);

for i=1:data_size
   
    pose_end = planar_robot.fkine(q(i, :));
    xyz = transl(pose_end);
   
    % also more labels can be added
    pose_robot(i, :) =  xyz;
    
    T = Rototr(q(i,:), lee);
    
    qi = planar_robot.ikine(T, 'q0', [0, 0, 0, 0, 0], 'mask',[1, 1, 1, 1, 1, 0]);
    ang_robot(i, :) = qi;
    
end
    
 feature = pose_robot;%q;
 label = ang_robot;%pose_robot;
 
    
end