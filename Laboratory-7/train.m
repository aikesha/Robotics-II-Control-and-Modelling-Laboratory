% the data set size can be also tuned
data_size = 20000;
[XTrain, YTrain] = create_dataset(data_size);
%q = [q1, q2, q3, q4, q5];
XXy = XTrain;
% nFeatures = 20; 
% nExamples = 10000;
% 
% 
% nOutputs = 1; % this example is for setting up a regression problem
% 
% x = rand(nExamples,nFeatures); 
% t = rand(nExamples, nOutputs);

%%
XTrain = reshape(XTrain', [1, 1, size(XTrain,2),size(XTrain,1)]);


nFeatures = 3;
numClasses = 5;

layers = [ ...
    imageInputLayer([1 1 nFeatures]);
    fullyConnectedLayer(128)
    leakyReluLayer
    fullyConnectedLayer(128)
    leakyReluLayer
    fullyConnectedLayer(64)
    leakyReluLayer
    fullyConnectedLayer(64)
    leakyReluLayer
    fullyConnectedLayer(numClasses)  
    regressionLayer  
    ]
maxEpochs = 15;
miniBatchSize = 200;

options = trainingOptions('adam', ...
    'ExecutionEnvironment','cpu', ...
    'GradientThreshold',1, ...
    'MaxEpochs',maxEpochs, ...
    'MiniBatchSize',miniBatchSize, ...
    'SequenceLength','longest', ...
    'Shuffle','never', ...
    'Verbose',0, ...
    'Plots','training-progress');


net = trainNetwork(XTrain, YTrain,layers,options);
save net