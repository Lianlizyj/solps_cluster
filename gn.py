#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:12:23 1212

@author: Yanjie Zhang (Python 3.7)
@email: lianlizyj@mail.dlut.edu.cn
Description:

Purpose:
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,\
                               AutoMinorLocator)
    
# %% te in innner target 

#plt.figure()
tmp=np.loadtxt('te3dl.last10')
plt.subplot(4,2,1)
plt.plot(tmp[:,0],abs(tmp[:,1]),'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()

ax.set_title("Inner target profiles",size=24,color='r', weight='bold',family='Times New Roman',fontsize=15,fontweight=1.5)

# ax.set_xlabel("x [$\mu$m]",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
ax.set_ylabel('$T_{e} (eV)$',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8,visible=False)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
#
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% te at outer target
tmp=np.loadtxt('te3dr.last10')
plt.subplot(4,2,2)
plt.plot(tmp[:,0],abs(tmp[:,1]),'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()
ax.set_title("Outer target profiles",size=24, color='r',weight='bold',family='Times New Roman',fontsize=15,fontweight=1.5)

# ax.set_xlabel("x [$\mu$m]",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
# ax.set_ylabel('$T_{e}$ (eV)',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8,visible=False)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% ne in innner target 
tmp=np.loadtxt('ne3dl.last10')
plt.subplot(4,2,3)
plt.plot(tmp[:,0],abs(tmp[:,1])/1e19,'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()

# ax.set_title("$n_{e}$ at inner target",size=24, weight='bold',family='Times New Roman',fontsize=25,fontweight=1.5)

# ax.set_xlabel("x [$\mu$m]",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
ax.set_ylabel('$n_{e} (10^{19} m^{-3}$)',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8,visible=False)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% ne at outer target
tmp=np.loadtxt('ne3dr.last10')
plt.subplot(4,2,4)
plt.plot(tmp[:,0],abs(tmp[:,1])/1e19,'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()
# ax.set_title("$n_{e}$ at outer target",size=24, weight='bold',family='Times New Roman',fontsize=25,fontweight=1.5)

# ax.set_xlabel("x [$\mu$m]",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
# ax.set_ylabel('$T_{e}$ (eV)',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8,visible=False)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% \q in innner target 
tmp=np.loadtxt('ft3dl.last10')
plt.subplot(4,2,5)
plt.plot(tmp[:,0],abs(tmp[:,1])/1e6,'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()

# ax.set_title("$q_{dep}$ at inner target",size=24, weight='bold',family='Times New Roman',fontsize=25,fontweight=1.5)

# ax.set_xlabel("x [$\mu$m]",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
ax.set_ylabel('$q_{dep} (MW)$',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8,visible=False)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% q at outer target
tmp=np.loadtxt('ft3dr.last10')
plt.subplot(4,2,6)
plt.plot(tmp[:,0],abs(tmp[:,1])/1e6,'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()
# ax.set_title("$q_{dep}$ at outer target",size=24, weight='bold',family='Times New Roman',fontsize=25,fontweight=1.5)
# ax.set_xlabel("x [$\mu$m]",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
# ax.set_ylabel('$T_{e}$ (eV)',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8,visible=False)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% \Gamma in innner target 
tmp=np.loadtxt('fn3dl.last10')
plt.subplot(4,2,7)
plt.plot(tmp[:,0],abs(tmp[:,1])/1e23,'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()

# ax.set_title("$q_{dep}$ at inner target",size=24, weight='bold',family='Times New Roman',fontsize=25,fontweight=1.5)

ax.set_xlabel("$r-r_{sep} (m)$",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
ax.set_ylabel('$\Gamma (10^{23} s^{-1}$)',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% q at outer target
tmp=np.loadtxt('fn3dr.last10')
plt.subplot(4,2,8)
plt.plot(tmp[:,0],abs(tmp[:,1])/1e23,'b-')

# =============================================================================
# set_plot
# =============================================================================
ax=plt.gca()
# ax.set_title("$q_{dep}$ at outer target",size=24, weight='bold',family='Times New Roman',fontsize=25,fontweight=1.5)

ax.set_xlabel("$r-r_{sep} (m)$",family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)
# ax.set_ylabel('$T_{e}$ (eV)',family='Times New Roman', weight='bold',fontsize=12,fontweight=1.5)

plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'
ax.tick_params(which='both',width=1.5)
ax.tick_params(which='major', length=7,color='k')
ax.tick_params(which='minor', length=4,color='k')
plt.xticks(family='Times New Roman', weight='normal',fontsize=8)
plt.yticks(family='Times New Roman', weight='normal',fontsize=8)
# ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.xaxis.set_minor_locator(MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator()) 
ax.yaxis.set_minor_locator(AutoMinorLocator()) 

# =============================================================================
# set the linewidth of boxes
# =============================================================================
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.axis('tight')

# %% fullscreen
# mng = plt.get_current_fig_manager()
# mng.frame.Maximize(True)
# figManager = plt.get_current_fig_manager()
# figManager.window.showMaximized()
# mng = plt.get_current_fig_manager()
# mng.window.state('zoomed') #works fine on Windows!
# mng = plt.get_current_fig_manager()
# mng.frame.Maximize(True)
# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()

# Option 1
# QT backend
# manager = plt.get_current_fig_manager()
# manager.window.showMaximized()

# Option 2
# TkAgg backend
# manager = plt.get_current_fig_manager()
# manager.resize(*manager.window.maxsize())

# Option 3
# WX backend
# manager = plt.get_current_fig_manager()
# manager.frame.Maximize(True)
plt.savefig("downstream.pdf")
