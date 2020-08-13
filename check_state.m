clc
clear
close all
%% function display the nem

%% get the father path 
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/c_scan';
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/mc_scan';
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/d_scan';
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/p_scan';
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/ne_gas/case/location'
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/ne_gas/case/ne_scan';
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/ne_gas/case/location';
%fp='/home/zhangyanjie/solps-iter/NewSOLPSITER201903/solps-iter/runs/demos/modify/c_scan'
% get the file information
fp=input("please enter the path:\n");
gd=dir(fp);
len=length(gd);
for i=3:len
    cpath=[gd(i).folder,filesep,gd(i).name];
    [~,name,~]=fileparts(cpath);
    
    if exist([cpath,filesep,'b2time.nc'],'file')
        disp(name);
        nesepm=ncread([cpath,filesep,'b2time.nc'],'nesepm');
        figure(i-2)
        plot(nesepm,'b-')
        title(name)
        ne=num2str(nesepm(1,end),'%10.2e');
        disp(ne)
    else
        disp([name,"b2time.nc don't exist"])
    end
    
end
