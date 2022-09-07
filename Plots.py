import os                          as os
import matplotlib.pyplot           as plt
import cartopy                     as cpy
import cartopy.crs                 as ccrs
import cartopy.feature             as cfeature
import numpy                       as np
from   cartopy.mpl.gridliner       import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.dates            as dates
import matplotlib.patches          as mpatches
from   numpy                       import polyfit
import numpy.polynomial.polynomial as poly
import proplot                     as pplt
from mpl_toolkits.axes_grid1       import make_axes_locatable, axes_size



years=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
contador = 0

#Stablish directory where we can find the data
os.chdir('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Arxius NPZ/2011-2020')

#Open dataset
ds = np.load('BalticSea2011-2020.npz')

lon       = ds['lon_allsat_DT21_BalticSea'  ]
lat       = ds['lat_allsat_DT21_BalticSea'  ] 
adt       = ds['adt_allsat_DT21_BalticSea'  ]
sla       = ds['sla_allsat_DT21_BalticSea'  ] 
ugos      = ds['ugos_allsat_DT21_BalticSea' ]
vgos      = ds['vgos_allsat_DT21_BalticSea' ]
ugosa     = ds['ugosa_allsat_DT21_BalticSea']
vgosa     = ds['vgosa_allsat_DT21_BalticSea'] 
time      = ds['time_allsat_DT21_BalticSea' ]

#Defining the grid
[mallax,mallay] = np.meshgrid(lon,lat)

#Defining region (GOTLAND BASIN. Green region)
lonrange1 = np.arange(14,22,0.01)                 
latrange1 = np.arange(54,60,0.01)
extent1=[14,22,54,60]
lonmin1 = 14
lonmax1 = 22
latmin1 = 54
latmax1 = 60
auxlon1=np.where((lon >= lonmin1) & (lon <= lonmax1)) [0] 
auxlat1=np.where((lat >= latmin1) & (lat <= latmax1)) [0]
lon1 = lon[auxlon1]
lat1 = lat[auxlat1]
[region1x,region1y]=np.meshgrid(auxlon1,auxlat1)
[malla1x,malla1y] = np.meshgrid(lon1,lat1)

# #Defining region (SEA OF BOTHNIA. Yellow region)
lonrange2 = np.arange(16,24,0.01)                 
latrange2 = np.arange(60,63,0.01)
extent2=[16,24,60,63]
lonmin2 = 16
lonmax2 = 24
latmin2 = 60
latmax2 = 63
auxlon2=np.where((lon >= lonmin2) & (lon <= lonmax2)) [0] 
auxlat2=np.where((lat >= latmin2) & (lat <= latmax2)) [0]
lon2 = lon[auxlon2]
lat2 = lat[auxlat2]
[region2x,region2y]=np.meshgrid(auxlon2,auxlat2)
[malla2x,malla2y] = np.meshgrid(lon2,lat2)

#Defining region (BAY OF BOTHNIA. Brown region)
lonrange3 = np.arange(16,27,0.01)                 
latrange3 = np.arange(63,67,0.01)
extent3=[16,27,63,67]
lonmin3 = 16
lonmax3 = 27
latmin3 = 63
latmax3 = 67
auxlon3=np.where((lon >= lonmin3) & (lon <= lonmax3)) [0] 
auxlat3=np.where((lat >= latmin3) & (lat <= latmax3)) [0]
lon3 = lon[auxlon3]
lat3 = lat[auxlat3]
[region3x,region3y]=np.meshgrid(auxlon3,auxlat3)
[malla3x,malla3y] = np.meshgrid(lon3,lat3)

#Defining region (Baltic SEA)
lonrange = np.arange(8,32,0.01)
latrange = np.arange(53,67,0.01)
extent = [8,32,53,67]

#Defining a nan region
lonmin = 8
lonmax = 14
latmin = 62
latmax = 67
auxlon=np.where((lon >= lonmin) & (lon <= lonmax)) [0] 
auxlat=np.where((lat >= latmin) & (lat <= latmax)) [0]
[reducidox,reducidoy]=np.meshgrid(auxlon,auxlat)

#########################################################################
##########################Emptying variables#############################
#########################################################################

totaltime              = np.empty(len(years)*time.shape[0])
realtime               = np.empty((time.shape[0],time.shape[1]), dtype=bool)
anualtime              = np.empty(len(years)) 
como                     = np.empty(len(years))


# adtmean                = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtspacemean           = np.empty((adt.shape[2],adt.shape[3]))
# adtspacemeananom       = np.empty((adt.shape[2],adt.shape[3]))
# adtyearsmean           = np.empty((adt.shape[0],adt.shape[1]))
# adtyearsmeananom       = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtspaceyearsmean      = np.empty((adt.shape[3]))
# adtspaceyearsmeananom  = np.empty((adt.shape[3]))
# totaladtspacemean      = np.empty(len(years)*(adt.shape[2]))
# totaladtspacemeananom  = np.empty(len(years)*(adt.shape[2])) 
# totaladtyearsmeananom  = np.empty(len(years)*(adt.shape[2]))
# slamean                = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# ugosmean               = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# vgosmean               = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KE                     = np.empty((adt.shape[0],adt.shape[1],adt.shape[2],adt.shape[3]))
# KEmean                 = np.empty((adt.shape[0],adt.shape[1],adt.shape[3])) 
# KEspacemean            = np.empty((adt.shape[2],adt.shape[3]))
# KEspacemeananom        = np.empty((adt.shape[2],adt.shape[3]))
# KEyearsmean            = np.empty((adt.shape[0],adt.shape[1]))
# KEyearsmeananom        = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# KEspaceyearsmeananom   = np.empty((adt.shape[3]))
# totalKEspacemeananom   = np.empty(len(years)*(adt.shape[2]))
# totalKEyearsmeananom   = np.empty(len(years)*(adt.shape[2]))
# ugosamean              = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# vgosamean              = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# EKE                    = np.empty((adt.shape[0],adt.shape[1],adt.shape[2],adt.shape[3]))
# EKEmean                = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtwinter              = np.empty((adt.shape[0],adt.shape[1],91,adt.shape[3]))
# adtspring              = np.empty((adt.shape[0],adt.shape[1],91,adt.shape[3]))
# adtsummer              = np.empty((adt.shape[0],adt.shape[1],92,adt.shape[3]))
# adtautumn              = np.empty((adt.shape[0],adt.shape[1],91,adt.shape[3]))   
# adtwintermean          = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtspringmean          = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtsummermean          = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtautumnmean          = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))   
# adtwinteryearsmean     = np.empty((adt.shape[0],adt.shape[1]))
# adtspringyearsmean     = np.empty((adt.shape[0],adt.shape[1]))
# adtsummeryearsmean     = np.empty((adt.shape[0],adt.shape[1]))
# adtautumnyearsmean     = np.empty((adt.shape[0],adt.shape[1]))
# adtwinteryearsmeananom = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtspringyearsmeananom = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtsummeryearsmeananom = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
# adtautumnyearsmeananom = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KEwinter               = np.empty((adt.shape[0],adt.shape[1],91,adt.shape[3])) 
KEspring               = np.empty((adt.shape[0],adt.shape[1],91,adt.shape[3]))
KEsummer               = np.empty((adt.shape[0],adt.shape[1],92,adt.shape[3]))
KEautumn               = np.empty((adt.shape[0],adt.shape[1],91,adt.shape[3])) 
KEwintermean           = np.empty((adt.shape[0],adt.shape[1],adt.shape[3])) 
KEspringmean           = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KEsummermean           = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KEautumnmean           = np.empty((adt.shape[0],adt.shape[1],adt.shape[3])) 
KEwinteryearsmean      = np.empty((adt.shape[0],adt.shape[1]))
KEspringyearsmean      = np.empty((adt.shape[0],adt.shape[1]))
KEsummeryearsmean      = np.empty((adt.shape[0],adt.shape[1]))
KEautumnyearsmean      = np.empty((adt.shape[0],adt.shape[1]))
KEwinteryearsmeananom  = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KEspringyearsmeananom  = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KEsummeryearsmeananom  = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))
KEautumnyearsmeananom  = np.empty((adt.shape[0],adt.shape[1],adt.shape[3]))



# adt1                   =np.empty((region1x.shape[0],region1y.shape[1],adt.shape[2],adt.shape[3]))
# sla1                   =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3]))
# ugos1                  =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3]))
# vgos1                  =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3]))
# ugosa1                 =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3]))
# vgosa1                 =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3]))
# KE1                    =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3]))
# EKE1                   =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[2],adt1.shape[3])) 
# adtmean1               =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# adtspacemean1          =np.empty((adt1.shape[2],adt1.shape[3]))
# adtspacemeananom1      =np.empty((adt1.shape[2],adt1.shape[3]))
# adtyearsmean1          =np.empty((adt1.shape[0],adt1.shape[1]))
# adtyearsmeananom1      =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtspaceyearsmeananom1 =np.empty((adt1.shape[3]))
# totaladtspacemean1     =np.empty(len(years)*(adt1.shape[2]))
# totaladtspacemeananom1 =np.empty(len(years)*(adt1.shape[2])) 
# totaladtyearsmeananom1 =np.empty(len(years)*(adt1.shape[2]))
# slamean1               =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# ugosmean1              =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# vgosmean1              =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# KEmean1                =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEspacemean1           =np.empty((adt1.shape[2],adt1.shape[3]))
# KEspacemeananom1       =np.empty((adt1.shape[2],adt1.shape[3]))
# KEyearsmean1           =np.empty((region1x.shape[0],region1y.shape[1])) 
# KEyearsmeananom1       =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# KEspaceyearsmeananom1  =np.empty((adt1.shape[3]))
# totalKEspacemeananom1  =np.empty(len(years)*(adt1.shape[2]))
# totalKEyearsmeananom1  =np.empty(len(years)*(adt1.shape[2]))
# ugosamean1             =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# vgosamean1             =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))
# EKEmean1               =np.empty((region1x.shape[0],region1y.shape[1],adt1.shape[3]))  
# adtwinter1             =np.empty((adt1.shape[0],adt1.shape[1],91,adt1.shape[3]))
# adtspring1             =np.empty((adt1.shape[0],adt1.shape[1],91,adt1.shape[3]))
# adtsummer1             =np.empty((adt1.shape[0],adt1.shape[1],92,adt1.shape[3]))
# adtautumn1             =np.empty((adt1.shape[0],adt1.shape[1],91,adt1.shape[3]))   
# adtwintermean1         =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtspringmean1         =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtsummermean1         =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtautumnmean1         =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))   
# adtwinteryearsmean1    =np.empty((adt1.shape[0],adt1.shape[1]))
# adtspringyearsmean1    =np.empty((adt1.shape[0],adt1.shape[1]))
# adtsummeryearsmean1    =np.empty((adt1.shape[0],adt1.shape[1]))
# adtautumnyearsmean1    =np.empty((adt1.shape[0],adt1.shape[1]))
# adtwinteryearsmeananom1=np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtspringyearsmeananom1=np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtsummeryearsmeananom1=np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# adtautumnyearsmeananom1=np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEwinter1              =np.empty((adt1.shape[0],adt1.shape[1],91,adt1.shape[3])) 
# KEspring1              =np.empty((adt1.shape[0],adt1.shape[1],91,adt1.shape[3]))
# KEsummer1              =np.empty((adt1.shape[0],adt1.shape[1],92,adt1.shape[3]))
# KEautumn1              =np.empty((adt1.shape[0],adt1.shape[1],91,adt1.shape[3]))
# KEwintermean1          =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3])) 
# KEspringmean1          =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEsummermean1          =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEautumnmean1          =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEwinteryearsmean1     =np.empty((adt1.shape[0],adt1.shape[1]))
# KEspringyearsmean1     =np.empty((adt1.shape[0],adt1.shape[1]))
# KEsummeryearsmean1     =np.empty((adt1.shape[0],adt1.shape[1]))
# KEautumnyearsmean1     =np.empty((adt1.shape[0],adt1.shape[1]))
# KEwinteryearsmeananom1 =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEspringyearsmeananom1 =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEsummeryearsmeananom1 =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3]))
# KEautumnyearsmeananom1 =np.empty((adt1.shape[0],adt1.shape[1],adt1.shape[3])) 

# adt2                   =np.empty((region2x.shape[0],region2y.shape[1],adt.shape[2],adt.shape[3]))
# sla2                   =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3]))
# ugos2                  =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3]))
# vgos2                  =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3]))
# ugosa2                 =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3]))
# vgosa2                 =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3]))
# KE2                    =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3]))
# EKE2                   =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[2],adt2.shape[3])) 
# adtmean2               =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# adtspacemean2          =np.empty((adt2.shape[2],adt2.shape[3]))
# adtspacemeananom2      =np.empty((adt2.shape[2],adt2.shape[3]))
# adtyearsmean2          =np.empty((adt2.shape[0],adt2.shape[1]))
# adtyearsmeananom2      =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtspaceyearsmeananom2 =np.empty((adt2.shape[3]))
# totaladtspacemean2     =np.empty(len(years)*(adt2.shape[2]))
# totaladtspacemeananom2 =np.empty(len(years)*(adt2.shape[2])) 
# totaladtyearsmeananom2 =np.empty(len(years)*(adt2.shape[2]))
# slamean2               =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# ugosmean2              =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# vgosmean2              =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# KEmean2                =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEspacemean2           =np.empty((adt2.shape[2],adt2.shape[3]))
# KEspacemeananom2       =np.empty((adt2.shape[2],adt2.shape[3]))
# KEyearsmean2           =np.empty((region2x.shape[0],region2y.shape[1])) 
# KEyearsmeananom2       =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# KEspaceyearsmeananom2  =np.empty((adt2.shape[3]))
# totalKEspacemeananom2  =np.empty(len(years)*(adt2.shape[2]))
# totalKEyearsmeananom2  =np.empty(len(years)*(adt2.shape[2]))
# ugosamean2             =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# vgosamean2             =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))
# EKEmean2               =np.empty((region2x.shape[0],region2y.shape[1],adt2.shape[3]))  
# adtwinter2             =np.empty((adt2.shape[0],adt2.shape[1],91,adt2.shape[3]))
# adtspring2             =np.empty((adt2.shape[0],adt2.shape[1],91,adt2.shape[3]))
# adtsummer2             =np.empty((adt2.shape[0],adt2.shape[1],92,adt2.shape[3]))
# adtautumn2             =np.empty((adt2.shape[0],adt2.shape[1],91,adt2.shape[3]))   
# adtwintermean2         =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtspringmean2         =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtsummermean2         =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtautumnmean2         =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))  
# adtwinteryearsmean2    =np.empty((adt2.shape[0],adt2.shape[1]))
# adtspringyearsmean2    =np.empty((adt2.shape[0],adt2.shape[1]))
# adtsummeryearsmean2    =np.empty((adt2.shape[0],adt2.shape[1]))
# adtautumnyearsmean2    =np.empty((adt2.shape[0],adt2.shape[1]))
# adtwinteryearsmeananom2=np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtspringyearsmeananom2=np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtsummeryearsmeananom2=np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# adtautumnyearsmeananom2=np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEwinter2              =np.empty((adt2.shape[0],adt2.shape[1],91,adt2.shape[3])) 
# KEspring2              =np.empty((adt2.shape[0],adt2.shape[1],91,adt2.shape[3]))
# KEsummer2              =np.empty((adt2.shape[0],adt2.shape[1],92,adt2.shape[3]))
# KEautumn2              =np.empty((adt2.shape[0],adt2.shape[1],91,adt2.shape[3])) 
# KEwintermean2          =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3])) 
# KEspringmean2          =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEsummermean2          =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEautumnmean2          =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3])) 
# KEwinteryearsmean2     =np.empty((adt2.shape[0],adt2.shape[1]))
# KEspringyearsmean2     =np.empty((adt2.shape[0],adt2.shape[1]))
# KEsummeryearsmean2     =np.empty((adt2.shape[0],adt2.shape[1]))
# KEautumnyearsmean2     =np.empty((adt2.shape[0],adt2.shape[1])) 
# KEwinteryearsmeananom2 =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEspringyearsmeananom2 =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEsummeryearsmeananom2 =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3]))
# KEautumnyearsmeananom2 =np.empty((adt2.shape[0],adt2.shape[1],adt2.shape[3])) 

# adt3                   =np.empty((region3x.shape[0],region3y.shape[1],adt.shape[2],adt.shape[3]))
# sla3                   =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3]))
# ugos3                  =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3]))
# vgos3                  =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3]))
# ugosa3                 =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3]))
# vgosa3                 =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3]))
# KE3                    =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3]))
# EKE3                   =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[2],adt3.shape[3])) 
# adtmean3               =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# adtspacemean3          =np.empty((adt3.shape[2],adt3.shape[3]))
# adtspacemeananom3      =np.empty((adt3.shape[2],adt3.shape[3]))
# adtyearsmean3          =np.empty((adt3.shape[0],adt3.shape[1]))
# adtyearsmeananom3      =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtspaceyearsmeananom3 =np.empty((adt3.shape[3]))
# totaladtspacemean3     =np.empty(len(years)*(adt3.shape[2]))
# totaladtspacemeananom3 =np.empty(len(years)*(adt3.shape[2])) 
# totaladtyearsmeananom3 =np.empty(len(years)*(adt3.shape[2]))
# slamean3               =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# ugosmean3              =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# vgosmean3              =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# KEmean3                =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# KEspacemean3           =np.empty((adt3.shape[2],adt3.shape[3]))
# KEspacemeananom3       =np.empty((adt3.shape[2],adt3.shape[3]))
# KEyearsmean3           =np.empty((region3x.shape[0],region3y.shape[1])) 
# KEyearsmeananom3       =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# KEspaceyearsmeananom3  =np.empty((adt3.shape[3]))
# totalKEspacemeananom3  =np.empty(len(years)*(adt3.shape[2]))
# totalKEyearsmeananom3  =np.empty(len(years)*(adt3.shape[2]))
# ugosamean3             =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# vgosamean3             =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))
# EKEmean3               =np.empty((region3x.shape[0],region3y.shape[1],adt3.shape[3]))  
# adtwinter3             =np.empty((adt3.shape[0],adt3.shape[1],91,adt3.shape[3]))
# adtspring3             =np.empty((adt3.shape[0],adt3.shape[1],91,adt3.shape[3]))
# adtsummer3             =np.empty((adt3.shape[0],adt3.shape[1],92,adt3.shape[3]))
# adtautumn3             =np.empty((adt3.shape[0],adt3.shape[1],91,adt3.shape[3]))   
# adtwintermean3         =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtspringmean3         =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtsummermean3         =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtautumnmean3         =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3])) 
# adtwinteryearsmean3    =np.empty((adt3.shape[0],adt3.shape[1]))
# adtspringyearsmean3    =np.empty((adt3.shape[0],adt3.shape[1]))
# adtsummeryearsmean3    =np.empty((adt3.shape[0],adt3.shape[1]))
# adtautumnyearsmean3    =np.empty((adt3.shape[0],adt3.shape[1])) 
# adtwinteryearsmeananom3=np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtspringyearsmeananom3=np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtsummeryearsmeananom3=np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# adtautumnyearsmeananom3=np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3])) 
# KEwinter3              =np.empty((adt3.shape[0],adt3.shape[1],91,adt3.shape[3])) 
# KEspring3              =np.empty((adt3.shape[0],adt3.shape[1],91,adt3.shape[3]))
# KEsummer3              =np.empty((adt3.shape[0],adt3.shape[1],92,adt3.shape[3]))
# KEautumn3              =np.empty((adt3.shape[0],adt3.shape[1],91,adt3.shape[3])) 
# KEwintermean3          =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3])) 
# KEspringmean3          =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# KEsummermean3          =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# KEautumnmean3          =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3])) 
# KEwinteryearsmean3     =np.empty((adt3.shape[0],adt3.shape[1]))
# KEspringyearsmean3     =np.empty((adt3.shape[0],adt3.shape[1]))
# KEsummeryearsmean3     =np.empty((adt3.shape[0],adt3.shape[1]))
# KEautumnyearsmean3     =np.empty((adt3.shape[0],adt3.shape[1])) 
# KEwinteryearsmeananom3 =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# KEspringyearsmeananom3 =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# KEsummeryearsmeananom3 =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3]))
# KEautumnyearsmeananom3 =np.empty((adt3.shape[0],adt3.shape[1],adt3.shape[3])) 

########################################################################
######################Filling Variables#################################
########################################################################

# adtmean                      [:,:,:]= 100*np.nanmean(adt[:,:,:,:],axis=2)
# adtspacemean                   [:,:]= 100*np.nanmean(adt[:,:,:,:] , axis=(0,1))
# adtyearsmean                   [:,:]= 100*np.nanmean(adt[:,:,:,:], axis=(2,3))
# slamean                      [:,:,:]= 100*np.nanmean(sla[:,:,:,:] , axis = 2)
# ugosmean                     [:,:,:]= 100*np.nanmean(ugos[:,:,:,:], axis = 2)
# vgosmean                     [:,:,:]= 100*np.nanmean(vgos[:,:,:,:], axis = 2)
KE                         [:,:,:,:]= 0.5*(ugos[:,:,:,:]**2 + vgos[:,:,:,:]**2) 
# KEmean                       [:,:,:]= 10000*np.nanmean(KE[:,:,:,:], axis=(2))
# KEspacemean                    [:,:]= 10000*np.nanmean(KE[:,:,:,:], axis=(0,1))
# KEyearsmean                    [:,:]= 10000*np.nanmean(KE[:,:,:,:], axis=(2,3))
# ugosamean                    [:,:,:]= 100*np.nanmean(ugosa[:,:,:,:], axis = 2)
# vgosamean                    [:,:,:]= 100*np.nanmean(vgosa[:,:,:,:], axis = 2)
# EKE                        [:,:,:,:]= 0.5*(ugosa[:,:,:,:]**2 + vgosa[:,:,:,:]**2)
# EKEmean                      [:,:,:]= np.nanmean(EKE[:,:,:,:], axis=2)
# adtwinter                  [:,:,:,:]= adt[:,:,0:91,:]
# adtspring                  [:,:,:,:]= adt[:,:,91:182,:]
# adtsummer                  [:,:,:,:]= adt[:,:,182:274,:]
# adtautumn                  [:,:,:,:]= adt[:,:,274:365,:]
# adtwintermean                [:,:,:]= 100*np.nanmean(adtwinter[:,:,:,:], axis=2)
# adtspringmean                [:,:,:]= 100*np.nanmean(adtspring[:,:,:,:], axis=2)
# adtsummermean                [:,:,:]= 100*np.nanmean(adtsummer[:,:,:,:], axis=2)
# adtautumnmean                [:,:,:]= 100*np.nanmean(adtautumn[:,:,:,:], axis=2)
# adtwinteryearsmean             [:,:]= 100*np.nanmean(adtwinter[:,:,:,:], axis=(2,3))
# adtspringyearsmean             [:,:]= 100*np.nanmean(adtspring[:,:,:,:], axis=(2,3))
# adtsummeryearsmean             [:,:]= 100*np.nanmean(adtsummer[:,:,:,:], axis=(2,3))
# adtautumnyearsmean             [:,:]= 100*np.nanmean(adtautumn[:,:,:,:], axis=(2,3))
KEwinter                   [:,:,:,:]= KE[:,:,0:91,:]
KEspring                   [:,:,:,:]= KE[:,:,91:182,:]
KEsummer                   [:,:,:,:]= KE[:,:,182:274,:]
KEautumn                   [:,:,:,:]= KE[:,:,274:365,:]
KEwintermean                 [:,:,:]= 10000*np.nanmean(KEwinter [:,:,:,:], axis=2)
KEspringmean                 [:,:,:]= 10000*np.nanmean(KEspring [:,:,:,:], axis=2)
KEsummermean                 [:,:,:]= 10000*np.nanmean(KEsummer [:,:,:,:], axis=2)
KEautumnmean                 [:,:,:]= 10000*np.nanmean(KEautumn [:,:,:,:], axis=2)
KEwinteryearsmean              [:,:]= 10000*np.nanmean(KEwinter[:,:,:,:], axis=(2,3))
KEspringyearsmean              [:,:]= 10000*np.nanmean(KEspring[:,:,:,:], axis=(2,3))
KEsummeryearsmean              [:,:]= 10000*np.nanmean(KEsummer[:,:,:,:], axis=(2,3))
KEautumnyearsmean              [:,:]= 10000*np.nanmean(KEautumn[:,:,:,:], axis=(2,3))


        
# adt1                     [:,:,:,:]= adt[region1y,region1x,:,:]
#sla1                     [:,:,:,:]= sla[region1y,region1x,:,:]
# ugos1                    [:,:,:,:]= ugos[region1y,region1x,:,:]
# vgos1                    [:,:,:,:]= vgos[region1y,region1x,:,:]
# KE1                      [:,:,:,:]= 0.5*(ugos1[:,:,:,:]**2 + vgos1[:,:,:,:]**2)
#ugosa1                    [:,:,:,:]= ugosa[region1y,region1x,:,:]
#vgosa1                    [:,:,:,:]= vgosa[region1y,region1x,:,:]
# EKE1                     [:,:,:,:]= 0.5*(ugosa1[:,:,:,:]**2 + vgosa1[:,:,:,:]**2)
# adtmean1                   [:,:,:]= 100*np.nanmean(adt1[:,:,:,:] , axis = 2)
# adtspacemean1                [:,:]= 100*np.nanmean(adt1[:,:,:,:] , axis=(0,1))
# adtyearsmean1                [:,:]= 100*np.nanmean(adt1[:,:,:,:], axis=(2,3))
# slamean1                   [:,:,:]= 100*np.nanmean(sla1[:,:,:,:] , axis = 2)
# ugosmean1                  [:,:,:]= 100*np.nanmean(ugos1[:,:,:,:], axis = 2)
# vgosmean1                  [:,:,:]= 100*np.nanmean(vgos1[:,:,:,:], axis = 2)
# KEmean1                    [:,:,:]= 10000*np.nanmean(KE1[:,:,:,:], axis=(2))
# KEspacemean1                 [:,:]= 10000*np.nanmean(KE1[:,:,:,:], axis=(0,1))
# KEyearsmean1                 [:,:]= 10000*np.nanmean(KE1[:,:,:,:], axis=(2,3))
# ugosamean1                 [:,:,:]= 100*np.nanmean(ugosa1[:,:,:,:], axis = 2)
# vgosamean1                 [:,:,:]= 100*np.nanmean(vgosa1[:,:,:,:], axis = 2)
# EKEmean1                   [:,:,:]= 10000*np.nanmean(EKE1[:,:,:,:], axis=2)
# adtwinter1               [:,:,:,:]= adt1[:,:,0:91,:]
# adtspring1               [:,:,:,:]= adt1[:,:,91:182,:]
# adtsummer1               [:,:,:,:]= adt1[:,:,182:274,:]
# adtautumn1               [:,:,:,:]= adt1[:,:,274:365,:]
# adtwintermean1             [:,:,:]= 100*np.nanmean(adtwinter1[:,:,:,:], axis=2)
# adtspringmean1             [:,:,:]= 100*np.nanmean(adtspring1[:,:,:,:], axis=2)
# adtsummermean1             [:,:,:]= 100*np.nanmean(adtsummer1[:,:,:,:], axis=2)
# adtautumnmean1             [:,:,:]= 100*np.nanmean(adtautumn1[:,:,:,:], axis=2)
# adtwinteryearsmean1          [:,:]= 100*np.nanmean(adtwinter1[:,:,:,:], axis=(2,3))
# adtspringyearsmean1          [:,:]= 100*np.nanmean(adtspring1[:,:,:,:], axis=(2,3))
# adtsummeryearsmean1          [:,:]= 100*np.nanmean(adtsummer1[:,:,:,:], axis=(2,3))
# adtautumnyearsmean1          [:,:]= 100*np.nanmean(adtautumn1[:,:,:,:], axis=(2,3))
# KEwinter1                [:,:,:,:]= KE1[:,:,0:91,:]
# KEspring1                [:,:,:,:]= KE1[:,:,91:182,:]
# KEsummer1                [:,:,:,:]= KE1[:,:,182:274,:]
# KEautumn1                [:,:,:,:]= KE1[:,:,274:365,:]
# KEwintermean1              [:,:,:]= 10000*np.nanmean(KEwinter1 [:,:,:,:], axis=2)
# KEspringmean1              [:,:,:]= 10000*np.nanmean(KEspring1 [:,:,:,:], axis=2)
# KEsummermean1              [:,:,:]= 10000*np.nanmean(KEsummer1 [:,:,:,:], axis=2)
# KEautumnmean1              [:,:,:]= 10000*np.nanmean(KEautumn1 [:,:,:,:], axis=2)
# KEwinteryearsmean1           [:,:]= 10000*np.nanmean(KEwinter1[:,:,:,:], axis=(2,3))
# KEspringyearsmean1           [:,:]= 10000*np.nanmean(KEspring1[:,:,:,:], axis=(2,3))
# KEsummeryearsmean1           [:,:]= 10000*np.nanmean(KEsummer1[:,:,:,:], axis=(2,3))
# KEautumnyearsmean1           [:,:]= 10000*np.nanmean(KEautumn1[:,:,:,:], axis=(2,3))

# adt2                     [:,:,:,:]= adt[region2y,region2x,:,:]
#sla2                     [:,:,:,:]= sla[region2y,region2x,:,:]
# ugos2                    [:,:,:,:]= ugos[region2y,region2x,:,:]
# vgos2                    [:,:,:,:]= vgos[region2y,region2x,:,:]
# KE2                      [:,:,:,:]= 0.5*(ugos2[:,:,:,:]**2 + vgos2[:,:,:,:]**2)
#ugosa2                    [:,:,:,:]= ugosa[region2y,region2x,:,:]
#vgosa2                    [:,:,:,:]= vgosa[region2y,region2x,:,:]
# EKE2                     [:,:,:,:]= 0.5*(ugosa2[:,:,:,:]**2 + vgosa2[:,:,:,:]**2)
# adtmean2                   [:,:,:]= 100*np.nanmean(adt2[:,:,:,:] , axis = 2)
# adtspacemean2                [:,:]= 100*np.nanmean(adt2[:,:,:,:] , axis=(0,1))
# adtyearsmean2                [:,:]= 100*np.nanmean(adt2[:,:,:,:], axis=(2,3))
# slamean2                   [:,:,:]= 100*np.nanmean(sla2[:,:,:,:] , axis = 2)
# ugosmean2                  [:,:,:]= 100*np.nanmean(ugos2[:,:,:,:], axis = 2)
# vgosmean2                  [:,:,:]= 100*np.nanmean(vgos2[:,:,:,:], axis = 2)
# KEmean2                    [:,:,:]= 10000*np.nanmean(KE2[:,:,:,:], axis=(2))
# KEspacemean2                 [:,:]= 10000*np.nanmean(KE2[:,:,:,:], axis=(0,1))
# KEyearsmean2                 [:,:]= 10000*np.nanmean(KE2[:,:,:,:], axis=(2,3))
# ugosamean2                 [:,:,:]= 100*np.nanmean(ugosa2[:,:,:,:], axis = 2)
# vgosamean2                 [:,:,:]= 100*np.nanmean(vgosa2[:,:,:,:], axis = 2)
# EKEmean2                   [:,:,:]= 10000*np.nanmean(EKE2[:,:,:,:], axis=2)
# adtwinter2               [:,:,:,:]= adt2[:,:,0:91,:]
# adtspring2               [:,:,:,:]= adt2[:,:,91:182,:]
# adtsummer2               [:,:,:,:]= adt2[:,:,182:274,:]
# adtautumn2               [:,:,:,:]= adt2[:,:,274:365,:]
# adtwintermean2             [:,:,:]= 100*np.nanmean(adtwinter2[:,:,:,:], axis=2)
# adtspringmean2             [:,:,:]= 100*np.nanmean(adtspring2[:,:,:,:], axis=2)
# adtsummermean2             [:,:,:]= 100*np.nanmean(adtsummer2[:,:,:,:], axis=2)
# adtautumnmean2             [:,:,:]= 100*np.nanmean(adtautumn2[:,:,:,:], axis=2)
# adtwinteryearsmean2          [:,:]= 100*np.nanmean(adtwinter2[:,:,:,:], axis=(2,3))
# adtspringyearsmean2          [:,:]= 100*np.nanmean(adtspring2[:,:,:,:], axis=(2,3))
# adtsummeryearsmean2          [:,:]= 100*np.nanmean(adtsummer2[:,:,:,:], axis=(2,3))
# adtautumnyearsmean2          [:,:]= 100*np.nanmean(adtautumn2[:,:,:,:], axis=(2,3))
# KEwinter2                [:,:,:,:]= KE2[:,:,0:91,:]
# KEspring2                [:,:,:,:]= KE2[:,:,91:182,:]
# KEsummer2                [:,:,:,:]= KE2[:,:,182:274,:]
# KEautumn2                [:,:,:,:]= KE2[:,:,274:365,:]
# KEwintermean2                [:,:,:]= 10000*np.mean(KEwinter2 [:,:,:,:], axis=2)
# KEspringmean2                [:,:,:]= 10000*np.mean(KEspring2 [:,:,:,:], axis=2)
# KEsummermean2                [:,:,:]= 10000*np.mean(KEsummer2 [:,:,:,:], axis=2)
# KEautumnmean2                [:,:,:]= 10000*np.mean(KEautumn2 [:,:,:,:], axis=2)
# KEwinteryearsmean2             [:,:]= 10000*np.mean(KEwinter2[:,:,:,:], axis=(2,3))
# KEspringyearsmean2             [:,:]= 10000*np.mean(KEspring2[:,:,:,:], axis=(2,3))
# KEsummeryearsmean2             [:,:]= 10000*np.mean(KEsummer2[:,:,:,:], axis=(2,3))
# KEautumnyearsmean2             [:,:]= 10000*np.mean(KEautumn2[:,:,:,:], axis=(2,3))

# adt3                       [:,:,:,:]= adt[region3y,region3x,:,:]
# sla3                       [:,:,:,:]= sla[region3y,region3x,:,:]
# ugos3                      [:,:,:,:]= ugos[region3y,region3x,:,:]
# vgos3                      [:,:,:,:]= vgos[region3y,region3x,:,:]
# KE3                        [:,:,:,:]= 0.5*(ugos3[:,:,:,:]**2 + vgos3[:,:,:,:]**2)
# ugosa3                     [:,:,:,:]= ugosa[region3y,region3x,:,:]
# vgosa3                     [:,:,:,:]= vgosa[region3y,region3x,:,:]
# EKE3                       [:,:,:,:]= 0.5*(ugosa3[:,:,:,:]**2 + vgosa3[:,:,:,:]**2)
# adtmean3                     [:,:,:]= 100*np.nanmean(adt3[:,:,:,:] , axis = 2)
# adtspacemean3                  [:,:]= 100*np.nanmean(adt3[:,:,:,:] , axis=(0,1))
# adtyearsmean3                  [:,:]= 100*np.nanmean(adt3[:,:,:,:], axis=(2,3))
# slamean3                     [:,:,:]= 100*np.nanmean(sla3[:,:,:,:] , axis = 2)
# ugosmean3                    [:,:,:]= 100*np.nanmean(ugos3[:,:,:,:], axis = 2)
# vgosmean3                    [:,:,:]= 100*np.nanmean(vgos3[:,:,:,:], axis = 2)
# KEmean3                      [:,:,:]= 10000*np.nanmean(KE3[:,:,:,:], axis=(2))
# KEspacemean3                   [:,:]= 10000*np.nanmean(KE3[:,:,:,:], axis=(0,1))
# KEyearsmean3                   [:,:]= 10000*np.nanmean(KE3[:,:,:,:], axis=(2,3))
# ugosamean3                   [:,:,:]= 100*np.nanmean(ugosa3[:,:,:,:], axis = 2)
# vgosamean3                   [:,:,:]= 100*np.nanmean(vgosa3[:,:,:,:], axis = 2)
# EKEmean3                     [:,:,:]= 10000*np.nanmean(EKE3[:,:,:,:], axis=2)
# adtwinter3                 [:,:,:,:]= adt3[:,:,0:91,:]
# adtspring3                 [:,:,:,:]= adt3[:,:,91:182,:]
# adtsummer3                 [:,:,:,:]= adt3[:,:,182:274,:]
# adtautumn3                 [:,:,:,:]= adt3[:,:,274:365,:]
# adtwintermean3               [:,:,:]= 100*np.mean(adtwinter3[:,:,:,:], axis=2)
# adtspringmean3               [:,:,:]= 100*np.mean(adtspring3[:,:,:,:], axis=2)
# adtsummermean3               [:,:,:]= 100*np.mean(adtsummer3[:,:,:,:], axis=2)
# adtautumnmean3               [:,:,:]= 100*np.mean(adtautumn3[:,:,:,:], axis=2)
# adtwinteryearsmean3            [:,:]= 100*np.mean(adtwinter3[:,:,:,:], axis=(2,3))
# adtspringyearsmean3            [:,:]= 100*np.mean(adtspring3[:,:,:,:], axis=(2,3))
# adtsummeryearsmean3            [:,:]= 100*np.mean(adtsummer3[:,:,:,:], axis=(2,3))
# adtautumnyearsmean3            [:,:]= 100*np.mean(adtautumn3[:,:,:,:], axis=(2,3))
# KEwinter3                  [:,:,:,:]= KE3[:,:,0:91,:]
# KEspring3                  [:,:,:,:]= KE3[:,:,91:182,:]
# KEsummer3                  [:,:,:,:]= KE3[:,:,182:274,:]
# KEautumn3                  [:,:,:,:]= KE3[:,:,274:365,:]
# KEwintermean3                [:,:,:]= 10000*np.mean(KEwinter3 [:,:,:,:], axis=2)
# KEspringmean3                [:,:,:]= 10000*np.mean(KEspring3 [:,:,:,:], axis=2)
# KEsummermean3                [:,:,:]= 10000*np.mean(KEsummer3 [:,:,:,:], axis=2)
# KEautumnmean3                [:,:,:]= 10000*np.mean(KEautumn3 [:,:,:,:], axis=2)
# KEwinteryearsmean3             [:,:]= 10000*np.mean(KEwinter3[:,:,:,:], axis=(2,3))
# KEspringyearsmean3             [:,:]= 10000*np.mean(KEspring3[:,:,:,:], axis=(2,3))
# KEsummeryearsmean3             [:,:]= 10000*np.mean(KEsummer3[:,:,:,:], axis=(2,3))
# KEautumnyearsmean3             [:,:]= 10000*np.mean(KEautumn3[:,:,:,:], axis=(2,3))

# realtime            [:,:]= np.invert(np.isnan(time[:,:]))

#########################################################################
##############################nan Region#################################
#########################################################################

# adtyearsmean      [reducidoy,reducidox]=np.nan
# adt           [reducidoy,reducidox,:,:]=np.nan 
# adtmean           [reducidoy,reducidox]=np.nan
# adtwintermean   [reducidoy,reducidox,:]=np.nan
# adtspringmean   [reducidoy,reducidox,:]=np.nan
# adtsummermean   [reducidoy,reducidox,:]=np.nan
# adtautumnmean   [reducidoy,reducidox,:]=np.nan
# adtwinteryearsmean[reducidoy,reducidox]=np.nan
# adtspringyearsmean[reducidoy,reducidox]=np.nan
# adtsummeryearsmean[reducidoy,reducidox]=np.nan
# adtautumnyearsmean[reducidoy,reducidox]=np.nan
KEwintermean    [reducidoy,reducidox,:]=np.nan
KEspringmean    [reducidoy,reducidox,:]=np.nan
KEsummermean    [reducidoy,reducidox,:]=np.nan
KEautumnmean    [reducidoy,reducidox,:]=np.nan
KEwinteryearsmean [reducidoy,reducidox]=np.nan
KEspringyearsmean [reducidoy,reducidox]=np.nan
KEsummeryearsmean [reducidoy,reducidox]=np.nan
KEautumnyearsmean [reducidoy,reducidox]=np.nan
# ugosmean          [reducidoy,reducidox]=np.nan
# vgosmean          [reducidoy,reducidox]=np.nan
# KEmean            [reducidoy,reducidox]=np.nan
# KEyearsmean       [reducidoy,reducidox]=np.nan
# ugosamean         [reducidoy,reducidox]=np.nan
# vgosamean         [reducidoy,reducidox]=np.nan
# EKEmean           [reducidoy,reducidox]=np.nan


for i,año in enumerate(years):
#Defining Variables
    # realtime                [:,i]= np.invert(np.isnan(time[:,i]))
    # adtyearsmeananom      [:,:,i]= adtmean[:,:,i]-adtyearsmean[:,:]
    # KEyearsmeananom       [:,:,i]= KEmean [:,:,i]-KEyearsmean [:,:]
    # adtwinteryearsmeananom[:,:,i]=adtwintermean[:,:,i]-adtwinteryearsmean[:,:]
    # adtspringyearsmeananom[:,:,i]=adtspringmean[:,:,i]-adtspringyearsmean[:,:]
    # adtsummeryearsmeananom[:,:,i]=adtsummermean[:,:,i]-adtsummeryearsmean[:,:]
    # adtautumnyearsmeananom[:,:,i]=adtautumnmean[:,:,i]-adtautumnyearsmean[:,:]
    KEwinteryearsmeananom [:,:,i]=KEwintermean[:,:,i]-KEwinteryearsmean[:,:]
    KEspringyearsmeananom [:,:,i]=KEspringmean[:,:,i]-KEspringyearsmean[:,:]
    KEsummeryearsmeananom [:,:,i]=KEsummermean[:,:,i]-KEsummeryearsmean[:,:]
    KEautumnyearsmeananom [:,:,i]=KEautumnmean[:,:,i]-KEautumnyearsmean[:,:]
    
    # adtyearsmeananom1      [:,:,i]=adtmean1[:,:,i]-adtyearsmean1[:,:]
    # KEyearsmeananom1       [:,:,i]=KEmean1 [:,:,i]-KEyearsmean1 [:,:]
    # adtwinteryearsmeananom1[:,:,i]=adtwintermean1[:,:,i]-adtwinteryearsmean1[:,:]
    # adtspringyearsmeananom1[:,:,i]=adtspringmean1[:,:,i]-adtspringyearsmean1[:,:]
    # adtsummeryearsmeananom1[:,:,i]=adtsummermean1[:,:,i]-adtsummeryearsmean1[:,:]
    # adtautumnyearsmeananom1[:,:,i]=adtautumnmean1[:,:,i]-adtautumnyearsmean1[:,:]
    # KEwinteryearsmeananom1 [:,:,i]=KEwintermean1[:,:,i]-KEwinteryearsmean1[:,:]
    # KEspringyearsmeananom1 [:,:,i]=KEspringmean1[:,:,i]-KEspringyearsmean1[:,:]
    # KEsummeryearsmeananom1 [:,:,i]=KEsummermean1[:,:,i]-KEsummeryearsmean1[:,:]
    # KEautumnyearsmeananom1 [:,:,i]=KEautumnmean1[:,:,i]-KEautumnyearsmean1[:,:]
    
    # adtyearsmeananom2       [:,:,i]=adtmean2[:,:,i]-adtyearsmean2[:,:]
    # KEyearsmeananom2        [:,:,i]=KEmean2 [:,:,i]-KEyearsmean2 [:,:]
    # adtwinteryearsmeananom2[:,:,i]=adtwintermean2[:,:,i]-adtwinteryearsmean2[:,:]
    # adtspringyearsmeananom2[:,:,i]=adtspringmean2[:,:,i]-adtspringyearsmean2[:,:]
    # adtsummeryearsmeananom2[:,:,i]=adtsummermean2[:,:,i]-adtsummeryearsmean2[:,:]
    # adtautumnyearsmeananom2[:,:,i]=adtautumnmean2[:,:,i]-adtautumnyearsmean2[:,:]
    # KEwinteryearsmeananom2 [:,:,i]=KEwintermean2[:,:,i]-KEwinteryearsmean2[:,:]
    # KEspringyearsmeananom2 [:,:,i]=KEspringmean2[:,:,i]-KEspringyearsmean2[:,:]
    # KEsummeryearsmeananom2 [:,:,i]=KEsummermean2[:,:,i]-KEsummeryearsmean2[:,:]
    # KEautumnyearsmeananom2 [:,:,i]=KEautumnmean2[:,:,i]-KEautumnyearsmean2[:,:]
    
    # adtyearsmeananom3      [:,:,i]=adtmean3[:,:,i]-adtyearsmean3[:,:]
    # KEyearsmeananom3       [:,:,i]=KEmean3 [:,:,i]-KEyearsmean3 [:,:]
    # adtwinteryearsmeananom3[:,:,i]=adtwintermean3[:,:,i]-adtwinteryearsmean3[:,:]
    # adtspringyearsmeananom3[:,:,i]=adtspringmean3[:,:,i]-adtspringyearsmean3[:,:]
    # adtsummeryearsmeananom3[:,:,i]=adtsummermean3[:,:,i]-adtsummeryearsmean3[:,:]
    # adtautumnyearsmeananom3[:,:,i]=adtautumnmean3[:,:,i]-adtautumnyearsmean3[:,:]
    # KEwinteryearsmeananom3 [:,:,i]=KEwintermean3[:,:,i]-KEwinteryearsmean3[:,:]
    # KEspringyearsmeananom3 [:,:,i]=KEspringmean3[:,:,i]-KEspringyearsmean3[:,:]
    # KEsummeryearsmeananom3 [:,:,i]=KEsummermean3[:,:,i]-KEsummeryearsmean3[:,:]
    # KEautumnyearsmeananom3 [:,:,i]=KEautumnmean3[:,:,i]-KEautumnyearsmean3[:,:]
    
    
    #adtyearsmeananom      [reducidoy,reducidox,:]=np.nan
    #KEyearsmeananom       [reducidoy,reducidox,:]=np.nan
    #adtwinteryearsmeananom[reducidoy,reducidox,:]=np.nan
    #adtspringyearsmeananom[reducidoy,reducidox,:]=np.nan
    #adtsummeryearsmeananom[reducidoy,reducidox,:]=np.nan
    #adtautumnyearsmeananom[reducidoy,reducidox,:]=np.nan
    #KEwinteryearsmeananom [reducidoy,reducidox,:]=np.nan
    #KEspringyearsmeananom [reducidoy,reducidox,:]=np.nan
    #KEsummeryearsmeananom [reducidoy,reducidox,:]=np.nan
    #KEautumnyearsmeananom [reducidoy,reducidox,:]=np.nan
    
    
    # adtspaceyearsmeananom[i]= np.nanmean(adtyearsmeananom[:,:,i], axis=(0,1))         
    # KEspaceyearsmeananom [i]= np.nanmean(KEyearsmeananom [:,:,i], axis=(0,1)) 
    
    # adtspaceyearsmeananom1[i]= np.nanmean(adtyearsmeananom1[:,:,i], axis=(0,1))
#     KEspaceyearsmeananom1 [i]= np.nanmean(KEyearsmeananom1 [:,:,i], axis=(0,1)) 

    # adtspaceyearsmeananom2[i]= np.nanmean(adtyearsmeananom2[:,:,i], axis=(0,1))
#     KEspaceyearsmeananom2 [i]= np.nanmean(KEyearsmeananom2 [:,:,i], axis=(0,1)) 

    # adtspaceyearsmeananom3[i]= np.nanmean(adtyearsmeananom3[:,:,i], axis=(0,1))
#     KEspaceyearsmeananom3 [i]= np.nanmean(KEyearsmeananom3 [:,:,i], axis=(0,1)) 

    
    # for j in range(366): 
    #     totaltime[contador] = time[j,i]
    #     anualtime       [i] = time[0,i]
        
        # totaladtspacemeananom[contador]= np.nanmean(100*adt[:,:,j,i]-adtyearsmean[:,:], axis=(0,1))
        # totalKEspacemeananom [contador]= np.nanmean(10000*KE[:,:,j,i]-KEyearsmean[:,:], axis=(0,1))

        # totaladtspacemeananom1[contador]= np.nanmean(100*adt1[:,:,j,i]-adtyearsmean1[:,:], axis=(0,1))
#         totalKEspacemeananom1 [contador]= np.nanmean(10000*KE1[:,:,j,i]-KEyearsmean1[:,:], axis=(0,1))


        # totaladtspacemeananom2[contador]= np.nanmean(100*adt2[:,:,j,i]-adtyearsmean2[:,:], axis=(0,1))
#         totalKEspacemeananom2 [contador]= np.nanmean(10000*KE2[:,:,j,i]-KEyearsmean2[:,:], axis=(0,1))


        # totaladtspacemeananom3[contador]= np.nanmean(100*adt3[:,:,j,i]-adtyearsmean3[:,:], axis=(0,1))
#         totalKEspacemeananom3 [contador]= np.nanmean(10000*KE3[:,:,j,i]-KEyearsmean3[:,:], axis=(0,1))
        
        # contador=contador + 1
   
# b = np.where(totalKEspacemeananom>70)[0]
# totalKEspacemeananom[b]=np.nan    
# realtotaltime=np.invert(np.isnan(totaltime))
# realanualtime= dates.num2date(anualtime)

# coeff_adt  = poly.polyfit(anualtime,adtspaceyearsmeananom,1)
# ffit_adt   = poly.polyval(anualtime,coeff_adt)
# coeff_KE  = poly.polyfit(anualtime,KEspaceyearsmeananom,1)
# ffit_KE   = poly.polyval(anualtime,coeff_KE)

# coeff_adt1  = poly.polyfit(anualtime,adtspaceyearsmeananom1,1)
# ffit_adt1   = poly.polyval(anualtime,coeff_adt1)
# coeff_KE1  = poly.polyfit(anualtime,KEspaceyearsmeananom1,1)
# ffit_KE1   = poly.polyval(anualtime,coeff_KE1)

# coeff_adt2  = poly.polyfit(anualtime,adtspaceyearsmeananom2,1)
# ffit_adt2   = poly.polyval(anualtime,coeff_adt2)
# coeff_KE2  = poly.polyfit(anualtime,KEspaceyearsmeananom2,1)
# ffit_KE2   = poly.polyval(anualtime,coeff_KE2)

# coeff_adt3  = poly.polyfit(anualtime,adtspaceyearsmeananom3,1)
# ffit_adt3   = poly.polyval(anualtime,coeff_adt3)
# coeff_KE3  = poly.polyfit(anualtime,KEspaceyearsmeananom3,1)
# ffit_KE3   = poly.polyval(anualtime,coeff_KE3)

# nonanscoeff_adt = np.where(np.invert(np.isnan(totaladtspacemeananom)))[0]
# coeff_adt  = poly.polyfit(totaltime[nonanscoeff_adt],totaladtspacemeananom[nonanscoeff_adt],1)
# ffit_adt   = poly.polyval(totaltime[nonanscoeff_adt],coeff_adt)

# nonanscoeff_KE = np.where(np.invert(np.isnan(totalKEspacemeananom)))[0]
# coeff_KE  = poly.polyfit(totaltime[nonanscoeff_KE],totalKEspacemeananom[nonanscoeff_KE],1)
# ffit_KE   = poly.polyval(totaltime[nonanscoeff_KE],coeff_KE)

# nonanscoeff_adt1 = np.where(np.invert(np.isnan(totaladtspacemeananom1)))[0]
# coeff_adt1  = poly.polyfit(totaltime[nonanscoeff_adt1],totaladtspacemeananom1[nonanscoeff_adt1],1)
# ffit_adt1   = poly.polyval(totaltime[nonanscoeff_adt1],coeff_adt1)

# nonanscoeff_KE1 = np.where(np.invert(np.isnan(totalKEspacemeananom1)))[0]
# coeff_KE1  = poly.polyfit(totaltime[nonanscoeff_KE1],totalKEspacemeananom1[nonanscoeff_KE1],1)
# ffit_KE1   = poly.polyval(totaltime[nonanscoeff_KE1],coeff_KE1)

# nonanscoeff_adt2 = np.where(np.invert(np.isnan(totaladtspacemeananom2)))[0]
# coeff_adt2  = poly.polyfit(totaltime[nonanscoeff_adt2],totaladtspacemeananom2[nonanscoeff_adt2],1)
# ffit_adt2   = poly.polyval(totaltime[nonanscoeff_adt2],coeff_adt2)

# nonanscoeff_KE2 = np.where(np.invert(np.isnan(totalKEspacemeananom2)))[0]
# coeff_KE2  = poly.polyfit(totaltime[nonanscoeff_KE2],totalKEspacemeananom2[nonanscoeff_KE2],1)
# ffit_KE2   = poly.polyval(totaltime[nonanscoeff_KE2],coeff_KE2)

# nonanscoeff_adt3 = np.where(np.invert(np.isnan(totaladtspacemeananom3)))[0]
# coeff_adt3  = poly.polyfit(totaltime[nonanscoeff_adt3],totaladtspacemeananom3[nonanscoeff_adt3],1)
# ffit_adt3   = poly.polyval(totaltime[nonanscoeff_adt3],coeff_adt3)

# nonanscoeff_KE3 = np.where(np.invert(np.isnan(totalKEspacemeananom3)))[0]
# coeff_KE3  = poly.polyfit(totaltime[nonanscoeff_KE3],totalKEspacemeananom[nonanscoeff_KE3],1)
# ffit_KE3   = poly.polyval(totaltime[nonanscoeff_KE3],coeff_KE3)

 
############################################################################### 
#            Map plots                                                        #
############################################################################### 
# for i, año in enumerate(years):
#     ax = plt.axes(projection=ccrs.PlateCarree())
#     plt.title('KE anomalies ('+str(año)+') [cm^2/s^2]', loc='center', fontsize = 18, y=1)
#     plt.pcolormesh(mallax,mallay, KEyearsmeananom[:,:,i], cmap ='RdBu', vmin=-5, vmax=5) 
#     # plt.quiver(malla3x[0:-1:2,0:-1:2],malla3y[0:-1:2,0:-1:2],ugosmean3[0:-1:2,0:-1:2,i],vgosmean3[0:-1:2,0:-1:2,i], width=0.0022, minlength=0.0000005, scale=80)
#     plt.colorbar()
#     ax.set_extent(extent)
#     #X and Y axis
#     grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
#     grid.top_labels   = False
#     grid.right_labels = False
#     grid.xformatter   = LONGITUDE_FORMATTER
#     grid.yformatter   = LATITUDE_FORMATTER
#     grid.xlabel_style = {'size': 7}
#     grid.ylabel_style = {'size': 7} 
#     ax.text(-0.1, 0.55, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax.transAxes, fontsize= 9)
#     ax.text(0.5, -0.2, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax.transAxes, fontsize= 9)
#     #Fancy things about the map
#     ax.add_feature(cpy.feature.OCEAN)
#     ax.add_feature(cpy.feature.LAND, edgecolor='white')
#     ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
#     ax.coastlines(linewidth=0.5)
#     ax.gridlines()


#     #Saving path
#     figbaltic = plt.figure(1, (8.5,6))
#     figbaltic.set_size_inches(5, 3.55)
#     figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/Baltic Sea/Velocities and KE/' + 'KE anomalies map ('+str(año)+'). Baltic Sea.png', dpi=300)  
#     plt.show()
#     plt.close()
############################################################################### 
#            Map plots                                                        #
############################################################################### 
for i, año in enumerate(years):  
    #Map and variable plot 
    figbaltic = plt.figure(1,(8.5,6))
    figbaltic.suptitle('Seasonal KE anomalies ('+str(año)+') [cm^2/s^2]', fontsize=18,fontweight='normal', y=0.94)
    ax1 = plt.subplot(2, 2, 1, projection=ccrs.PlateCarree()) 
    como = ax1.pcolormesh(mallax,mallay,KEwinteryearsmeananom[:,:,i], cmap ='RdBu', vmin=-20, vmax=20)
    ax1.set_title('Winter', fontsize=15)
    ax2 = plt.subplot(2, 2, 2, projection=ccrs.PlateCarree()) 
    ax2.pcolormesh(mallax,mallay, KEspringyearsmeananom[:,:,i], cmap ='RdBu', vmin=-20, vmax=20)
    ax2.set_title('Spring', fontsize=15)
    ax3 = plt.subplot(2, 2, 3, projection=ccrs.PlateCarree()) 
    ax3.pcolormesh(mallax,mallay,KEsummeryearsmeananom[:,:,i], cmap ='RdBu', vmin=-20, vmax=20)
    ax3.set_title('Summer', fontsize=15)
    ax4 = plt.subplot(2, 2, 4, projection=ccrs.PlateCarree()) 
    ax4.pcolormesh(mallax,mallay,KEautumnyearsmeananom[:,:,i], cmap ='RdBu', vmin=-20, vmax=20)
    ax4.set_title('Autumn', fontsize=15)
    cbar_ax = figbaltic.add_axes([0.93, 0.1,0.04,0.7])
    figbaltic.colorbar(como,cbar_ax ,orientation='vertical')
    
    # plt.quiver(mallax[0:-1:2,0:-1:2],mallay[0:-1:2,0:-1:2],ugosmean[0:-1:2,0:-1:2,i],vgosmean[0:-1:2,0:-1:2,i], width=0.001, minlength=0.000001, scale=100)
    # plt.colorbar(ax1)
    ax1.set_extent(extent)
    ax2.set_extent(extent)
    ax3.set_extent(extent)
    ax4.set_extent(extent)
    
    #X and Y axis
    grid1 = ax1.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
    grid2 = ax2.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
    grid3 = ax3.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
    grid4 = ax4.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
    grid1.top_labels   = False
    grid1.right_labels = False
    grid1.xformatter   = LONGITUDE_FORMATTER
    grid1.yformatter   = LATITUDE_FORMATTER
    grid1.xlabel_style = {'size': 7}
    grid1.ylabel_style = {'size': 7} 
    grid2.top_labels   = False
    grid2.right_labels = False
    grid2.xformatter   = LONGITUDE_FORMATTER
    grid2.yformatter   = LATITUDE_FORMATTER
    grid2.xlabel_style = {'size': 7}
    grid2.ylabel_style = {'size': 7} 
    grid3.top_labels   = False
    grid3.right_labels = False
    grid3.xformatter   = LONGITUDE_FORMATTER
    grid3.yformatter   = LATITUDE_FORMATTER
    grid3.xlabel_style = {'size': 7}
    grid3.ylabel_style = {'size': 7} 
    grid4.top_labels   = False
    grid4.right_labels = False
    grid4.xformatter   = LONGITUDE_FORMATTER
    grid4.yformatter   = LATITUDE_FORMATTER
    grid4.xlabel_style = {'size': 7}
    grid4.ylabel_style = {'size': 7} 
    ax1.text(-0.1, 0.53, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
    ax1.text(0.5, -0.2, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
    ax2.text(-0.1, 0.53, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)
    ax2.text(0.5, -0.2, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)
    ax3.text(-0.1, -0.9, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
    ax3.text(0.5, -1.62, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
    ax4.text(-0.1, -0.9, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)
    ax4.text(0.5, -1.62, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)

    #Fancy things about the map
    ax1.add_feature(cpy.feature.OCEAN)
    ax1.add_feature(cpy.feature.LAND, edgecolor='white')
    ax1.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
    ax1.coastlines(linewidth=0.5)
    ax1.gridlines()
    ax2.add_feature(cpy.feature.OCEAN)
    ax2.add_feature(cpy.feature.LAND, edgecolor='white')
    ax2.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
    ax2.coastlines(linewidth=0.5)
    ax2.gridlines()
    ax3.add_feature(cpy.feature.OCEAN)
    ax3.add_feature(cpy.feature.LAND, edgecolor='white')
    ax3.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
    ax3.coastlines(linewidth=0.5)
    ax3.gridlines()
    ax4.add_feature(cpy.feature.OCEAN)
    ax4.add_feature(cpy.feature.LAND, edgecolor='white')
    ax4.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
    ax4.coastlines(linewidth=0.5)
    ax4.gridlines()
    #Saving the plots
    figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/Baltic Sea/Velocities and KE/' + 'Seasonal KE anomalies map ('+str(año)+'). Baltic Sea.png', dpi=300)  
    plt.show()
    plt.close()
############################################################################### 
#            Map plots                                                        #
###############################################################################   
#     #Map and variable plot 
# figbaltic = plt.figure(1,(8.5,6))
# figbaltic.suptitle('Autumn KE anomalies [cm^2/s^2]', fontsize=20,fontweight='normal', y=0.97)
# for i,año in enumerate(years):
#     ax = plt.subplot(5, 2, i+1,projection=ccrs.PlateCarree()) 
#     como = ax.pcolormesh(mallax,mallay,KEautumnyearsmeananom[:,:,i], cmap ='RdBu', vmin=-10, vmax=10)
#     ax.set_title(str(año), fontsize=9, position=(1,0.5),va='center')
#     cbar_ax = figbaltic.add_axes([0.93, 0.1,0.04,0.7])
#     figbaltic.colorbar(como,cbar_ax ,orientation='vertical')
#     ax.set_extent(extent)

    
#     #X and Y axis
#     grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
#     grid.top_labels   = False
#     grid.right_labels = False
#     grid.xformatter   = LONGITUDE_FORMATTER
#     grid.yformatter   = LATITUDE_FORMATTER
#     grid.xlabel_style = {'size': 7}
#     grid.ylabel_style = {'size': 7} 
#     # ax1.text(-0.13, 0.53, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
#     # ax1.text(0.5, -0.24, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
#     # ax2.text(-0.13, 0.53, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)
#     # ax2.text(0.5, -0.24, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)
#     # ax3.text(-0.13, -1.8, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
#     # ax3.text(0.5, -2.6, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax1.transAxes, fontsize= 7)
#     # ax4.text(-0.13, -1.8, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)
#     # ax4.text(0.5, -2.6, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax2.transAxes, fontsize= 7)

#     #Fancy things about the map
#     ax.add_feature(cpy.feature.OCEAN)
#     ax.add_feature(cpy.feature.LAND, edgecolor='white')
#     ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
#     ax.coastlines(linewidth=0.5)
#     ax.gridlines()

# #Saving the plots
# figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/Gotland Basin/Velocities and KE/' + 'Autumn KE anomalies map. Baltic Sea.png', dpi=300)  
# plt.show()
# plt.close()

###############################################################################
#   Many years mean plot                                                      #
###############################################################################
#Map and variable plot
# ax = plt.axes(projection=ccrs.PlateCarree())
# plt.title('KE (2016-2020) [cm]', loc='center')
# plt.pcolormesh(mallax,mallay,KEyearsmean[:,:], cmap ='jet', vmin=0, vmax=2)
# plt.colorbar()
# ax.set_extent(extent)
# #X and Y axis
# grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.1, color='k', alpha=1, linestyle='--')
# grid.top_labels   = False
# grid.right_labels = False
# grid.xformatter   = LONGITUDE_FORMATTER
# grid.yformatter   = LATITUDE_FORMATTER
# grid.xlabel_style = {'size': 7}
# grid.ylabel_style = {'size': 7} 
# ax.text(-0.1, 0.55, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax.transAxes, fontsize= 9)
# ax.text(0.5, -0.2, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax.transAxes, fontsize= 9)
# #Fancy things about the map
# ax.add_feature(cpy.feature.OCEAN)
# ax.add_feature(cpy.feature.LAND, edgecolor='white')
# ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
# ax.coastlines(linewidth=0.5)
# ax.gridlines()
# #plt.show()
# #Saving the plots
# figbaltic = plt.figure(1, (8.5,6))
# figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/Velocities and EKE/' + 'KE (2016-2020).png', dpi=300)  
# plt.close()


###############################################################################
#   Boxes Plot                                                                #
###############################################################################
# ax    = plt.subplot(projection=ccrs.PlateCarree())
# ax.set_extent(extent)
# grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.3, color='k', alpha=1, linestyle='-')
# grid.top_labels   = False
# grid.right_labels = False
# grid.xformatter   = LONGITUDE_FORMATTER
# grid.yformatter   = LATITUDE_FORMATTER
# grid.xlabel_style = {'size': 7}
# grid.ylabel_style = {'size': 7} 
# ax.text(-0.1, 0.55, 'Latitude', va='bottom', ha='center', rotation='vertical', rotation_mode='anchor', transform=ax.transAxes, fontsize= 9)
# ax.text(0.5, -0.2, 'Longitude', va='bottom', ha='center', rotation='horizontal', rotation_mode='anchor', transform=ax.transAxes, fontsize= 9)
# ax.add_feature(cpy.feature.OCEAN)
# ax.add_feature(cpy.feature.LAND, edgecolor='white')
# ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='lightgray'))
# ax.coastlines(linewidth=0.5)
# ax.add_patch(mpatches.Rectangle(xy=[14,54], width=8, height=6, edgecolor='red', facecolor='none', alpha=1,linewidth =2, zorder=10, label='Gotland Basin'))
# ax.add_patch(mpatches.Rectangle(xy=[16,60], width=8, height=3, edgecolor='green', facecolor='none', alpha=1, linewidth =2, zorder=10, label='Sea of Bothnia'))
# ax.add_patch(mpatches.Rectangle(xy=[16,63], width=11, height=3, edgecolor='brown', facecolor='none', alpha=1, linewidth =2, zorder=10, label='Bay of Bothnia'))
# plt.legend(prop={'size': 6})
# figbaltic = plt.figure(1, (8.5,6))
# figbaltic.set_size_inches(5, 3.55)
# figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/All regions/' + 'Boxes Plot.png', dpi=300)  
# plt.show()
# plt.close()


###############################################################################
#      Anual Anomalies Temporal Series Plot (ADT and KE)                      #
###############################################################################
# plt.figure()
# #plt.title('KE ('+str(round(10000*coeff_KE1[1],2))+' mm^2/(s^2*year)) and ADT ('+str(round(100*coeff_adt1[1],3))+' (mm/year)) anual anomalies')
# plt.title('ADT (cm) anual anomalies (2011-2020)')
# plt.plot(years[:],adtspaceyearsmeananom [:], '-o',linewidth=4, color='red', label='Baltic Sea')
# plt.plot(years[:],adtspaceyearsmeananom1[:], '-o',linewidth=1, color='gold', label='Gotland Basin')
# plt.plot(years[:],adtspaceyearsmeananom2[:], '-o',linewidth=1, color='deepskyblue', label='Sea of Bothnia')
# plt.plot(years[:],adtspaceyearsmeananom3[:], '-o',linewidth=1, color='lime', label='Bay of Bothnia')
# # plt.plot(years[:],ffit_adt[:], '-', linewidth=4, color='red', label='Baltic Sea. '+str(round(10*coeff_adt[1], 3))+' mm/year')
# # plt.plot(years[:],ffit_adt1[:], '-', linewidth=1, color='gold', label='Gotland Basin. '+str(round(10*coeff_adt1[1], 3))+' mm/year')
# # plt.plot(years[:],ffit_adt2[:], '-', linewidth=1, color='deepskyblue', label='Sea of Bothnia. '+str(round(10*coeff_adt2[1], 3))+' mm/year')
# # plt.plot(years[:],ffit_adt3[:], '-', linewidth=1, color='lime', label='Bay of Bothnia. '+str(round(10*coeff_adt3[1], 3))+' mm/year')
# plt.legend()
# plt.ylim([-10,10])
# plt.xlabel('Time [years]')
# plt.ylabel('ADT [cm]')
# figbaltic = plt.figure(1, (8.5,6))
# figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/All regions/' + 'ADT Anual Anomalies (2011-2020).png', dpi=300)
# plt.close()

###############################################################################
#       Anual Temporal Series Plot                                            #
###############################################################################    
# for i,año in enumerate(years):    
#     plt.figure()
#     plt.plot(dates.num2date(time[realtime[:,i],i]),KEspacemeananom3[realtime[:,i],i],linewidth=2, color='teal')
#     plt.title('KE and ADT Anual Anomalies ('+str(año)+')', fontsize=15)
#     plt.ylim([-30,30])
#     plt.xlabel('Time [days]')
#     plt.ylabel('KE [cm^2/s^2]')
#     figbaltic = plt.figure(1, (8.5,6))
#     figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/Baltic Sea/Velocities and EKE/' + 'KE('+str(año)+').png', dpi=300)
#     plt.close()
    
###############################################################################
#      Continuous Temporal Series Plot                                        #
###############################################################################
# plt.figure()
# plt.plot(dates.num2date(totaltime[realtotaltime]),totalKEspacemeananom[realtotaltime],linewidth=2, color='teal')
# plt.plot(dates.num2date(totaltime[nonanscoeff_KE]),ffit_KE[:], color='red', linewidth=2, label=''+str(round(coeff_KE[1]*36500,2))+'mm^2/(s^2*year)')
# plt.legend()
# plt.title('KE Space-Mean Anomalies (2011-2020) [cm^2/s^2]', fontsize=14)
# #plt.ylim([-40,40])
# plt.xlabel('Time [days]')
# plt.ylabel('KE [cm^2/s^2]')
# figbaltic = plt.figure(1, (8.5,6))
# figbaltic.set_size_inches(5.4, 3.6)
# figbaltic.savefig('C:/Users/sergi/OneDrive/Escritorio/Pràctiques IMDEA/Plots/Temporal Series/' + 'KE Temporal Series Anomalies (2011-2020). Baltic Sea.png', dpi=300)  
# plt.show()
# plt.close()





