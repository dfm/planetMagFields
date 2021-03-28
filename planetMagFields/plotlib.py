#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs

def plotB(p2D,th2D,B,r=1,planet="earth"):

    planet = planet.lower()

    bmax = np.abs(B).max()
    digits = int(np.log10(bmax)) + 1

    if digits > 1:
        bmax = np.round(bmax)
    else:
        bmax = np.round(bmax,decimals=1)

    projection = ccrs.Mollweide()
    ax = plt.axes(projection=projection)

    if planet == "earth":
        ax.coastlines()

    lon2D = p2D - np.pi
    lat2D = np.pi/2 - th2D

    divnorm = colors.TwoSlopeNorm(vmin=-bmax, vcenter=0, vmax=bmax)

    cs = np.linspace(-bmax,bmax,100)

    cont = ax.contourf(lon2D*180/np.pi,lat2D*180/np.pi,B,cs,  \
           transform=ccrs.PlateCarree(),cmap='RdBu_r',norm=divnorm,extend='both')

    cbar = plt.colorbar(cont,orientation='horizontal',fraction=0.06, pad=0.04,ticks=[-bmax,0,bmax])
    cbar.ax.set_xlabel(r'Radial magnetic field ($\mu$T)',fontsize=25)
    cbar.ax.tick_params(labelsize=20)

    if r==1:
        radLabel = '  Surface'
    else:
        radLabel = r'  $r/r_{\rm surface}=%.2f$' %r

    ax.set_title(planet.capitalize() + radLabel,fontsize=25,pad=20)

def plotB_subplot(p2D,th2D,B,ax,planet="earth"):
    planet = planet.lower()

    bmax = np.abs(B).max()
    digits = int(np.log10(bmax)) + 1

    if digits > 1:
        bmax = np.round(bmax)
    else:
        bmax = np.round(bmax,decimals=1)

    if planet == "earth":
        ax.coastlines()

    p2D -= np.pi
    th2D -= np.pi/2
    th2D = -th2D

    cs = np.linspace(-bmax,bmax,100)
    divnorm = colors.TwoSlopeNorm(vmin=-bmax, vcenter=0, vmax=bmax)

    cont = ax.contourf(p2D*180/np.pi,th2D*180/np.pi,B,cs,  \
           transform=ccrs.PlateCarree(),cmap='RdBu_r',norm=divnorm,extend='both')

    cbar = plt.colorbar(cont,orientation='horizontal',fraction=0.06, pad=0.04,ticks=[-bmax,0,bmax])
    #cbar.ax.set_xlabel(r'Radial magnetic field ($\mu$T)',fontsize=15)
    cbar.ax.tick_params(labelsize=15)

    ax.set_title(planet.capitalize(),fontsize=20)