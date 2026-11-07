import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang9_p2_b1_c2_hh12(self):
                # Khai báo biến
                # Khai báo biến
                list_k = [1300, 1344, 1400, 1500, 1600, 1200]
                list_cx_cz = [(3, -4), (4, -3), (-3, -4), (-4, -3), (3, 4), (4, 3)]
                list_M = [(3840, 5120), (5120, 3840), (3840, -5120), (5120, -3840), (-3840, 5120), (-5120, 3840)]
                
                k = random.choice(list_k)
                cx, cz = random.choice(list_cx_cz)
                y_M, z_M = random.choice(list_M)
                
                x_B = k * cx
                z_B = k * cz
                OB = k * 5
                h = OB - 6400
                
                R_qd = 2 * OB
                x_I = -x_B
                z_I = -z_B
                
                val_IH_sq = x_I**2 + (z_I - z_M)**2
                IH_sym = sp.sqrt(val_IH_sq)
                
                MN_min_val = math.sqrt(y_M**2 + (R_qd - math.sqrt(val_IH_sq))**2)
                MN_min_round = round(MN_min_val)
                
                false_z_I = z_I + random.choice([100, 200, 360, -100, -200, -360])
                false_MN = MN_min_round + random.choice([10, 20, 42, -15, -25])
                
                
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
	\draw  [fill={rgb, 255:red, 10; green, 107; blue, 220 }  ,fill opacity=1 ] (281.3,131) .. controls (281.3,95.71) and (309.91,67.1) .. (345.2,67.1) .. controls (380.49,67.1) and (409.1,95.71) .. (409.1,131) .. controls (409.1,166.29) and (380.49,194.9) .. (345.2,194.9) .. controls (309.91,194.9) and (281.3,166.29) .. (281.3,131) -- cycle ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (320.45,105.8) .. controls (320.45,105.8) and (320.45,105.8) .. (320.45,105.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (306.95,93.8) .. controls (305.45,97.3) and (303.95,100.8) .. (302.45,104.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (303.7,106.3) .. controls (310.74,99.47) and (312.7,94.12) .. (312.7,102.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (313.7,104.55) .. controls (312.12,105.88) and (307.74,107.34) .. (309.2,108.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (312.7,108.8) .. controls (312.7,108.8) and (312.7,108.8) .. (312.7,108.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (316.95,108.05) .. controls (317.95,105.88) and (320.77,103.79) .. (319.95,101.55) .. controls (318.72,98.17) and (314.82,96.48) .. (311.95,94.3) .. controls (311.14,93.68) and (313.12,95.97) .. (313.7,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (307.7,89.8) .. controls (308.53,89.3) and (309.37,88.8) .. (310.2,88.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (308.2,88.3) .. controls (307.28,87.97) and (306.37,87.63) .. (305.45,87.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (304.2,91.55) .. controls (303.53,90.88) and (302.87,90.22) .. (302.2,89.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (302.45,93.8) .. controls (301.53,94.13) and (300.62,94.47) .. (299.7,94.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (300.2,97.8) .. controls (299.53,98.13) and (298.87,98.47) .. (298.2,98.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (298.7,101.8) .. controls (297.7,102.13) and (296.7,102.47) .. (295.7,102.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (296.45,104.3) .. controls (295.28,104.97) and (294.12,105.63) .. (292.95,106.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (293.95,106.8) .. controls (293.87,107.55) and (293.78,108.3) .. (293.7,109.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (298.7,106.8) .. controls (298.7,108.22) and (298.7,109.63) .. (298.7,111.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (301.7,109.55) .. controls (302.12,109.97) and (302.53,110.38) .. (302.95,110.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (305.2,110.55) .. controls (305.53,110.55) and (305.87,110.55) .. (306.2,110.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (296.45,113.8) .. controls (297.03,114.05) and (297.62,114.3) .. (298.2,114.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (335.7,155.3) .. controls (333.53,151.97) and (331.37,148.63) .. (329.2,145.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (329.2,144.55) .. controls (327.7,141.8) and (326.2,139.05) .. (324.7,136.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (331.7,157.3) .. controls (328.28,152.05) and (324.87,146.8) .. (321.45,141.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (323.7,154.55) .. controls (322.37,152.3) and (321.03,150.05) .. (319.7,147.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (341.2,154.3) .. controls (337.7,148.47) and (334.2,142.63) .. (330.7,136.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (345.2,159.8) .. controls (346.28,156.47) and (347.37,153.13) .. (348.45,149.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (347.7,152.8) .. controls (344.95,148.8) and (342.2,144.8) .. (339.45,140.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (347.7,150.8) .. controls (348.87,151.13) and (350.03,151.47) .. (351.2,151.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (349.7,154.8) .. controls (349.7,155.47) and (349.7,156.13) .. (349.7,156.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (348.45,159.8) .. controls (348.45,160.3) and (348.45,160.8) .. (348.45,161.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (344.2,161.8) .. controls (343.7,162.55) and (343.2,163.3) .. (342.7,164.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (340.7,164.05) .. controls (340.87,165.22) and (341.03,166.38) .. (341.2,167.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (338.45,168.8) .. controls (339.03,168.97) and (339.62,169.13) .. (340.2,169.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (335.2,170.3) .. controls (335.62,171.13) and (336.03,171.97) .. (336.45,172.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (335.45,172.8) .. controls (335.2,173.72) and (334.95,174.63) .. (334.7,175.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (331.7,175.05) .. controls (331.7,175.88) and (331.7,176.72) .. (331.7,177.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (330.95,173.55) .. controls (330.95,168.63) and (330.95,163.72) .. (330.95,158.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (333.95,165.3) .. controls (335.59,162.53) and (336.91,159.15) .. (339.7,157.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (332.2,161.05) .. controls (330.95,160.05) and (329.7,159.05) .. (328.45,158.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (386.7,116.8) .. controls (382.32,121.18) and (377.97,125.57) .. (373.45,129.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (373.7,127.3) .. controls (373.05,125.56) and (372.11,123.57) .. (372.7,121.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (373.7,120.05) .. controls (375.2,118.55) and (376.7,117.05) .. (378.2,115.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (378.95,114.8) .. controls (381.03,114.05) and (383.12,113.3) .. (385.2,112.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (386.7,114.3) .. controls (388.03,115.22) and (389.37,116.13) .. (390.7,117.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (393.7,119.05) .. controls (395.12,118.97) and (396.53,118.88) .. (397.95,118.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (398.95,118.8) .. controls (400.2,118.13) and (401.45,117.47) .. (402.7,116.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (403.2,117.05) .. controls (403.12,120.97) and (403.03,124.88) .. (402.95,128.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (404.7,124.3) .. controls (403.95,131.22) and (403.2,138.13) .. (402.45,145.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (399.95,128.55) .. controls (398.03,126.3) and (396.84,123.12) .. (394.2,121.8) .. controls (391.74,120.57) and (386.29,118.82) .. (385.95,121.55) .. controls (385.71,123.44) and (395.63,131.97) .. (397.95,134.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (393.7,128.8) .. controls (392.78,130.8) and (391.87,132.8) .. (390.95,134.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (389.2,133.55) .. controls (387,130.93) and (384.58,128.4) .. (381.7,126.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (380.7,127.55) .. controls (381.12,129.55) and (381.53,131.55) .. (381.95,133.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (376.95,131.3) .. controls (377.28,132.72) and (377.62,134.13) .. (377.95,135.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (395.95,134.8) .. controls (395.78,137.13) and (395.62,139.47) .. (395.45,141.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (399.95,142.05) .. controls (399.37,142.97) and (398.78,143.88) .. (398.2,144.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (396.2,134.05) .. controls (397.12,135.13) and (398.03,136.22) .. (398.95,137.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (402.2,148.3) .. controls (401.87,149.55) and (401.53,150.8) .. (401.2,152.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (399.95,149.3) .. controls (399.87,149.72) and (399.78,150.13) .. (399.7,150.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (399.7,150.8) .. controls (399.03,153.22) and (398.37,155.63) .. (397.7,158.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (390.45,96.55) .. controls (390.87,96.3) and (391.28,96.05) .. (391.7,95.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (392.45,97.05) .. controls (392.53,97.13) and (392.62,97.22) .. (392.7,97.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (387.7,96.8) .. controls (386.28,96.8) and (384.87,96.8) .. (383.45,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=5.25] [line join = round][line cap = round] (346.7,78.05) .. controls (346.28,77.8) and (345.87,77.55) .. (345.45,77.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (310.7,86.3) .. controls (311.95,86.05) and (313.2,85.8) .. (314.45,85.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (313.2,87.8) .. controls (313.62,87.47) and (314.03,87.13) .. (314.45,86.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (307.2,84.55) .. controls (307.53,84.55) and (307.87,84.55) .. (308.2,84.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (308.7,85.05) .. controls (308.62,84.63) and (308.53,84.22) .. (308.45,83.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (314.7,85.8) .. controls (316.53,85.05) and (318.37,84.3) .. (320.2,83.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (316.95,86.8) .. controls (317.78,86.13) and (318.62,85.47) .. (319.45,84.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (316.2,86.3) .. controls (315.2,87.47) and (314.2,88.63) .. (313.2,89.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (289.45,108.8) .. controls (289.87,111.47) and (290.28,114.13) .. (290.7,116.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (307.7,113.8) .. controls (309.37,113.47) and (311.03,113.13) .. (312.7,112.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (312.7,113.55) .. controls (313.2,113.72) and (313.7,113.88) .. (314.2,114.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (316.2,111.8) .. controls (315.78,112.47) and (315.37,113.13) .. (314.95,113.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (314.95,113.3) .. controls (315.37,114.88) and (315.78,116.47) .. (316.2,118.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (301.7,114.8) .. controls (301.37,116.88) and (301.03,118.97) .. (300.7,121.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (297.95,117.3) .. controls (298.78,119.05) and (299.62,120.8) .. (300.45,122.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (298.2,118.05) .. controls (298.7,119.8) and (299.2,121.55) .. (299.7,123.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (296.45,117.8) .. controls (296.95,119.13) and (297.45,120.47) .. (297.95,121.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (295.95,118.05) .. controls (296.78,119.8) and (297.62,121.55) .. (298.45,123.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (303.2,113.3) .. controls (302.87,114.3) and (302.53,115.3) .. (302.2,116.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (299.2,117.8) .. controls (299.37,118.47) and (299.53,119.13) .. (299.7,119.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (295.7,120.3) .. controls (297.7,122.13) and (299.7,123.97) .. (301.7,125.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (296.95,123.05) .. controls (298.53,123.88) and (300.12,124.72) .. (301.7,125.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (301.2,121.8) .. controls (302.95,123.63) and (304.7,125.47) .. (306.45,127.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (302.7,125.05) .. controls (303.7,125.97) and (304.7,126.88) .. (305.7,127.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (301.7,123.3) .. controls (303.37,124.47) and (304.68,127.01) .. (306.7,126.8) .. controls (308.29,126.64) and (308.2,123.97) .. (308.95,122.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (307.2,125.3) .. controls (307.37,124.8) and (307.53,124.3) .. (307.7,123.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (307.2,127.8) .. controls (308.53,128.8) and (309.87,129.8) .. (311.2,130.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (308.45,128.8) .. controls (309.7,128.88) and (310.95,128.97) .. (312.2,129.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (312.2,130.3) .. controls (312.2,131.3) and (312.2,132.3) .. (312.2,133.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (312.7,133.05) .. controls (313.7,133.38) and (314.7,133.72) .. (315.7,134.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (316.7,134.8) .. controls (318.28,136.05) and (319.87,137.3) .. (321.45,138.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (318.45,136.8) .. controls (318.45,137.47) and (318.45,138.13) .. (318.45,138.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (319.2,135.8) .. controls (320.62,134.72) and (322.03,133.63) .. (323.45,132.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (325.95,133.3) .. controls (327.37,133.05) and (328.78,132.8) .. (330.2,132.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (334.7,137.55) .. controls (335.7,137.55) and (336.7,137.55) .. (337.7,137.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (350.7,147.8) .. controls (352.55,149.65) and (356,152.28) .. (354.7,154.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (353.7,148.05) .. controls (354.7,149.13) and (355.7,150.22) .. (356.7,151.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (354.2,150.8) .. controls (353.7,149.8) and (353.2,148.8) .. (352.7,147.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (352.7,159.8) .. controls (351.95,160.88) and (351.2,161.97) .. (350.45,163.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (344.95,168.8) .. controls (344.78,169.63) and (344.62,170.47) .. (344.45,171.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (334.2,178.55) .. controls (335.03,179.22) and (335.87,179.88) .. (336.7,180.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (337.45,175.55) .. controls (338.45,175.88) and (339.45,176.22) .. (340.45,176.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (338.95,175.55) .. controls (339.87,174.47) and (340.78,173.38) .. (341.7,172.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.2,178.05) .. controls (329.45,180.3) and (330.7,182.55) .. (331.95,184.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (331.95,181.55) .. controls (332.2,182.3) and (332.45,183.05) .. (332.7,183.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (331.7,184.8) .. controls (332.95,186.38) and (334.2,187.97) .. (335.45,189.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (319.45,83.8) .. controls (320.62,83.47) and (321.78,83.13) .. (322.95,82.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (322.7,83.8) .. controls (322.37,82.63) and (322.03,81.47) .. (321.7,80.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (321.7,79.8) .. controls (324.45,79.72) and (327.2,79.63) .. (329.95,79.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.7,79.8) .. controls (327.28,80.63) and (326.87,81.47) .. (326.45,82.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.7,79.55) .. controls (330.45,80.55) and (332.2,81.55) .. (333.95,82.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (330.95,81.55) .. controls (331.28,82.97) and (331.62,84.38) .. (331.95,85.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (331.7,83.3) .. controls (331.62,84.13) and (331.53,84.97) .. (331.45,85.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (330.95,83.8) .. controls (330.2,84.38) and (329.45,84.97) .. (328.7,85.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (329.45,84.8) .. controls (330.28,85.22) and (331.12,85.63) .. (331.95,86.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (312.45,80.8) .. controls (313.12,81.22) and (313.78,81.63) .. (314.45,82.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (314.7,82.05) .. controls (315.95,81.55) and (317.2,81.05) .. (318.45,80.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (315.7,80.8) .. controls (315.45,80.22) and (315.2,79.63) .. (314.95,79.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (314.45,79.8) .. controls (314.2,79.97) and (313.95,80.13) .. (313.7,80.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (319.2,78.05) .. controls (319.7,77.88) and (320.2,77.72) .. (320.7,77.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (323.7,77.3) .. controls (324.12,76.97) and (324.53,76.63) .. (324.95,76.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.95,77.3) .. controls (329.03,76.88) and (330.12,76.47) .. (331.2,76.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (330.45,75.8) .. controls (329.95,75.47) and (329.45,75.13) .. (328.95,74.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (331.2,75.8) .. controls (332.45,75.05) and (333.7,74.3) .. (334.95,73.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (332.95,74.8) .. controls (334.95,74.38) and (336.95,73.97) .. (338.95,73.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (334.7,73.3) .. controls (334.2,73.3) and (333.7,73.3) .. (333.2,73.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (316.45,92.8) .. controls (317.7,93.63) and (318.95,94.47) .. (320.2,95.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (306.45,82.8) .. controls (308.7,83.38) and (310.95,83.97) .. (313.2,84.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (313.7,84.55) .. controls (315.62,83.97) and (317.53,83.38) .. (319.45,82.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (322.95,100.05) .. controls (325.62,96.83) and (327.56,92.36) .. (331.45,90.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.95,90.3) .. controls (328.62,89.47) and (328.28,88.63) .. (327.95,87.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.7,87.3) .. controls (326.95,89.13) and (326.2,90.97) .. (325.45,92.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (324.95,91.05) .. controls (324.95,92.13) and (324.95,93.22) .. (324.95,94.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (324.95,94.3) .. controls (324.95,94.47) and (324.95,94.63) .. (324.95,94.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (325.2,92.55) .. controls (324.03,93.97) and (322.87,95.38) .. (321.7,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (322.7,98.3) .. controls (324.38,95.27) and (329.9,91.5) .. (327.45,89.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (326.45,88.8) .. controls (326.03,89.3) and (325.62,89.8) .. (325.2,90.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (324.45,93.8) .. controls (324.12,94.47) and (323.78,95.13) .. (323.45,95.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (330.7,91.55) .. controls (331.83,90.83) and (333.99,90.67) .. (334.7,91.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (334.45,91.8) .. controls (335.45,92.88) and (336.45,93.97) .. (337.45,95.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (337.7,96.3) .. controls (337.37,97.13) and (337.03,97.97) .. (336.7,98.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (337.45,96.8) .. controls (337.52,97.47) and (337.03,98.9) .. (336.45,98.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (335.95,98.3) .. controls (336.2,97.13) and (336.45,95.97) .. (336.7,94.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (335.2,94.8) .. controls (332.78,95.3) and (330.37,95.8) .. (327.95,96.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.7,94.8) .. controls (330.7,94.05) and (332.7,93.3) .. (334.7,92.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (333.2,92.8) .. controls (331.95,93.38) and (330.7,93.97) .. (329.45,94.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (329.95,93.3) .. controls (330.87,92.05) and (331.78,90.8) .. (332.7,89.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.2,96.55) .. controls (327.2,96.55) and (327.2,96.55) .. (327.2,96.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.2,96.3) .. controls (329.03,97.72) and (329.87,99.13) .. (330.7,100.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.7,98.3) .. controls (328.28,99.13) and (327.87,99.97) .. (327.45,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.45,97.05) .. controls (326.7,99.05) and (325.95,101.05) .. (325.2,103.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (325.7,98.05) .. controls (325.37,100.13) and (325.03,102.22) .. (324.7,104.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.45,100.3) .. controls (329.28,100.97) and (330.12,101.63) .. (330.95,102.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (330.95,101.55) .. controls (331.45,101.3) and (331.95,101.05) .. (332.45,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (335.2,76.8) .. controls (339.37,75.55) and (343.53,74.3) .. (347.7,73.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (347.7,73.05) .. controls (351.53,73.63) and (355.37,74.22) .. (359.2,74.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (348.7,73.8) .. controls (351.39,74.73) and (354.18,76.74) .. (356.95,76.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (350.7,75.55) .. controls (353.03,76.22) and (355.37,76.88) .. (357.7,77.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (349.7,74.8) .. controls (351.7,76.13) and (353.7,77.47) .. (355.7,78.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (350.95,75.55) .. controls (350.78,77.97) and (350.62,80.38) .. (350.45,82.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (350.7,81.8) .. controls (352.62,81.3) and (354.53,80.8) .. (356.45,80.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (353.7,79.8) .. controls (353.37,79.13) and (353.03,78.47) .. (352.7,77.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (352.45,79.8) .. controls (350.95,77.8) and (349.45,75.8) .. (347.95,73.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (341.2,76.05) .. controls (340.87,76.3) and (340.53,76.55) .. (340.2,76.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (339.95,77.55) .. controls (340.62,78.63) and (341.28,79.72) .. (341.95,80.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (341.45,78.05) .. controls (342.12,79.05) and (342.78,80.05) .. (343.45,81.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (338.7,76.8) .. controls (340.78,79.38) and (342.87,81.97) .. (344.95,84.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (342.2,81.8) .. controls (342.62,83.47) and (343.03,85.13) .. (343.45,86.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (344.95,81.3) .. controls (345.87,81.8) and (346.78,82.3) .. (347.7,82.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (349.7,79.8) .. controls (349.53,80.97) and (349.37,82.13) .. (349.2,83.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (349.45,82.8) .. controls (347.95,84.22) and (346.45,85.63) .. (344.95,87.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (347.7,81.55) .. controls (346.95,82.63) and (346.2,83.72) .. (345.45,84.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (341.95,81.8) .. controls (341.87,82.63) and (341.78,83.47) .. (341.7,84.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (344.95,81.3) .. controls (344.87,83.05) and (344.78,84.8) .. (344.7,86.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (341.7,82.8) .. controls (342.37,84.22) and (343.03,85.63) .. (343.7,87.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (341.45,84.8) .. controls (342.53,86.13) and (343.62,87.47) .. (344.7,88.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (379.95,96.3) .. controls (379.03,97.13) and (378.12,97.97) .. (377.2,98.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (378.2,99.55) .. controls (378.7,100.63) and (379.2,101.72) .. (379.7,102.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (379.45,98.8) .. controls (380.2,99.8) and (380.95,100.8) .. (381.7,101.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (384.45,101.05) .. controls (382.45,102.3) and (380.45,103.55) .. (378.45,104.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (379.7,101.8) .. controls (378.7,102.47) and (377.7,103.13) .. (376.7,103.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (377.2,102.8) .. controls (375.78,102.72) and (374.37,102.63) .. (372.95,102.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (372.95,103.05) .. controls (373.53,104.55) and (374.12,106.05) .. (374.7,107.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (375.7,107.8) .. controls (377.03,106.8) and (378.37,105.8) .. (379.7,104.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (377.7,106.8) .. controls (377.28,106.3) and (376.87,105.8) .. (376.45,105.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (375.45,105.3) .. controls (376.13,104.81) and (377.45,104.38) .. (377.95,105.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (376.95,105.55) .. controls (377.95,104.63) and (378.95,103.72) .. (379.95,102.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (387.7,92.3) .. controls (388.28,91.55) and (388.87,90.8) .. (389.45,90.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (389.45,89.8) .. controls (389.53,89.3) and (389.62,88.8) .. (389.7,88.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (390.95,88.8) .. controls (391.78,90.13) and (392.62,91.47) .. (393.45,92.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (391.45,91.8) .. controls (391.87,92.55) and (392.28,93.3) .. (392.7,94.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (393.7,91.55) .. controls (395.53,94.63) and (397.37,97.72) .. (399.2,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (395.45,96.3) .. controls (397.2,98.97) and (398.95,101.63) .. (400.7,104.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (398.95,99.8) .. controls (400.03,101.97) and (401.12,104.13) .. (402.2,106.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (397.2,101.55) .. controls (398.03,103.13) and (398.87,104.72) .. (399.7,106.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.45,99.05) .. controls (396.28,100.63) and (396.12,102.22) .. (395.95,103.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (392.7,99.8) .. controls (395.05,103.46) and (395.57,104.54) .. (394.7,102.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (387.45,100.55) .. controls (388.62,102.22) and (389.78,103.88) .. (390.95,105.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (387.45,101.8) .. controls (387.7,102.38) and (387.95,102.97) .. (388.2,103.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (386.95,101.3) .. controls (388.2,102.72) and (389.45,104.13) .. (390.7,105.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (388.7,104.3) .. controls (389.2,104.55) and (389.7,104.8) .. (390.2,105.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (389.45,103.8) .. controls (387.78,103.13) and (386.12,102.47) .. (384.45,101.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.45,114.55) .. controls (396.95,113.63) and (397.45,112.72) .. (397.95,111.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (397.7,115.3) .. controls (398.78,114.55) and (399.87,113.8) .. (400.95,113.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (398.7,112.05) .. controls (400.2,112.63) and (401.7,113.22) .. (403.2,113.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (401.2,113.05) .. controls (405.06,111.51) and (405.9,112.5) .. (404.7,111.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (405.7,114.05) .. controls (405.37,113.13) and (405.03,112.22) .. (404.7,111.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (403.2,107.55) .. controls (403.78,108.63) and (404.37,109.72) .. (404.95,110.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (394.7,159.55) .. controls (395.37,161.22) and (396.03,162.88) .. (396.7,164.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (402.56,154.86) .. controls (401.15,157.99) and (399.75,161.11) .. (398.34,164.24) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.95,162.55) .. controls (396.53,164.63) and (396.12,166.72) .. (395.7,168.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (396.45,165.3) .. controls (396.45,166.47) and (396.45,167.63) .. (396.45,168.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (387.45,84.55) .. controls (385.78,83.05) and (384.12,81.55) .. (382.45,80.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (382.2,79.55) .. controls (381.37,79.97) and (380.53,80.38) .. (379.7,80.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (379.45,81.55) .. controls (378.62,83.3) and (377.78,85.05) .. (376.95,86.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (376.95,86.8) .. controls (377.87,87.63) and (378.78,88.47) .. (379.7,89.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (379.7,89.3) .. controls (381.03,89.22) and (382.37,89.13) .. (383.7,89.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (383.7,88.8) .. controls (383.2,86.38) and (382.7,83.97) .. (382.2,81.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (381.7,81.8) .. controls (381.45,83.63) and (381.2,85.47) .. (380.95,87.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (380.7,82.8) .. controls (380.28,84.3) and (379.87,85.8) .. (379.45,87.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (379.7,87.3) .. controls (380.53,87.55) and (381.37,87.8) .. (382.2,88.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (384.2,83.55) .. controls (385.7,84.88) and (387.2,86.22) .. (388.7,87.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (381.7,86.3) .. controls (381.45,86.72) and (381.2,87.13) .. (380.95,87.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (378.7,86.55) .. controls (379.03,86.97) and (379.37,87.38) .. (379.7,87.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (383.7,90.05) .. controls (383.62,90.3) and (383.53,90.55) .. (383.45,90.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (371.7,89.55) .. controls (373.45,91.05) and (375.2,92.55) .. (376.95,94.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (372.7,90.55) .. controls (371.62,91.05) and (370.53,91.55) .. (369.45,92.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (369.45,92.55) .. controls (369.53,93.3) and (369.62,94.05) .. (369.7,94.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (370.2,94.8) .. controls (371.2,93.8) and (372.2,92.8) .. (373.2,91.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (373.7,92.55) .. controls (374.53,93.22) and (375.37,93.88) .. (376.2,94.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (376.2,94.8) .. controls (375.7,95.13) and (375.2,95.47) .. (374.7,95.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (317.95,122.55) .. controls (319.87,122.55) and (321.78,122.55) .. (323.7,122.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (321.7,123.05) .. controls (323.2,123.3) and (324.7,123.55) .. (326.2,123.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (321.7,123.05) .. controls (321.53,123.05) and (321.37,123.05) .. (321.2,123.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (329.7,124.05) .. controls (329.78,124.05) and (329.87,124.05) .. (329.95,124.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (317.2,124.55) .. controls (317.37,124.55) and (317.53,124.55) .. (317.7,124.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (313.7,99.8) .. controls (317.2,100.05) and (320.7,100.3) .. (324.2,100.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (330.7,94.05) .. controls (331.78,93.97) and (332.87,93.88) .. (333.95,93.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (312.45,108.8) .. controls (312.95,109.55) and (313.45,110.3) .. (313.95,111.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (383.7,100.3) .. controls (384.7,100.47) and (385.7,100.63) .. (386.7,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (377.45,104.3) .. controls (376.87,104.22) and (376.28,104.13) .. (375.7,104.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (380.2,84.8) .. controls (379.7,84.8) and (379.2,84.8) .. (378.7,84.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (380.2,85.05) .. controls (380.62,84.72) and (381.03,84.38) .. (381.45,84.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (394.45,97.8) .. controls (394.95,98.72) and (395.45,99.63) .. (395.95,100.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (404.95,129.3) .. controls (405.12,131.63) and (405.28,133.97) .. (405.45,136.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (404.7,138.8) .. controls (404.62,140.63) and (404.53,142.47) .. (404.45,144.3) ;
	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (303.42,128.94) .. controls (295.59,113.64) and (304.53,93.4) .. (323.41,83.72) .. controls (342.28,74.05) and (363.94,78.62) .. (371.78,93.91) .. controls (379.61,109.21) and (370.67,129.45) .. (351.79,139.13) .. controls (332.92,148.8) and (311.26,144.23) .. (303.42,128.94) -- cycle ;
	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (288.47,148.64) .. controls (275.09,122.54) and (288.19,89.11) .. (317.72,73.98) .. controls (347.26,58.84) and (382.04,67.74) .. (395.42,93.84) .. controls (408.79,119.94) and (395.69,153.37) .. (366.16,168.51) .. controls (336.62,183.64) and (301.84,174.74) .. (288.47,148.64) -- cycle ;
	\draw  [line width=0.75]  (281.3,131) .. controls (281.3,95.71) and (309.91,67.1) .. (345.2,67.1) .. controls (380.49,67.1) and (409.1,95.71) .. (409.1,131) .. controls (409.1,166.29) and (380.49,194.9) .. (345.2,194.9) .. controls (309.91,194.9) and (281.3,166.29) .. (281.3,131) -- cycle ;
	\draw  [draw opacity=0] (407.26,122.44) .. controls (431.84,141.42) and (444.95,161.39) .. (438.88,174.47) .. controls (429.73,194.2) and (380.36,190.74) .. (328.62,166.73) .. controls (276.88,142.73) and (242.36,107.27) .. (251.52,87.53) .. controls (257.31,75.04) and (279.22,71.85) .. (307.65,77.27) -- (345.2,131) -- cycle ; \draw   (407.26,122.44) .. controls (431.84,141.42) and (444.95,161.39) .. (438.88,174.47) .. controls (429.73,194.2) and (380.36,190.74) .. (328.62,166.73) .. controls (276.88,142.73) and (242.36,107.27) .. (251.52,87.53) .. controls (257.31,75.04) and (279.22,71.85) .. (307.65,77.27) ;  
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (254.96,112.71) -- (237.63,96.75) -- (238.36,95.96) -- (255.69,111.92) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (238.44,112.64) -- (248.37,91.24) -- (258.37,100.01) -- (248.45,121.41) -- cycle ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (245.63,118.52) -- (255.14,97.72) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (242.33,115.75) -- (251.84,94.95) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (253.27,110.77) -- (243.54,101.88) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (250.88,115.85) -- (241.16,106.96) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (255.93,105.02) -- (246.2,96.13) ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (226.39,102.1) -- (236.32,80.7) -- (246.33,89.47) -- (236.4,110.87) -- cycle ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (233.58,107.98) -- (243.1,87.18) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (230.28,105.21) -- (239.79,84.41) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (241.22,100.23) -- (231.5,91.34) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (238.84,105.31) -- (229.11,96.42) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (243.88,94.48) -- (234.15,85.59) ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (265.11,103.75) -- (270.57,102.14) -- (276.01,110.5) -- (272.34,114.85) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (270.57,102.14) .. controls (271.31,101.66) and (273.13,103.14) .. (274.63,105.45) .. controls (276.14,107.76) and (276.75,110.02) .. (276.01,110.5) .. controls (275.27,110.98) and (273.46,109.5) .. (271.95,107.19) .. controls (270.45,104.89) and (269.83,102.63) .. (270.57,102.14) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (264.91,104.28) -- (271.01,102.55) -- (272.42,103.46) -- (266.32,105.2) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (266.33,102.25) .. controls (267.11,101.75) and (269.6,104.2) .. (271.9,107.73) .. controls (274.2,111.26) and (275.44,114.53) .. (274.66,115.04) .. controls (273.88,115.55) and (271.39,113.09) .. (269.09,109.56) .. controls (266.79,106.03) and (265.55,102.76) .. (266.33,102.25) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (266.33,102.25) -- (274.66,115.04) -- (270.08,118.02) -- (261.75,105.23) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (261.75,105.23) .. controls (262.53,104.73) and (265.02,107.18) .. (267.32,110.71) .. controls (269.63,114.24) and (270.86,117.52) .. (270.08,118.02) .. controls (269.31,118.53) and (266.81,116.08) .. (264.51,112.54) .. controls (262.21,109.01) and (260.98,105.74) .. (261.75,105.23) -- cycle ;
	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (262.04,105.67) .. controls (262.66,105.26) and (264.91,107.6) .. (267.05,110.89) .. controls (269.19,114.18) and (270.42,117.18) .. (269.8,117.58) .. controls (269.17,117.99) and (266.93,115.65) .. (264.79,112.37) .. controls (262.64,109.08) and (261.41,106.08) .. (262.04,105.67) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (261.5,106.35) .. controls (262.21,105.88) and (264.46,108.07) .. (266.52,111.23) .. controls (268.58,114.4) and (269.67,117.34) .. (268.96,117.8) .. controls (268.25,118.26) and (266,116.08) .. (263.94,112.91) .. controls (261.88,109.75) and (260.79,106.81) .. (261.5,106.35) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (261.5,106.35) -- (268.96,117.8) -- (264.77,120.53) -- (257.31,109.08) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (257.31,109.08) .. controls (258.02,108.61) and (260.27,110.8) .. (262.33,113.97) .. controls (264.39,117.13) and (265.48,120.07) .. (264.77,120.53) .. controls (264.06,121) and (261.81,118.81) .. (259.75,115.64) .. controls (257.69,112.48) and (256.6,109.54) .. (257.31,109.08) -- cycle ;
	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (257.57,109.47) .. controls (258.14,109.1) and (260.16,111.18) .. (262.08,114.13) .. controls (264,117.07) and (265.09,119.77) .. (264.52,120.14) .. controls (263.94,120.51) and (261.92,118.43) .. (260,115.48) .. controls (258.08,112.53) and (256.99,109.84) .. (257.57,109.47) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (257.59,109.8) .. controls (258.17,109.43) and (260.12,111.4) .. (261.95,114.21) .. controls (263.78,117.02) and (264.8,119.6) .. (264.22,119.98) .. controls (263.65,120.35) and (261.69,118.38) .. (259.86,115.57) .. controls (258.03,112.76) and (257.02,110.18) .. (257.59,109.8) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (257.59,109.8) -- (264.22,119.98) -- (260.82,122.19) -- (254.2,112.02) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (254.2,112.02) .. controls (254.77,111.64) and (256.72,113.61) .. (258.55,116.42) .. controls (260.38,119.23) and (261.4,121.82) .. (260.82,122.19) .. controls (260.25,122.57) and (258.29,120.6) .. (256.46,117.79) .. controls (254.63,114.98) and (253.62,112.39) .. (254.2,112.02) -- cycle ;
	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (254.42,112.37) .. controls (254.89,112.06) and (256.65,113.94) .. (258.35,116.56) .. controls (260.06,119.17) and (261.06,121.54) .. (260.6,121.84) .. controls (260.13,122.15) and (258.37,120.27) .. (256.67,117.65) .. controls (254.96,115.04) and (253.96,112.67) .. (254.42,112.37) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (253.92,113.11) .. controls (254.64,112.64) and (256.52,114.25) .. (258.12,116.71) .. controls (259.72,119.17) and (260.43,121.54) .. (259.72,122) .. controls (259,122.47) and (257.12,120.86) .. (255.52,118.4) .. controls (253.92,115.94) and (253.21,113.57) .. (253.92,113.11) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (254.24,112.9) -- (260.04,121.79) -- (254.78,125.22) -- (248.98,116.32) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (248.98,116.32) .. controls (249.87,115.74) and (251.9,117.26) .. (253.5,119.72) .. controls (255.1,122.18) and (255.67,124.64) .. (254.78,125.22) .. controls (253.88,125.8) and (251.86,124.28) .. (250.26,121.83) .. controls (248.66,119.37) and (248.09,116.91) .. (248.98,116.32) -- cycle ;
	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (249.18,116.63) .. controls (249.9,116.16) and (251.69,117.64) .. (253.18,119.92) .. controls (254.67,122.21) and (255.3,124.45) .. (254.58,124.92) .. controls (253.86,125.38) and (252.07,123.91) .. (250.58,121.62) .. controls (249.09,119.33) and (248.46,117.1) .. (249.18,116.63) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (248.87,117.24) .. controls (249.19,117.03) and (250.54,118.52) .. (251.87,120.58) .. controls (253.21,122.63) and (254.03,124.46) .. (253.71,124.67) .. controls (253.39,124.88) and (252.04,123.39) .. (250.71,121.34) .. controls (249.37,119.28) and (248.55,117.45) .. (248.87,117.24) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (249.01,117.15) -- (253.85,124.58) -- (251.49,126.12) -- (246.65,118.69) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (246.65,118.69) .. controls (247.05,118.43) and (248.46,119.88) .. (249.79,121.93) .. controls (251.13,123.98) and (251.89,125.86) .. (251.49,126.12) .. controls (251.08,126.38) and (249.67,124.93) .. (248.34,122.88) .. controls (247,120.83) and (246.24,118.95) .. (246.65,118.69) -- cycle ;
	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (246.69,118.66) .. controls (247.3,118.26) and (248.88,119.6) .. (250.22,121.66) .. controls (251.55,123.71) and (252.14,125.69) .. (251.53,126.09) .. controls (250.91,126.49) and (249.33,125.15) .. (248,123.1) .. controls (246.66,121.05) and (246.07,119.06) .. (246.69,118.66) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (247.3,121.28) .. controls (247.7,121.02) and (248.49,121.52) .. (249.06,122.41) .. controls (249.64,123.29) and (249.78,124.22) .. (249.38,124.48) .. controls (248.98,124.74) and (248.19,124.24) .. (247.61,123.35) .. controls (247.04,122.47) and (246.89,121.54) .. (247.3,121.28) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (261.53,113.26) -- (262.65,114.98) -- (255.02,119.95) -- (253.9,118.23) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (260.1,120.08) -- (256.2,122.46) -- (255.84,121.3) -- (259.74,118.91) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (256.71,114.17) -- (252.81,116.55) -- (251.8,115.79) -- (255.7,113.4) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (263.87,107.68) -- (260.07,110.22) -- (259.19,109.39) -- (262.99,106.84) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (268.82,103.84) -- (264.7,106.59) -- (263.77,105.71) -- (267.89,102.95) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (259.38,110.75) -- (256.22,112.87) -- (255.46,112.14) -- (258.63,110.03) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (255.5,113.1) -- (250.77,116.1) -- (250.19,115.81) -- (254.92,112.81) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (249.82,117.08) -- (247.67,118.44) -- (247.99,118.59) -- (250.14,117.23) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (234.69,117.71) .. controls (238.28,115.38) and (244.06,117.9) .. (247.61,123.35) .. controls (251.16,128.8) and (251.13,135.11) .. (247.55,137.45) .. controls (243.96,139.79) and (238.18,137.26) .. (234.63,131.81) .. controls (231.07,126.36) and (231.1,120.05) .. (234.69,117.71) -- cycle ;
	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (233.45,118.52) .. controls (236.35,116.63) and (241.58,119.52) .. (245.13,124.97) .. controls (248.68,130.42) and (249.21,136.37) .. (246.31,138.26) .. controls (243.41,140.15) and (238.18,137.26) .. (234.63,131.81) .. controls (231.07,126.36) and (230.55,120.41) .. (233.45,118.52) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (244.23,124.68) -- (244.86,125.64) -- (241.64,127.73) -- (241.02,126.77) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (240.16,120.35) -- (240.52,120.64) -- (229.44,134.83) -- (229.08,134.54) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (246.81,137) -- (246.77,137.45) -- (229.19,135.82) -- (229.23,135.38) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (232.12,124.8) -- (232.52,124.93) -- (229.48,134.67) -- (229.08,134.54) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (231.81,132.87) .. controls (231.99,132.75) and (232.23,132.8) .. (232.34,132.98) -- (232.98,133.95) .. controls (233.09,134.13) and (233.04,134.37) .. (232.86,134.49) -- (227.75,137.82) .. controls (227.57,137.94) and (227.33,137.89) .. (227.21,137.71) -- (226.58,136.74) .. controls (226.46,136.56) and (226.51,136.32) .. (226.69,136.2) -- cycle ;
	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (263.2,118.71) -- (280.89,134.27) -- (280.17,135.09) -- (262.49,119.52) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (279.72,118.41) -- (270.28,140.03) -- (260.07,131.48) -- (269.51,109.87) -- cycle ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (272.39,112.7) -- (263.36,133.71) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (275.76,115.39) -- (266.72,136.4) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (264.93,120.62) -- (274.86,129.28) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (267.2,115.48) -- (277.13,124.15) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (262.41,126.42) -- (272.33,135.09) ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 9; green, 52; blue, 104 }  ,fill opacity=1 ] (292,128.68) -- (282.56,150.29) -- (272.36,141.75) -- (281.8,120.13) -- cycle ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (284.68,122.96) -- (275.64,143.97) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (288.04,125.65) -- (279,146.67) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (277.21,130.88) -- (287.14,139.55) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (279.49,125.75) -- (289.41,134.41) ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.64 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (274.69,136.69) -- (284.62,145.35) ;
\end{tikzpicture}'''
                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Vệ tinh hoạt động dựa trên nguyên lý của vật lý Newton. Một vật thể bị kéo bởi một lực hấp dẫn từ một vật thể khác sẽ chuyển động theo một quỹ đạo elip xung quanh vật thể đó. Để đưa vệ tinh lên quỹ đạo, người ta sử dụng các loại tên lửa đẩy khác nhau để cung cấp cho vệ tinh động lượng cần thiết để thoát khỏi trọng lực của Trái Đất và duy trì quỹ đạo ổn định. Để thuận tiện ta quy ước một quỹ đạo gần tròn thành một đường tròn. Trong hệ tọa độ $Oxyz$ , gốc tọa độ là tâm trái đất, một vệ tinh nhân tạo có quỹ đạo được coi như một đường tròn có bán kính $%s$ km có điểm xuất phát là điểm $B\\left(%s;0;%s\\right)$ và đây cũng là điểm gần Trái Đất nhất của vệ tinh. Quỹ đạo của vệ tinh này nằm trên mặt phẳng vuông góc với trục tung và có tâm nằm trên đường thẳng $OB$. Coi trái đất là hình cầu hoàn hảo có bán kính bằng $6400$ km.}{%s}''' 
                                 % (R_qd, x_B, z_B, hinhve))
                
                ########################################################################
                # Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Phương trình mặt phẳng chứa quỹ đạo của vệ tinh là $y = 0$'
                nb_da_1_s = 'Phương trình mặt phẳng chứa quỹ đạo của vệ tinh là $x + z = 0$'
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                nb_da_1 = random.choice(list_nb_da_1)
                
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]
                
                # Nội dung lời giải
                loigiai_nb_1 = ('''Quỹ đạo của vệ tinh này nằm trên mặt phẳng vuông góc với trục tung nên một vectơ chỉ phương của mặt phẳng chứa quỹ đạo của vệ tinh là $\\left(0;1;0\\right)$.\\\\
                Khi đó phương trình mặt phẳng chứa quỹ đạo của vệ tinh có dạng $y + a = 0$. \\\\
                Quỹ đạo đi qua điểm $B\\left(%s;0;%s\\right)$ nên $0 + a = 0 \\Rightarrow a = 0$.\\\\
                Vậy phương trình mặt phẳng chứa quỹ đạo của vệ tinh là $y = 0$.''' 
                                % (x_B, z_B))
                
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]
                
                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))
                
                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)
                
                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
                
                ########################################################################
                # Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Khi xuất phát tại điểm $B$ vệ tinh đang ở độ cao $%s$ km so với mặt đất' % (h)
                th_da_1_s = 'Khi xuất phát tại điểm $B$ vệ tinh đang ở độ cao $%s$ km so với mặt đất' % (h + random.choice([100, 200, 300, -100]))
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                th_da_1 = random.choice(list_th_da_1)
                
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]
                
                # Nội dung lời giải
                loigiai_th_1 = ('''Khoảng cách ngắn nhất từ Trái Đất đến vệ tinh là:
                $$OB - R = \\sqrt{%s^2 + 0^2 + \\left(%s\\right)^2} - 6400 = %s \\text{ km}$$
                Vậy khi xuất phát tại điểm $B$ thì vệ tinh đang ở độ cao $%s$ km so với mặt đất.''' 
                                % (x_B, z_B, h, h))
                
                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]
                
                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))
                
                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)
                
                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
                
                ######################################################################## 
                # Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Quỹ đạo của vệ tinh là đường tròn có tâm $I\\left(%s;0;%s\\right)$' % (x_I, z_I)
                vd_da_1_s = 'Quỹ đạo của vệ tinh là đường tròn có tâm $I\\left(%s;0;%s\\right)$' % (x_I, false_z_I)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                vd_da_1 = random.choice(list_vd_da_1)
                
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]
                
                # Nội dung lời giải
                loigiai_vd_1 = ('''Quỹ đạo của vệ tinh có tâm nằm trên đường thẳng $OB$ nên tâm $I$ nằm trên đường thẳng $OB$.\\\\
                Mặt khác: $IB = R_{qd} = %s = 2.OB$ nên $O$ là trung điểm của $IB$.\\\\
                Khi đó $\\left\\{\\begin{matrix} x_I = 2x_O - x_B \\\\ y_I = 2y_O - y_B \\\\ z_I = 2z_O - z_B \\end{matrix}\\right. \\Leftrightarrow \\left\\{\\begin{matrix} x_I = %s \\\\ y_I = 0 \\\\ z_I = %s \\end{matrix}\\right.$ nên tọa độ điểm $I\\left(%s;0;%s\\right)$.''' 
                                % (R_qd, x_I, z_I, x_I, z_I))
                
                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]
                
                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))
                
                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)
                
                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
                
                ######################################################################## 
                # Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Khi Trái Đất quay, điểm cực Nam và cực Bắc của Trái Đất không thay đổi vị trí. Biết rằng điểm cực Nam của Trái Đất có tọa độ là $M\\left(0;%s;%s\\right)$. Khoảng cách gần nhất giữa vệ tinh và điểm cực Nam bằng $%s$ km (Kết quả làm tròn đến hàng đơn vị)' % (y_M, z_M, MN_min_round)
                vdc_da_1_s = 'Khi Trái Đất quay, điểm cực Nam và cực Bắc của Trái Đất không thay đổi vị trí. Biết rằng điểm cực Nam của Trái Đất có tọa độ là $M\\left(0;%s;%s\\right)$. Khoảng cách gần nhất giữa vệ tinh và điểm cực Nam bằng $%s$ km (Kết quả làm tròn đến hàng đơn vị)' % (y_M, z_M, false_MN)
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                vdc_da_1 = random.choice(list_vdc_da_1)
                
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]
                
                # Nội dung lời giải
                loigiai_vdc_1 = ('''Gọi $H$ là hình chiếu của $M$ lên mặt phẳng quỹ đạo $y = 0 \\Rightarrow H\\left(0;0;%s\\right)$\\\\
                Khi đó: $MH = d\\left(M,\\left(y=0\\right)\\right) = %s$; $IH = \\sqrt{%s^2 + \\left(%s - %s\\right)^2} = %s$\\\\
                Từ đó suy ra: $NH = IN - IH = %s - %s$\\\\
                Nối $I$ và $H$ cắt quỹ đạo tại $N$ thì khi đó:\\\\
                $MN_{\\min} = \\sqrt{MH^2 + NH^2} = \\sqrt{%s^2 + \\left(%s - %s\\right)^2} \\approx %s$ km.''' 
                                 % (z_M, abs(y_M), x_I, z_I, z_M, latex(IH_sym), R_qd, latex(IH_sym), abs(y_M), R_qd, latex(IH_sym), MN_min_round))
                
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]
                
                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                
                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)
                
                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
                
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)
                
                # Lặp đến khi đáp án có từ 1 đến 3 đúng
                while True:
                    nb_da_1 = random.choice(list_nb_da_1)
                    th_da_1 = random.choice(list_th_da_1)
                    vd_da_1 = random.choice(list_vd_da_1)
                    vdc_da_1 = random.choice(list_vdc_da_1)
                
                    answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                    true_count = count_true_answers(answers)
                
                    if 1 <= true_count <= 3:
                        break
                
                # Gán lại vào list
                list_nb_1 = [nb_da_1]
                list_th_1 = [th_da_1]
                list_vd_1 = [vd_da_1]
                list_vdc_1 = [vdc_da_1]
                
                combined_nb = list(zip(list_nb_1, list_nb_2))
                combined_th = list(zip(list_th_1, list_th_2))
                combined_vd = list(zip(list_vd_1, list_vd_2))
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                
                random.shuffle(combined_nb)
                random.shuffle(combined_th)
                random.shuffle(combined_vd)
                random.shuffle(combined_vdc)
                
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
                
                # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+
                    str(noidungcauhoi)+ '\n'
                    '\\choiceTFn \n'
                    '{'+str(shuffled_answers_nb[0])+'}\n'
                    '{'+str(shuffled_answers_th[0])+'}\n'
                    '{'+str(shuffled_answers_vd[0])+'}\n'
                    '{'+str(shuffled_answers_vdc[0])+'}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item '+str(shuffled_solutions_nb[0])+'\n'
                    '\\item '+str(shuffled_solutions_th[0])+'\n'
                    '\\item '+str(shuffled_solutions_vd[0])+'\n'
                    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n\\end{minipage} \n\n')
                return content