clear all;
close all;
% stimuli number
N = 21;
% gaussFilter
k = 5;  % this parameter is tunable
gaussFilter = gausswin(k*2*N,5); 

% stimuli # after filter
stim_N = linspace(1,N-1,N-1);   % there should be no stimuli on diagnal
for i = 1:length(stim_N)
    % precise gaussian filter
    % stim_N(1,i) = stim_N(1,i) * gaussFilter(max(1,(i-1)*k),1);
    stim_N(1,i) = stim_N(1,i) * gaussFilter(i*k,1);
end
% from diagnal to the topleft
stim_N_new = flip(stim_N);

% result matrix: 1 means there should be a stimuli, 0 means there shouldn't
% be a stimuli
res = zeros(N,N);
for i = 1:(N-1)
    tmpnum = round(stim_N_new(i));
    tmpres = randperm(N-i);
    
    % upper triangle
    for j = 1:tmpnum
        res(tmpres(j),tmpres(j)+i) = 1;
    end
    
    % lower triangle
    tmpres = randperm(N-i);
    for j = 1:tmpnum
        res(tmpres(j)+i,tmpres(j)) = 1;
    end
end
            
% create a matrix for indeix 1-30
[rId, cId] = find(triu( res ));

new_pairs = zeros(length(rId),2);
        
for i = 1:length(rId)
    new_pairs(i,1) = rId(i);
    new_pairs(i,2) = cId(i);
end
% permute the list
nTrials = length(rId)-1;
randomOrder=randperm(nTrials); 

for kk = 1:nTrials
    nItems_rand(kk,:) = new_pairs(randomOrder(kk),:);
end

% Create the conditionfiles. 
condition = 0;
for iBlock = 1:2  
    for n = 1:nTrials/2
        condition = condition +1;
        curCon = randomOrder(condition);
        conditionStruct(n).conditions = curCon-1;
        conditionStruct(n).block = iBlock;
        conditionStruct(n).sample1 = nItems_rand(condition,1)-1;
        conditionStruct(n).sample2 = nItems_rand(condition,2)-1;
        conditionStruct(n).height = randi(5)-1;
        conditionStruct(n).blur = randi(15)-1;
        conditionStruct(n).lighting = randi(2)-1;
    end
    newTestFileName = fullfile(['soap_conditions','_',num2str(iBlock), '.txt']);
    WriteStructsToText(newTestFileName, conditionStruct);
end









