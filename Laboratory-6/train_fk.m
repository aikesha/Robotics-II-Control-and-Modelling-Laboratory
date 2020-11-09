clear
data_size = 5000; %???
[XTrain, YTrain] = create_dataset_fk(data_size);
% q = [q1, q2, q3, q4, q5];
% 
%  nFeatures = 20; 
%  nExamples = 10000;
%  
%  
%  nOutputs = 1; % this example is for setting up a regression problem
%  
%  x = rand(nExamples,nFeatures); 
%  t = rand(nExamples, nOutputs);

XTrain = reshape(XTrain', [1, 1, size(XTrain,2),size(XTrain,1)]);

nFeatures = 5;
numClasses = 3;

%You can learn about training NN by looking the following links
%https://www.mathworks.com/help/deeplearning/ref/trainingoptions.html
%https://www.mathworks.com/help/deeplearning/ref/trainnetwork.html
%https://www.mathworks.com/help/deeplearning/ug/list-of-deep-learning-layers.html

layers = [ ...
     imageInputLayer([1 1 nFeatures]);
    
    fullyConnectedLayer(512)
    fullyConnectedLayer(256)
    tanhLayer()
%  add more hidden layers to reduce the total mean error VARIABLE 'a' in the
%  script 'demo_fk.m'
%  you can change reluLayer to other activation functions
    fullyConnectedLayer(numClasses)  
    regressionLayer
    ]

maxEpochs = 10; %24
miniBatchSize = 100;

options = trainingOptions('adam', ...
    'ExecutionEnvironment','cpu', ...
    'GradientThreshold',1, ...
    'MaxEpochs',maxEpochs, ...
    'MiniBatchSize',miniBatchSize, ...
    'SequenceLength','longest', ...
    'Shuffle','never', ...
    'Verbose',0, ...
    'Plots','training-progress');

net_fk = trainNetwork(XTrain, YTrain,layers,options);

save net_fk